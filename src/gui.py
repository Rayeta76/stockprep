# gui.py - Interfaz gráfica básica para StockPrep

import tkinter as tk
from core_logic import procesar_lote_imagenes
import os

class StockPrepGUI:
    def __init__(self, master):
        self.master = master
        master.title("StockPrep - Automatización de Metadatos")
        self.master.geometry("600x250")
        self.directorio_actual = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        self.status_text = tk.StringVar()
        self.status_text.set("Listo para procesar imágenes.")

        self.label = tk.Label(master, text="StockPrep: Automatización de metadatos para imágenes de stock")
        self.label.pack(pady=10)

        self.procesar_btn = tk.Button(master, text="Procesar imágenes", command=self.iniciar_procesamiento)
        self.procesar_btn.pack(pady=10)

        self.status = tk.Label(master, textvariable=self.status_text, fg="blue")
        self.status.pack(pady=10)

    def log(self, mensaje):
        self.status_text.set(mensaje)
        self.master.update()

    def iniciar_procesamiento(self):
        self.log("Procesando imágenes, por favor espera...")
        procesar_lote_imagenes(self.log, self.directorio_actual, "imagenes")
        self.log("Proceso finalizado.")

if __name__ == "__main__":
    root = tk.Tk()
    app = StockPrepGUI(root)
    root.mainloop()
