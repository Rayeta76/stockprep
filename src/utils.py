# utils.py - Utilidades de limpieza, creación de carpetas, guardado y renombrado

import os
import re
import json

def limpiar_nombre_archivo(nombre):
    nombre_limpio = re.sub(r'[\\/*?:"<>|]', '', nombre).strip()
    nombre_limpio = nombre_limpio.replace(' ', '_')
    return nombre_limpio[:60] if nombre_limpio else "Untitled"

def crear_directorios(lista_de_rutas):
    for ruta in lista_de_rutas:
        os.makedirs(ruta, exist_ok=True)

def guardar_log(ruta, info):
    with open(ruta, 'w', encoding='utf-8') as f:
        f.write(info)

def guardar_json(ruta, datos):
    with open(ruta, 'w', encoding='utf-8') as f:
        json.dump(datos, f, ensure_ascii=False, indent=4)

def guardar_xml(ruta, datos):
    with open(ruta, 'w', encoding='utf-8') as f:
        f.write(f"<imagen>\n")
        f.write(f"  <filename>{datos['filename']}</filename>\n")
        f.write(f"  <title>{datos['title']}</title>\n")
        f.write(f"  <description>{datos['description']}</description>\n")
        f.write(f"  <keywords>{datos['keywords']}</keywords>\n")
        f.write(f"</imagen>\n")

def renombrar_imagen(ruta_imagen, nombre_base, carpeta_destino):
    ext = os.path.splitext(ruta_imagen)[1].lower()
    nuevo_nombre = f"{nombre_base}{ext}"
    ruta_nueva = os.path.join(carpeta_destino, nuevo_nombre)
    contador = 1
    while os.path.exists(ruta_nueva):
        nuevo_nombre = f"{nombre_base}_{contador}{ext}"
        ruta_nueva = os.path.join(carpeta_destino, nuevo_nombre)
        contador += 1
    if os.path.abspath(ruta_imagen) != os.path.abspath(ruta_nueva):
        os.rename(ruta_imagen, ruta_nueva)
    return nuevo_nombre

