# Examen unidad 3

# Importamos las librerías necesarias
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

if __name__ == "__main__":        
# Diccionarios iniciales
    carros = {}

# Función para mostrar el menú
def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Agregar un carro")
    print("2. Eliminar un carro")
    print("3. Mostrar carros en mi posecion")
    print("4. Salir")

# Inicia el programa en bucle
while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
            # Lista de palabras
        palabras = ["Lamborghini","Bugatti","Ferrari","Nissan","Toyota", "Ford"]
        print("Un carro recomendado es")
        # sirve para generar una palabra aleatoria y decirte cual carro te recomienda comprar
        palabra = random.choice(palabras)
        print( random.choice(palabras))
        # Agregar un carro de lujo
        nuevo_carro = input("Ingresa la marca del carro: ")
        precio = int(input(f"Ingrese el precio de {nuevo_carro} (en MXM): "))
        carros[nuevo_carro] = precio
        print(f"{nuevo_carro} agregado con éxito al diccionario de carros.")

    elif opcion == "2":
        # Eliminar un carro 
        print("Carros disponibles:")
        for carro in carros.keys():
            print(f"- {carro}")
        carro_eliminar = input("¿Qué carro deseas eliminar?: ")
        if carro_eliminar in carros:
            del carros[carro_eliminar]
            print(f"{carro_eliminar} eliminado con éxito del diccionario.")
        else:
            print("El carro ingresado no existe en la lista.")

    elif opcion == "3":
        # Muestra una lista de los carros que tienes
        print("\nMis carros:")
        for carro, precio in carros.items():
            print(f"{carro}: ${precio} USD")

    elif opcion == "4":
        # Salir del programa
        print("Saliendo de la compra de carros... ¡Hasta luego!")
        break

    else:
        # Opción no válida
        print("No existe esa funcion.")

    # Uso de librerías adicionales
    time.sleep(3)  # Pausa breve

    carros = "carros.csv"

    # Guardar los diccionarios en un archivo CSV
guardar_diccionarios_en_csv(carros)

    # Leer los diccionarios desde el archivo CSV
carros_leidos = leer_diccionarios_de_csv(carros)
print("Datos leídos del archivo CSV:")
print(carros_leidos)