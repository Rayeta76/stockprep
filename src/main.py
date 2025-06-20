import sys
import tkinter as tk
import os

try:
    from .gui import StockPrepAppGUI
    from .core_logic import ejecutar_procesamiento_stockprep
except ImportError:
    from gui import StockPrepAppGUI  # type: ignore
    from core_logic import ejecutar_procesamiento_stockprep  # type: ignore


def run_cli_mode() -> None:
    print("Modo CLI aún no implementado por completo.")
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    print(f"Usando carpeta base: {base_dir}")
    ejecutar_procesamiento_stockprep(base_dir, print)


def run_gui_mode() -> None:
    root = tk.Tk()
    StockPrepAppGUI(root)
    root.mainloop()


if __name__ == "__main__":
    if "--cli" in sys.argv:
        run_cli_mode()
    else:
        run_gui_mode()


