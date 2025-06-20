# StockPrep 📷🔍  
Reconocimiento y anotación automática de imágenes con BLIP-2 / Florence-2 y PyTorch.

## Tabla de contenidos
- [Descripción](#descripción)
- [Características](#características)
- [Instalación](#instalación)
- [Uso rápido](#uso-rápido)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Hoja de ruta](#hoja-de-ruta)
- [Contribuir](#contribuir)
- [Licencia](#licencia)

## Descripción
StockPrep procesa lotes de imágenes para generar:
1. **Descripción textual** mediante modelos BLIP-2 o Florence-2  
2. **Palabras clave** derivadas de la descripción  
3. **Metadatos** en CSV, JSON y XML

El propósito es facilitar la catalogación de grandes colecciones fotográficas.

## Características
- 🖼️ Batch processing de carpetas completas  
- ⚙️ Selector de modelo (CPU / GPU)  
- 📄 Exporta resultados a `metadatos/` en **CSV, JSON, XML**  
- 🔑 Genera top-N keywords sin *stop-words* en español  
- 📝 Interfaz CLI y pequeña GUI con `tkinter`

## Instalación
> Requiere Python 3.11 y CUDA 12 (opcional, para GPU).

```bash
git clone https://github.com/Rayeta76/stockprep.git
cd stockprep
conda create -n stockprep python=3.11
conda activate stockprep
pip install -r requirements.txt

