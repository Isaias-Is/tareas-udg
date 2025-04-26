from punto import Punto
from typing import List, Dict, Set

class Grafo:
    def __init__(self, puntos: List[Punto]):
        self.grafo: Dict[Punto, Set[Punto]] = {punto: set() for punto in puntos}
        
    def agregar_conexion(self, punto1: Punto, punto2: Punto):
        if punto1 == punto2:
            raise ValueError("Se esta tratando de conectar un punto a si mismo")
        self.grafo[punto1].add(punto2)
        self.grafo[punto2].add(punto1)
        #print(f"Grafo: {self.grafo}")

    def eliminar_conexion(self, punto1: Punto, punto2: Punto):
        if punto1 == punto2:
            raise ValueError("No existe una conexion entre un punto y si mismo")
        if punto1 not in self.grafo[punto2]:
            raise ValueError("No hay conexion entre los puntos")
        self.grafo[punto1].remove(punto2)
        self.grafo[punto2].remove(punto1)

    def agregar_puntos(self, punto: Punto):
        self.grafo[punto] = set()

    def checar_nuevos_puntos(self, puntos: List[Punto]):
        for punto in puntos:
            if punto not in self.grafo.keys():
                self.grafo[punto] = set()