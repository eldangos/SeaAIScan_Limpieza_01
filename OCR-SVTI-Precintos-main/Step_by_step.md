# SeaAIScan — instalación del prototipo (Windows)

Esta guía corresponde a la **limpieza 01**. Todavía ejecuta la aplicación antigua con UI,
comparación con Excel y OCR de precintos; no es aún el backend/JSON exigido por SVTI.

## 1. Preparar Python

Usar **Python 3.10** y abrir una terminal en la carpeta que contiene `main.py`.

```powershell
py -3.10 -m venv venv
```

Activación en **PowerShell**:

```powershell
.\venv\Scripts\Activate.ps1
```

En **CMD** se utiliza `venv\Scripts\activate.bat`.
Si PowerShell bloquea la activación, se puede ejecutar sin activar el entorno
usando `venv\Scripts\python.exe` en lugar de `python` en los comandos siguientes.
No es necesario cambiar las políticas de ejecución de Windows para ello.

## 2. Instalar dependencias

```powershell
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
```

El archivo `requirements.txt` está en UTF-8 y declara las librerías importadas
por el proyecto. Se conservaron las versiones antiguas de Paddle y OpenCV
para no introducir una migración en esta limpieza. Otras librerías siguen sin
fijar versión: **la instalación todavía debe verificarse en una máquina limpia**.

## 3. Ejecutar comprobaciones y abrir la aplicación

```powershell
python -m unittest discover -s tests -v
python main.py
```

Las pruebas incluidas verifican configuración, recorte y arranque simulado.
**No prueban conexión a la cámara, calidad del OCR ni funcionamiento de Qt real.**

## 4. Configuración y seguridad

- Los parámetros RTSP predeterminados se ajustan en `config.py` y se aplican en `main.py`.
- El prototipo admite algunas variables de entorno: `CAM_IP`, `CAM_USER`, `CAM_PASS` y `CAM_CHANNEL`.
- **No subir archivos `.env` con contraseñas a un repositorio ni pegarlas en capturas/logs.**
- La UI heredada también usa QSettings para guardar credenciales; queda pendiente
  su revisión de seguridad en una siguiente etapa.

## 5. Si hay errores

Registrar versión de Python (`python --version`), sistema operativo y mensaje de
error completo **sin incluir contraseñas ni URLs RTSP con credenciales**.
No instalar o actualizar versiones al azar durante el piloto.
