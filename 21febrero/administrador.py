from typing import List
from materia import Materia, generarMateriaAleatoria #Mi clase.

class Administrador:
    def __init__(self):
        self.materias: List[Materia] = []

    def agregarMateria(self, materia: Materia):
        self.materias.append(materia)

    def mostrarMaterias(self):
        for materia in self.materias:
            print(materia)

    def mostrarTablaMaterias(self):
        print(f"{'Clave':<7}{'Nombre':<28}{'Carrera':<10}{'Creditos':<4}")
        print("-"*53)
        for materia in self.materias:
            print(f"{materia.clave:<7}{materia.nombre:<28}{materia.carrera:<10}{materia.creditos:<4}")

    def agregarMateriaAleatoria(self):
        materia = generarMateriaAleatoria()
        self.materias.append(materia)

    def respaldar(self, nombre):
        with open(nombre+'.csv', "w") as archivo:
            for materia in self.materias:
                archivo.write(f"{materia}\n")

    def recuperar(self, nombre):
        self.materias.clear()
        with open(nombre+'.csv', "r") as archivo:
            for linea in archivo:
                linea = linea.strip().split(",") #Separa cada atributo de la clase.
                materia = Materia()
                materia.nombre = linea[0].split("=")[1]
                materia.clave = linea[1].split("=")[1]
                materia.carrera = linea[2].split("=")[1]
                materia.creditos = int(linea[3].split("=")[1])
                self.materias.append(materia)
