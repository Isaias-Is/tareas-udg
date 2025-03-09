from typing import List
from nicegui import events
import csv
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
                archivo.write(f"{materia}\n".encode('utf-8'))

    def recuperar(self, nombre):
        self.materias.clear()
        with open(nombre+'.csv', "r") as archivo:
            for linea in archivo:
                linea = linea.strip().split(",") #Separa cada atributo de la clase.
                materia = Materia()
                materia.id = int(linea[0].split("=")[1])
                materia.nombre = linea[1].split("=")[1]
                materia.clave = linea[2].split("=")[1]
                materia.carrera = linea[3].split("=")[1]
                materia.creditos = int(linea[4].split("=")[1])
                self.materias.append(materia)

    def respaldarCSV(self, nombre):
        with open(nombre + '.csv', 'w') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=['id', 'nombre', 'clave', 'carrera', 'creditos'], lineterminator='\n')
            escritor.writeheader()
            escritor.writerows([i.to_dict() for i in self.materias])
            
    def recuperarCSV(self, nombre):
        with open(nombre + '.csv', 'r') as archivo:
            lector = csv.DictReader(archivo)
            self.materias = []
            for fila in lector:
                mat = Materia(fila['nombre'], fila['clave'], fila['carrera'], int(fila['creditos']))
                mat.id = int(fila['id'])
                self.materias.append(mat)
    
    def cargarCSV(self, archivo: events.UploadEventArguments):
        contenido = archivo.content.read().decode('utf-8').splitlines()
        lector = csv.DictReader(contenido)
        for fila in lector:
            mat = Materia(fila['nombre'], fila['clave'], fila['carrera'], int(fila['creditos']))
            mat.id = int(fila['id'])
            self.materias.append(mat)