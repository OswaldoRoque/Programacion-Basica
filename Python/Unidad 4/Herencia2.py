# Herencia
 # Clase base o padre
class Celulares:
     def __init__(self, marca, creador):
         self.marca = marca
         self.creador = creador
 
     def presentarse(self):
         return f"Una marca de celular es {self.marca} y el dueño de esa marca es {self.creador}."
 
 # Clase derivada o hija
class Iphone(Celulares):
     def __init__(self, marca, creador, dueño):
         super().__init__(marca, creador)  # Llamada al constructor de la clase padre
         self.dueño = dueño
 
     def presentarse(self):
         # Sobrescribimos el método de la clase padre
         return f"Marca de celular: {self.marca} y su dueño es {self.creador} pero el dueño de todo eso es {self.dueño}."
 
 # Otra clase derivada
class Oppo(Celulares):
     def __init__(self, marca, creador, compra):
         super().__init__(marca, creador)
         self.compra = compra
 
     def presentarse(self):
         return f"Marca de celular: {self.marca} y lo fundo {self.creador} y es mas comprado por su {self.compra}."
 
 # Programa principal
if __name__ == "__main__":
     celulares = Celulares ("Motorola", "Joseph Galvin")
     iphone = Iphone("Iphone", "Appel Inc", "Tim Cook")
     oppo = Oppo ("Oppo", "Tony Chen, Jin Leqin, Duan Yongping", "Camara")
 
     print(celulares.presentarse())
     print(iphone.presentarse())
     print(oppo.presentarse())