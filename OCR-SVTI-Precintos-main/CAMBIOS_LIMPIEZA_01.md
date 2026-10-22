# SeaAIScan — Registro de limpieza 01

## Alcance

Primera limpieza **limitada al arranque, configuración, dependencias y guía de instalación**.
No se ha reestructurado `ui/`, `modulos/`, la lógica OCR, RTSP ni el flujo con Excel.
La aplicación sigue funcionando como **prototipo antiguo**, no como entrega completa de SVTI.

## Cambios realizados

- `main.py`: mantiene la creación de `QApplication`, la ventana y los nombres de
  QSettings; devuelve el código de salida de Qt; configura RTSP antes de importar la UI.
- `config.py`: agrupa constantes y elimina la configuración RTSP como efecto secundario
  de la importación. Se llama explícitamente a `configurar_entorno_rtsp()`.
  Se conservan los nombres y valores de constantes, la ruta de capturas y el recorte.
- `requirements.txt`: convertido de UTF-16 a UTF-8; corregido `dotenv` por
  `python-dotenv`; añadidos `requests` y `PySide6` detectados en importaciones.
  Los cuatro pines existentes (`paddlepaddle`, `paddleocr`, `numpy`, `opencv-python`)
  permanecen sin cambios. El resto no se ha fijado todavía a versiones validadas.
- `Step_by_step.md`: instalación desde `requirements.txt`, comandos PowerShell/CMD,
  instrucciones de ejecución, comprobaciones y advertencias de seguridad.
- `tests/test_inicio_config.py`: pruebas aisladas (sin cámara ni Qt/Paddle reales).

## Comprobaciones realizadas en el entorno de revisión

- Comparación del contenido: los módulos `ui/` y `modulos/` se conservaron intactos.
- Análisis sintáctico de todos los archivos Python (AST/compile) sin importarlos.
- Pruebas unitarias básicas de entorno, ruta de capturas, recorte y arranque simulado.

## Pendiente y fuera de alcance de esta fase

- Pruebas **reales** en Windows con cámara Hikvision / RTSP y OCR.
- Certificar dependencias instalables en un equipo limpio; fijar versiones definitivas.
- Separar la UI del backend, eliminar cruce Excel, leer contenedor + precintos,
  generar JSON y persistir eventos, integración API, cola e idempotencia.
- Revisar manejo de secretos en QSettings y licencias de PySide6.

**Versión anterior:** `OCR-SVTI-Precintos-main.zip` (respaldo; no se modificó).
**Versión de esta etapa:** `SeaAIScan_Limpieza_01.zip`.
