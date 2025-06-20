# procesar_imagen.py - IA de captioning (BLIP) y generación de keywords

from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch

def cargar_modelo_blip():
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return processor, model

def describir_imagen_blip(ruta_imagen, processor, model):
    image = Image.open(ruta_imagen).convert('RGB')
    inputs = processor(image, return_tensors="pt")
    with torch.no_grad():
        out = model.generate(**inputs)
        descripcion = processor.decode(out[0], skip_special_tokens=True)
    return descripcion

def generar_keywords(descripcion):
    if not descripcion:
        return []
    stopwords = ['a', 'the', 'of', 'on', 'in', 'with', 'and', 'to', 'for', 'by', 'at', 'an', 'from', 'as', 'is']
    palabras = descripcion.lower().replace('.', '').replace(',', '').split()
    keywords = [w for w in palabras if w not in stopwords and len(w) > 2]
    keywords = list(dict.fromkeys(keywords))
    return keywords[:25]

