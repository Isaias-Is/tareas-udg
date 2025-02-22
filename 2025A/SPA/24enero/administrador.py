from typing import List

class Tanque():
    def __init__(self, nombre, salud, vel):
        self.nombre = nombre 
        self.salud = salud
        self.vel = vel

class Administrador():
    def __init__(self):
        self.lista:List[Tanque] = []

    def agregarTanque(self):
        print("-------Agregar Tanque------")
        nombre = input("Nombre: ")
        salud = int(input("Salud: "))
        vel = float(input("Vel: "))
        self.lista.append(Tanque(nombre, salud, vel))

    def mostrarTanques(self):
        for elem in self.lista:
            print("-----------------------------")
            print(f"Tanque: {elem.nombre}")
            print(f"- Salud: {elem.salud}")
            print(f"- Velocidad: {elem.vel}")
