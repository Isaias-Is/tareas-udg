import csv
from typing import List
from materia import Materia

def guardar_csv(nombre_archivo, campos, datos: List[Ma]):
    with open(f'{nombre_archivo}.csv', 'w') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=campos, lineterminator='\n')
        escritor.writeheader()
        escritor.writerows([i.to_dict() for i in datos])
        #Obviously, datos is a list of instances, the class must have a method to_dict().

def recuperar_csv(nombre, lista):
    with open(nombre + '.csv', 'r') as archivo:
        lector = csv.DictReader(archivo)
        lista = []
        for fila in lector:
            lista.append(Materia(fila['id'], fila['nombre'], fila['clave'], fila['carrera'], int(fila['creditos'])))
