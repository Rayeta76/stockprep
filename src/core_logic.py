# core_logic.py - Núcleo de procesamiento de imágenes y generación de metadatos externos

import os
import csv
from procesar_imagen import cargar_modelo_blip, describir_imagen_blip, generar_keywords
from utils import limpiar_nombre_archivo, crear_directorios, guardar_json, guardar_xml, guardar_log, renombrar_imagen

def procesar_lote_imagenes(status_callback, base_dir, carpeta_relativa_imagenes):
    carpetas = {
        'imagenes': os.path.join(base_dir, carpeta_relativa_imagenes),
        'logs': os.path.join(base_dir, 'logs'),
        'metadatos': os.path.join(base_dir, 'metadatos'),
        'xml': os.path.join(base_dir, 'xml'),
        'resultados': os.path.join(base_dir, 'resultados')
    }
    crear_directorios(carpetas.values())
    imagenes = [f for f in os.listdir(carpetas['imagenes']) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    if not imagenes:
        status_callback("No se encontraron imágenes JPG/JPEG/PNG en la carpeta.")
        return

    processor, model = cargar_modelo_blip()
    csv_resultados = []

    for imagen in imagenes:
        ruta_imagen = os.path.join(carpetas['imagenes'], imagen)
        descripcion = describir_imagen_blip(ruta_imagen, processor, model).strip()
        titulo = descripcion.split('.')[0][:70] if descripcion else "Untitled"
        titulo = limpiar_nombre_archivo(titulo)

        nombre_sin_ext = os.path.splitext(titulo)[0]
        nuevo_nombre = renombrar_imagen(ruta_imagen, nombre_sin_ext, carpetas['imagenes'])
        ruta_nueva_imagen = os.path.join(carpetas['imagenes'], nuevo_nombre)

        keywords = generar_keywords(descripcion)
        keywords_str = ', '.join(keywords)

        datos = {
            'filename': nuevo_nombre,
            'title': titulo,
            'description': descripcion,
            'keywords': keywords_str
        }

        guardar_log(os.path.join(carpetas['logs'], titulo + '.log'),
                    f"Imagen: {nuevo_nombre}\nTitulo: {titulo}\nDescripcion: {descripcion}\nKeywords: {keywords_str}")
        guardar_json(os.path.join(carpetas['metadatos'], titulo + '.json'), datos)
        guardar_xml(os.path.join(carpetas['xml'], titulo + '.xml'), datos)

        csv_resultados.append([nuevo_nombre, titulo, descripcion, keywords_str])
        status_callback(f"Procesada: {nuevo_nombre}")

    ruta_csv = os.path.join(carpetas['resultados'], 'imagenes_stock.csv')
    with open(ruta_csv, 'w', newline='', encoding='utf-8') as fcsv:
        writer = csv.writer(fcsv)
        writer.writerow(['filename', 'title', 'description', 'keywords'])
        writer.writerows(csv_resultados)
    status_callback("\n¡PROCESO FINALIZADO! CSV global y archivos individuales generados correctamente.")


