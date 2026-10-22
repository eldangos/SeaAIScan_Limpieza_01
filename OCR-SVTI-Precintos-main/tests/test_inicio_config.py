"""Pruebas de la limpieza 01; no dependen de cámara ni del motor OCR."""

import os
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest.mock import patch

import config
import main


class FrameFalso:
    def __init__(self, alto, ancho):
        self.shape = (alto, ancho, 3)
        self.recorte = None

    def __getitem__(self, indices):
        self.recorte = indices
        return self

    def copy(self):
        return self


class TestConfiguracion(unittest.TestCase):
    def test_rtsp_tcp_si_no_hay_preferencia(self):
        with patch.dict(os.environ, {}, clear=True):
            config.configurar_entorno_rtsp()
            self.assertEqual(os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"], "rtsp_transport;tcp")

    def test_rtsp_no_pisa_preferencia_existente(self):
        with patch.dict(os.environ, {"OPENCV_FFMPEG_CAPTURE_OPTIONS": "rtsp_transport;udp"}, clear=True):
            config.configurar_entorno_rtsp()
            self.assertEqual(os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"], "rtsp_transport;udp")

    def test_recorte_coincide_con_reticula(self):
        frame = FrameFalso(100, 200)
        self.assertIs(config.recorte_reticula(frame), frame)
        self.assertEqual(frame.recorte, (slice(40, 60), slice(70, 130)))

    def test_carpeta_se_crea_solo_al_solicitarla(self):
        with tempfile.TemporaryDirectory() as temp:
            carpeta = Path(temp) / "capturas"
            with patch.object(config, "CARPETA_CAPTURAS", carpeta):
                self.assertFalse(carpeta.exists())
                self.assertEqual(config.asegurar_carpeta_capturas(), carpeta)
                self.assertTrue(carpeta.is_dir())

    def test_arranque_simulado_sin_importar_qt_real(self):
        registros = []

        class AppFalsa:
            def __init__(self, argv):
                registros.append("init")

            def setOrganizationName(self, valor):
                registros.append(("org", valor))

            def setApplicationName(self, valor):
                registros.append(("app", valor))

            def exec(self):
                registros.append("exec")
                return 0

        class VentanaFalsa:
            def show(self):
                registros.append("show")

        paquete = types.ModuleType("PySide6")
        paquete.__path__ = []
        widgets = types.ModuleType("PySide6.QtWidgets")
        widgets.QApplication = AppFalsa
        ui_modulo = types.ModuleType("ui.main_window")
        ui_modulo.MainWindow = VentanaFalsa
        with patch.dict(sys.modules, {
            "PySide6": paquete,
            "PySide6.QtWidgets": widgets,
            "ui.main_window": ui_modulo,
        }):
            with patch.object(main, "configurar_entorno_rtsp", side_effect=lambda: registros.append("rtsp")):
                self.assertEqual(main.main(), 0)
        self.assertEqual(registros, [
            "rtsp", "init", ("org", "ACCELERA"),
            ("app", "SVTI-Precintos"), "show", "exec",
        ])


if __name__ == "__main__":
    unittest.main()
