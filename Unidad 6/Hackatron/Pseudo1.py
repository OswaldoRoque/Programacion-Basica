def contar_palabras(texto):
    palabras = texto.split()
    return len(palabras)

texto = input("Ingresa un texto: ")
cantidad_palabras = contar_palabras(texto)
print(f"El texto contiene {cantidad_palabras} palabras.")