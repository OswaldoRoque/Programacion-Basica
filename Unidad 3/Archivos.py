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

# Ejemplo de uso
if __name__ == "__main__":
    datos = [
        {"Nombre": "Juan", "Edad": 25, "Ciudad": "Madrid"},
        {"Nombre": "Ana", "Edad": 30, "Ciudad": "Barcelona"},
        {"Nombre": "Luis", "Edad": 35, "Ciudad": "Valencia"}
    ]

    archivo = "datos.csv"

    # Guardar los diccionarios en un archivo CSV
    guardar_diccionarios_en_csv(archivo, datos)

    # Leer los diccionarios desde el archivo CSV
    datos_leidos = leer_diccionarios_de_csv(archivo)
    print("Datos leídos del archivo CSV:")
    print(datos_leidos)