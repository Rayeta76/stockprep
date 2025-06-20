# main.py - Lanzador del procesamiento principal StockPrep (solo CSV y ficheros externos)

from core_logic import procesar_lote_imagenes

if __name__ == "__main__":
    def log(msg):
        print(msg)
    import os
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    procesar_lote_imagenes(log, base_dir, "imagenes")


