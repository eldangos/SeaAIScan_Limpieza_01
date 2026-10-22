"""Punto de entrada de la aplicación de escritorio SeaAIScan (prototipo)."""

import sys

from config import configurar_entorno_rtsp


def main() -> int:
    """Prepara RTSP, inicia la interfaz y devuelve el código de salida de Qt."""
    # Configurar antes de importar módulos que abren flujos con OpenCV.
    configurar_entorno_rtsp()

    from PySide6.QtWidgets import QApplication
    from ui.main_window import MainWindow

    app = QApplication(sys.argv)
    # Conservar los identificadores para no perder QSettings existentes.
    app.setOrganizationName("ACCELERA")
    app.setApplicationName("SVTI-Precintos")

    ventana = MainWindow()
    ventana.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
