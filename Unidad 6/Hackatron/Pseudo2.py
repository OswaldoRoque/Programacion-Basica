def contar_elementos(texto):
    vocales = "aeiouAEIOU"
    consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    numeros = "0123456789"
    
    contador_vocales = sum(1 for char in texto if char in vocales)
    contador_consonantes = sum(1 for char in texto if char in consonantes)
    contador_numeros = sum(1 for char in texto if char in numeros)
    contador_palabras = len(texto) - (contador_vocales + contador_consonantes + contador_numeros)
    
    return contador_vocales, contador_consonantes, contador_numeros, contador_palabras

texto = input("Ingresa un texto: ")
vocales, consonantes, numeros, palabras = contar_elementos(texto)

print(f"Vocales: {vocales}")
print(f"Consonantes: {consonantes}")
print(f"Números: {numeros}")
print(f"Palabras: {palabras}")