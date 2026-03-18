# Sentinel-Gaze 🛡️ | Endpoint Biometric Monitoring

**Sentinel-Gaze** es una suite de seguridad avanzada basada en IA diseñada para mitigar riesgos críticos como **Insider Threats**, **Shoulder Surfing** y el acceso físico no autorizado a estaciones de trabajo sensibles.

Mediante el uso de **Visión Artificial** (MediaPipe) y monitorización biométrica en tiempo real, el sistema impone un entorno de **Zero-Trust**, asegurando que los datos solo sean visibles para el operador autorizado.

## 🚀 Funcionalidades Clave

* **Zero-Trust Presence Monitoring**: Protocolo de bloqueo automático de la estación de trabajo tras detectar la ausencia del operador.
* **Anti-Shoulder Surfing**: Detección en tiempo real de múltiples sujetos en el perímetro, activando alertas y captura de evidencias visuales.
* **Privacy Overlay & Data Obfuscation**: Oscurecimiento inmediato de la pantalla (black-out) al detectar distracciones o terceros, protegiendo información sensible.
* **Forensic Integrity**: Generación de un checksum **SHA-256** al finalizar la sesión para garantizar la integridad de los logs y evitar manipulaciones.

## 🛠️ Arquitectura del Sistema

El sistema se basa en una arquitectura modular:
1.  **Vision Engine**: Basado en MediaPipe Face Mesh para el rastreo submilimétrico de puntos faciales.
2.  **Response Controller**: Gestión de comandos a nivel de SO (LockWorkStation) y alertas de interfaz gráfica (Tkinter).
3.  **Auditor**: Registro persistente de eventos de seguridad y verificación de integridad criptográfica.

## 📋 Instalación y Despliegue

### Requisitos Previos
* **Python 3.11** (Crítico para asegurar la compatibilidad de los binarios precompilados de MediaPipe y Numpy).
* Webcam activa.
* Sistema Operativo: Windows (para la funcionalidad de bloqueo `user32.dll`).

### Despliegue del Entorno
1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/danielbarbeytotorres/sentinel-gaze.git](https://github.com/danielbarbeytotorres/sentinel-gaze.git)
    cd sentinel-gaze
    ```

2.  **Configurar entorno virtual (VENV):**
    Para evitar conflictos de compilación con las librerías base, debes usar la versión correcta de Python. 
    
    Si Python 3.11 es tu versión por defecto en el sistema, ejecuta:
    ```bash
    python -m venv venv
    ```

    **⚠️ TROUBLESHOOTING (Usuarios de Windows):** Si tienes instalada una versión más reciente (como Python 3.13) como predeterminada, el comando anterior te generará errores al instalar `numpy`. En ese caso, fuerza al sistema a usar la versión 3.11 mediante el Launcher de Windows:
    ```bash
    py -3.11 -m venv venv
    ```

3.  **Activar el entorno:**
    ```powershell
    .\venv\Scripts\activate
    ```

4.  **Instalar dependencias certificadas:**
    ```bash
    pip install -r requirements.txt
    ```
    *Nota: El proyecto está fijado a `numpy==1.26.4` y `mediapipe==0.10.11` por motivos de estabilidad.*

5.  **Configuración de Políticas:**
    Edita `config.json` para ajustar los umbrales de seguridad:
    * `lock_timeout`: Segundos antes de bloquear la sesión por ausencia.
    * `real_lock_enabled`: `true` para activar el bloqueo real del sistema operativo.

6.  **Ejecución:**
    ```bash
    python sentinel-gaze.py
    ```

## 🔐 Auditoría y Logs
Todos los eventos se registran en `security_events.log`. Al cerrar el programa (presionando la tecla `ESC`), se generará automáticamente una firma digital SHA-256 mostrada en consola para facilitar la auditoría forense.

<img width="1597" height="1085" alt="1" src="https://github.com/user-attachments/assets/70767e6e-289d-42b0-a71f-5702ea01b687" />


Desarrollado por [Daniel Barbeyto](https://github.com/danielbarbeytotorres)
