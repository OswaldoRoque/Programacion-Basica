# Examen unidad 3
from Archivos import guardar_diccionarios_en_csv, leer_diccionarios_de_csv
# Importamos las librerías necesarias
import time
import random
archivo = "datos.csv"

# Diccionarios iniciales
carros = [
{"Nissan": 50000}
]
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
        carros(nuevo_carro) == precio
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
    time.sleep(3)  # Pausa breve}

guardar_diccionarios_en_csv(archivo, carros)

# Actividad hacer un programa llamado LeerconLibreria.py que importe la función leer_diccionarios_de_csv y lea el archivo datos.csv

leer_diccionarios_de_csv(archivo)

datos_leidos = leer_diccionarios_de_csv(archivo)
print("Datos leidos del archivo CSV:")
print(datos_leidos)