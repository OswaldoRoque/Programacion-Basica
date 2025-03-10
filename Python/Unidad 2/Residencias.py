#En este programa se hara sobre si un alumno tiene 80 creditos o mas permita hacer el servicio social, pero si tiene 120 que permita hacer recidencias 

creditos = int(input("Ingrese el numero de creditos: "))
if creditos < 80:
    print("No puedes hacer servicio social.")
elif creditos >= 120:
    print("Puedes hacer las residencias.")
elif creditos < 120:
    print("Puedes hacer el servicio social.")
elif creditos >= 80:
    print("Puedes hacer el servicio social.")