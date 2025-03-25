import csv
from typing import List
from bici import Bici
from nicegui import events

class Bicipuerto:
    def __init__(self):
        self.bicis : List[Bici] = []

    def ingresar_bici(self, bici: Bici):
        for b in self.bicis:
            if b._id == bici._id:
                b.horasUso += bici.horasUso
                b.metrosRecorridos += bici.metrosRecorridos
                return 0
        self.bicis.append(bici)
        return 1

    def mostrar_tabla_bicis(self):
        print(f"|{'ID':^6}|{'Horas uso':^11}|{'Metros recorridos':^19}|")
        for bici in self.bicis:
            print(f"|{bici._id:<6}|{bici.horasUso:<11}|{bici.metrosRecorridos:<19}|")

    def respaldarCSV(self, nombre):
        with open(nombre + '.csv', 'w') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=['id', 'horasUso', 'metrosRecorridos'], lineterminator='\n')
            escritor.writeheader()
            escritor.writerows([i.to_dict() for i in self.bicis])
            
    def cargarCSV(self, archivo: events.UploadEventArguments):
        contenido = archivo.content.read().decode('utf-8').splitlines()
        lector = csv.DictReader(contenido)
        self.bicis.clear()
        for fila in lector:
            mat = Bici(horasUso=fila['horasUso'], metrosRecorridos=fila['metrosRecorridos'])
            mat._id = int(fila['id'])
            self.bicis.append(mat)