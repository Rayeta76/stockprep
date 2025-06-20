import os
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk

try:
    from .core_logic import ejecutar_procesamiento_stockprep
except ImportError:
    from core_logic import ejecutar_procesamiento_stockprep  # type: ignore


class StockPrepAppGUI:
    """Interfaz gráfica principal de StockPrep."""

    def __init__(self, master: tk.Tk) -> None:
        self.master = master
        self.master.title("StockPrep – Procesador de imágenes (simulado)")
        self.master.geometry("800x650")

        # ---------- Selección de carpeta ----------
        self.base_dir_var = tk.StringVar(master)
        proyecto = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        self.base_dir_var.set(proyecto)

        dir_frame = ttk.Frame(master, padding=10)
        dir_frame.pack(fill=tk.X)

        ttk.Button(
            dir_frame,
            text="Seleccionar carpeta del proyecto",
            command=self.select_project_directory,
        ).pack(side=tk.LEFT, padx=(0, 10))

        ttk.Label(dir_frame, text="Directorio actual:").pack(side=tk.LEFT)
        ttk.Label(dir_frame, textvariable=self.base_dir_var, relief="sunken").pack(
            side=tk.LEFT, fill=tk.X, expand=True
        )

        # ---------- Botón principal ----------
        self.process_button = ttk.Button(
            master,
            text="Iniciar procesamiento",
            command=self.start_processing_thread,
            style="Accent.TButton",
        )
        self.process_button.pack(pady=15)

        # ---------- Área de log ----------
        ttk.Label(master, text="Registro de actividad:").pack(anchor=tk.W, padx=10)
        self.log = scrolledtext.ScrolledText(master, height=20, state=tk.DISABLED)
        self.log.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))

    # ----- callbacks GUI -----
    def gui_status_update(self, msg: str) -> None:
        self.master.after(0, lambda: self._append(msg))

    def _append(self, msg: str) -> None:
        self.log.config(state=tk.NORMAL)
        self.log.insert(tk.END, msg + "\n")
        self.log.see(tk.END)
        self.log.config(state=tk.DISABLED)

    def select_project_directory(self) -> None:
        nuevo = filedialog.askdirectory(initialdir=self.base_dir_var.get())
        if nuevo:
            self.base_dir_var.set(nuevo)

    def start_processing_thread(self) -> None:
        self.process_button.config(state=tk.DISABLED)
        th = threading.Thread(
            target=self.run_processing, args=(self.base_dir_var.get(),), daemon=True
        )
        th.start()

    def run_processing(self, carpeta: str) -> None:
        try:
            ejecutar_procesamiento_stockprep(carpeta, self.gui_status_update)
        finally:
            self.master.after(0, lambda: self.process_button.config(state=tk.NORMAL))


if __name__ == "__main__":
    tk_root = tk.Tk()
    app = StockPrepAppGUI(tk_root)
    tk_root.mainloop()
