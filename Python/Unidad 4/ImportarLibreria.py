
import time
import random
import csv 

def guardar_diccionarios_en_csv(nombre_archivo, lista_diccionarios):
    """Guarda una lista de diccionarios en un archivo CSV."""
    if not lista_diccionarios:
        print("La lista de diccionarios está vacía.")
        return

    # Obtener las claves del primer diccionario como encabezados
    encabezados = lista_diccionarios[0].keys()

    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo_csv:
        escritor = csv.DictWriter(archivo_csv, fieldnames=encabezados)
        escritor.writeheader()
        escritor.writerows(lista_diccionarios)

    print(f"Datos guardados en {nombre_archivo} exitosamente.")

def leer_diccionarios_de_csv(nombre_archivo):
    """Lee un archivo CSV y lo convierte en una lista de diccionarios."""
    try:
        with open(nombre_archivo, mode='r', encoding='utf-8') as archivo_csv:
            lector = csv.DictReader(archivo_csv)
            return [fila for fila in lector]
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe.")
        return []
    
archivo = "carros.csv"

carros = [{"Nissan": 80000,"Bugatti": 90000}]

guardar_diccionarios_en_csv(archivo, carros)