while True:
    print("\n Deseas hacer las compras")
    print("1. Si")
    print("2. No")

    opcion = input("Elige una opción: ")

    if opcion == "1":

        Lista = []
        print(" Lista de Compras ")
        producto1 = input("Agrega el primer producto: ")
    Lista.append(producto1)

    producto2 = input("Agrega el segundo producto: ")
    Lista.append(producto2)

    producto3 = input("Agrega el tercer producto: ")
    Lista.append(producto3)

    print("\n Tu lista de compras es:")
    for producto in Lista:
        print(f"- {producto}")

        print("\n ¡Lista creada!")