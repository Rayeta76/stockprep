import os
from typing import Callable, List, Tuple

from . import utils
from . import procesar_imagen as proc_img

StatusCb = Callable[[str], None]


def _listar_imagenes(carpeta: str) -> List[str]:
    extensiones = (".jpg", ".jpeg", ".png")
    return [
        f for f in os.listdir(carpeta) if f.lower().endswith(extensiones)
    ]


def ejecutar_procesamiento_stockprep(base_dir: str, status_callback: StatusCb = print) -> None:
    status_callback("=" * 46)
    status_callback(f"Procesando proyecto StockPrep en: {base_dir}")
    status_callback("=" * 46)

    if not utils.crear_carpetas_estructura(base_dir, status_callback):
        status_callback("ERROR: estructura de carpetas incompleta. Abortando.")
        return

    carpetas = {c: os.path.join(base_dir, c) for c in utils.CARPETAS_PROYECTO}
    imagenes = _listar_imagenes(carpetas["imagenes"])
    if not imagenes:
        status_callback("No se encontraron imágenes para procesar.")
        return

    status_callback(f"Total imágenes encontradas: {len(imagenes)}")

    proc, modelo, _gpu = proc_img.cargar_modelo_ia(status_callback)
    resultados: List[Tuple[str, str, List[str]]] = []

    for idx, nombre in enumerate(imagenes, start=1):
        status_callback(f"\n[ {idx}/{len(imagenes)} ] -> {nombre}")

        ruta = os.path.join(carpetas["imagenes"], nombre)
        desc = proc_img.describir_imagen_ia(ruta, proc, modelo, status_callback)
        titulo_raw = desc.split(".")[0][:60]
        titulo = utils.limpiar_nombre_archivo(titulo_raw, status_callback)
        hashtags = proc_img.extraer_hashtags(desc, status_callback=status_callback)
        origen = utils.detectar_aplicacion_origen(nombre)
        status_callback(f"  Título simulado : {titulo}")
        status_callback(f"  Hashtags simul.  : {hashtags}")
        status_callback(f"  Origen detectado : {origen}")

        resultados.append((titulo, desc, hashtags))

    status_callback("\nProceso simulado completado.")


