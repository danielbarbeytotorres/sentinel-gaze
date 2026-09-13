# Sentinel-Gaze 🛡️ | Endpoint Biometric Monitoring
 
**Sentinel-Gaze** is an advanced AI-powered security suite designed to mitigate critical risks such as **Insider Threats**, **Shoulder Surfing**, and unauthorized physical access to sensitive workstations.
 
Through the use of **Computer Vision** (MediaPipe) and real-time biometric monitoring, the system enforces a **Zero-Trust** environment, ensuring that data is only visible to the authorized operator.
 
## 🚀 Key Features
 
* **Zero-Trust Presence Monitoring**: Automatic workstation lockdown protocol after detecting operator absence.
* **Anti-Shoulder Surfing**: Real-time detection of multiple subjects in the perimeter, activating alerts and visual evidence capture.
* **Privacy Overlay & Data Obfuscation**: Immediate screen blackout upon detecting distractions or third parties, protecting sensitive information.
* **Forensic Integrity**: Generation of a **SHA-256** checksum at session end to guarantee log integrity and prevent tampering.
## 🛠️ System Architecture
 
The system is based on a modular architecture:
1.  **Vision Engine**: Based on MediaPipe Face Mesh for sub-millimetric facial point tracking.
2.  **Response Controller**: OS-level command management (LockWorkStation) and graphical interface alerts (Tkinter).
3.  **Auditor**: Persistent logging of security events and cryptographic integrity verification.
## 📋 Installation and Deployment
 
### Prerequisites
* **Python 3.11** (Critical to ensure compatibility with MediaPipe and Numpy precompiled binaries).
* Active webcam.
* Operating System: Windows (for `user32.dll` lock functionality).
### Environment Setup
1.  **Clone the repository:**

```bash
    git clone https://github.com/danielbarbeytotorres/sentinel-gaze.git
    cd sentinel-gaze
```
 
2.  **Configure virtual environment (VENV):**
    To avoid compilation conflicts with base libraries, you must use the correct Python version.
    
    If Python 3.11 is your default system version, run:
```bash
    python -m venv venv
 
    **⚠️ TROUBLESHOOTING (Windows Users):** If you have a more recent version installed (such as Python 3.13) as default, the above command will generate errors when installing `numpy`. In that case, force the system to use version 3.11 via the Windows Launcher:

    py -3.11 -m venv venv
```
 
3.  **Activate the environment:**
   
```powershell
    .\venv\Scripts\activate
```
 
4.  **Install certified dependencies:**


```bash
    pip install -r requirements.txt
    
    *Note: The project is pinned to `numpy==1.26.4` and `mediapipe==0.10.11` for stability reasons.*
```
    
 
5.  **Policy Configuration:**
    Edit `config.json` to adjust security thresholds:
    * `lock_timeout`: Seconds before locking the session due to absence.
    * `real_lock_enabled`: `true` to activate real operating system lock.
6.  **Execution:**

```bash
    python sentinel-gaze.py
```
 
## 🔐 Auditing and Logs
All events are logged in `security_events.log`. When closing the program (by pressing the `ESC` key), a **SHA-256** digital signature will be automatically generated and displayed in the console to facilitate forensic auditing.
 
<img width="1597" height="1085" alt="1" src="https://github.com/user-attachments/assets/70767e6e-289d-42b0-a71f-5702ea01b687" />
Developed by [Daniel Barbeyto](https://github.com/danielbarbeytotorres)
