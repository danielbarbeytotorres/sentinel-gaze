import cv2
import mediapipe as mp
import tkinter as tk
import logging
import time
import os
import json
import hashlib

def load_configuration():
    with open('config.json', 'r') as f:
        return json.load(f)

CONF = load_configuration()

if not os.path.exists(CONF['paths']['evidence_dir']):
    os.makedirs(CONF['paths']['evidence_dir'])

# --- LOGGING ---
logging.basicConfig(
    filename=CONF['paths']['log_file'],
    level=logging.INFO,
    format='%(asctime)s - [SECURITY] - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# --- INTEGRITY ---
def generate_verification_hash():
    sha256_hash = hashlib.sha256()
    logging.shutdown()
    try:
        with open(CONF['paths']['log_file'], "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        hash_res = sha256_hash.hexdigest()
        logging.info(f"INTEGRITY: Session digital signature (SHA-256): {hash_res}")
        print(f"\n🛡️  [AUDIT] Integrity hash generated: {hash_res}")
    except FileNotFoundError:
        print("\n⚠️ [AUDIT] Log file not found. Hash skipped.")

def register_visual_evidence(frame):
    timestamp = int(time.time())
    file_path = os.path.join(CONF['paths']['evidence_dir'], f"evidence_{timestamp}.jpg")
    cv2.imwrite(file_path, frame)
    logging.warning(f"INCIDENT: Visual evidence stored at: {file_path}")

# --- OVERLAY (GUI) ---
root = tk.Tk()
root.attributes("-topmost", True)
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
root.geometry(f"{sw}x{sh}+0+0")
root.configure(bg='black') 
root.overrideredirect(True)
root.withdraw()

ui_text = tk.StringVar()
alert_label = tk.Label(root, textvariable=ui_text, fg="red", bg="black", font=("Courier New", 40, "bold"))
alert_label.pack(expand=True)

mp_face_mesh = mp.solutions.face_mesh

def run_sentinel():
    video_capture = cv2.VideoCapture(0)
    
    # VARIABLES
    ts_absence_start = None
    lock_state = False
    ts_distraction_start = None # Usaremos siempre esta (con T)
    distraction_state = False
    ts_last_intruder_incident = 0

    with mp_face_mesh.FaceMesh(max_num_faces=5, refine_landmarks=True) as face_mesh:
        print("📸 Calibrating biometric sensors...")
        time.sleep(2) 
        reference_threshold = 0.58 

        print("\n----------------------------------------------------------")
        print("---- SENTINEL-GAZE: Endpoint Monitoring Active ----")
        print("----------------------------------------------------------")

        while video_capture.isOpened():
            ret, frame = video_capture.read()
            if not ret: break
            
            raw_frame = frame.copy() 
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            analysis = face_mesh.process(rgb_frame)
            
            faces_detected = len(analysis.multi_face_landmarks) if analysis.multi_face_landmarks else 0
            now = time.time()
            
            trigger_alert = False
            alert_msg = ""

            # --- ZERO TRUST ---
            if faces_detected == 0:
                if ts_absence_start is None: 
                    ts_absence_start = now
                elif now - ts_absence_start > CONF['settings']['lock_timeout'] and not lock_state:
                    logging.critical("SECURITY POLICY: Workstation locked due to operator absence.")
                    lock_state = True
                    if CONF['settings']['real_lock_enabled']:
                        print("🔒 [LOCK] Executing system lock...")
                        os.system('rundll32.exe user32.dll,LockWorkStation')
            else:
                if lock_state:
                    absence_duration = now - ts_absence_start
                    logging.info(f"AUDIT: Session resumed after {absence_duration:.2f}s of inactivity.")
                ts_absence_start = None
                lock_state = False

            # --- SHOULDER SURFING ---
            if faces_detected > 1:
                trigger_alert = True
                alert_msg = "⚠️ SECURITY ALERT ⚠️\nUNAUTHORIZED ACCESS DETECTED"
                if now - ts_last_intruder_incident > 15.0:
                    register_visual_evidence(raw_frame)
                    ts_last_intruder_incident = now

            # --- MONITOR ATTENTION ---
            elif faces_detected == 1:
                eye_y_position = analysis.multi_face_landmarks[0].landmark[159].y
                if eye_y_position > reference_threshold + CONF['settings']['eye_tolerance_threshold']:
                    trigger_alert = True
                    alert_msg = "SYSTEM PROTECTED:\nPLEASE RESUME ATTENTION"
                    
                    if ts_distraction_start is None: 
                        ts_distraction_start = now
                    # Corregido: antes usabas 'distraccion' con C
                    elif now - ts_distraction_start > CONF['settings']['distraction_alert_time'] and not distraction_state:
                        distraction_state = True
                else:
                    if distraction_state:
                        # Corregido: antes usabas 'distraccion' con C
                        dist_duration = now - ts_distraction_start
                        logging.warning(f"EVENT: Attention loss registered. Duration: {dist_duration:.2f}s")
                    ts_distraction_start = None
                    distraction_state = False

            if trigger_alert:
                ui_text.set(alert_msg)
                root.deiconify()
                root.update()
            else:
                root.withdraw()
                root.update()
            
            cv2.imshow('Status Monitor', cv2.resize(cv2.flip(frame, 1), (320, 240)))
            if cv2.waitKey(5) & 0xFF == 27: break

    video_capture.release()
    cv2.destroyAllWindows()
    generate_verification_hash() 
    root.destroy()

if __name__ == "__main__":
    try:
        run_sentinel()
    except Exception as e:
        print(f"❌ Critical Error: {e}")
        logging.error(f"CRITICAL ERROR: Main engine failure: {e}")