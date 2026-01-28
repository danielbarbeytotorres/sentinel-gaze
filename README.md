# Sentinel-Gaze 🛡️

**Sentinel-Gaze** is an advanced AI-powered endpoint security suite designed to mitigate risks associated with **Insider Threats**, **Shoulder Surfing**, and unauthorized physical access to critical workstations.

By leveraging **Computer Vision** (MediaPipe) and real-time biometric monitoring, the system enforces a **Zero-Trust** environment, ensuring that data is only visible to the authorized operator.

## 🚀 Key Features

* **Zero-Trust Presence Monitoring**: Automatic workstation locking protocol initiated upon operator absence.
* **Anti-Shoulder Surfing**: Real-time detection of multiple subjects within the perimeter, triggering automated alerts and visual evidence capture.
* **Privacy Overlay & Data Obfuscation**: Immediate full-screen black-out (blur) to protect sensitive information when a distraction or third party is detected.
* **Forensic Integrity & Chain of Custody**: Generation of a **SHA-256 Checksum** at session termination to guarantee that log files have not been tampered with.

## 🛠️ Architecture

The system is built on a modular architecture:
1.  **Vision Engine**: Based on MediaPipe Face Mesh for sub-millimeter facial landmark tracking.
2.  **Response Controller**: Manages OS-level commands (Workstation Lock) and GUI alerts.
3.  **Auditor**: Handles persistent logging of security events and integrity verification.

## 📋 Installation & Setup

### Prerequisites
* Python 3.8 or higher.
* Active webcam.

### Deployment
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/tu_usuario/sentinel-gaze.git](https://github.com/tu_usuario/sentinel-gaze.git)
   cd sentinel-gaze
   ```
Aquí tienes el README.md redactado con un nivel técnico de Ingeniero de Ciberseguridad. He optado por el inglés como idioma principal para que el repositorio gane visibilidad internacional, pero con una estructura clara que cualquiera (incluido Adrián) podrá seguir sin problemas.

Copia este contenido en tu archivo README.md:

Markdown
# Sentinel-Gaze v2.0 🛡️

**Sentinel-Gaze** is an advanced AI-powered endpoint security suite designed to mitigate risks associated with **Insider Threats**, **Shoulder Surfing**, and unauthorized physical access to critical workstations.

By leveraging **Computer Vision** (MediaPipe) and real-time biometric monitoring, the system enforces a **Zero-Trust** environment, ensuring that data is only visible to the authorized operator.

## 🚀 Key Features

* **Zero-Trust Presence Monitoring**: Automatic workstation locking protocol initiated upon operator absence.
* **Anti-Shoulder Surfing**: Real-time detection of multiple subjects within the perimeter, triggering automated alerts and visual evidence capture.
* **Privacy Overlay & Data Obfuscation**: Immediate full-screen black-out (blur) to protect sensitive information when a distraction or third party is detected.
* **Forensic Integrity & Chain of Custody**: Generation of a **SHA-256 Checksum** at session termination to guarantee that log files have not been tampered with.

## 🛠️ Architecture

The system is built on a modular architecture:
1.  **Vision Engine**: Based on MediaPipe Face Mesh for sub-millimeter facial landmark tracking.
2.  **Response Controller**: Manages OS-level commands (Workstation Lock) and GUI alerts.
3.  **Auditor**: Handles persistent logging of security events and integrity verification.



## 📋 Installation & Setup

### Prerequisites
* Python 3.8 or higher.
* Active webcam.

### Deployment
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/tu_usuario/sentinel-gaze.git](https://github.com/tu_usuario/sentinel-gaze.git)
   cd sentinel-gaze
   
2. **Install dependencies:**
  ```bash
    pip install -r requirements.txt
  ```

3. **Configuration:**
Edit the config.json file to adjust security thresholds:
- timeout_bloqueo: Seconds before locking the station.
- bloqueo_real_activo: Set to true to enable OS-level locking.

4. **Execution:**
  ```bash
    python sentinel_gaze.py
  ```
