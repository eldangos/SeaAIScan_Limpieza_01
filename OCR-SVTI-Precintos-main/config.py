"""Constantes y utilidades compartidas por el prototipo SeaAIScan.

No almacenar aquí contraseñas ni datos de acceso a la cámara.
La configuración RTSP se aplica explícitamente desde main.py.
"""

import os
from pathlib import Path


# Configuración del video: conserva valores predeterminados y ajustes externos.
def configurar_entorno_rtsp() -> None:
    """Prefiere RTSP por TCP, salvo que el entorno ya defina otra opción."""
    os.environ.setdefault("OPENCV_FFMPEG_CAPTURE_OPTIONS", "rtsp_transport;tcp")


# Retícula de referencia para visualización y recorte central.
COLOR_RETICULA = (0, 180, 80)
GROSOR_RETICULA = 2
ANCHO_RETICULA_PCT = 0.30
ALTO_RETICULA_PCT = 0.20

# Directorios locales de este prototipo.
RAIZ_PROYECTO = Path(__file__).resolve().parent
CARPETA_CAPTURAS = RAIZ_PROYECTO / "capturas_precintos"

# Valores heredados del prototipo Hikvision.
CANAL_RTSP_DEFAULT = "101"
CANAL_RTSP_MEDIO = "102"
PUERTO_RTSP = 554
VEL_FOCO = 5


def asegurar_carpeta_capturas() -> Path:
    """Crea la carpeta de capturas si aún no existe."""
    CARPETA_CAPTURAS.mkdir(parents=True, exist_ok=True)
    return CARPETA_CAPTURAS


def recorte_reticula(frame):
    """Recorta la zona central equivalente a la retícula de la UI."""
    alto, ancho = frame.shape[:2]
    rw = max(1, int(ancho * ANCHO_RETICULA_PCT))
    rh = max(1, int(alto * ALTO_RETICULA_PCT))
    x1 = max(0, ancho // 2 - rw // 2)
    y1 = max(0, alto // 2 - rh // 2)
    x2 = min(ancho, x1 + rw)
    y2 = min(alto, y1 + rh)
    return frame[y1:y2, x1:x2].copy()
