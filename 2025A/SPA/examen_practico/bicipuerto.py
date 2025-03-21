from typing import List
from bici import Bici

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