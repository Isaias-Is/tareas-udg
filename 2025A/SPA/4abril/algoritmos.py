from dataclasses import dataclass
from random import randint
from typing import List
from math import sqrt

@dataclass
class Punto:
    x: int
    y: int
    red: int
    green: int
    blue: int
    radio: int

def generar_punto() -> Punto:
    return Punto(randint(0,500), randint(0,500), randint(0,255), randint(0,255), randint(0,255), randint(5,50))

@dataclass
class PuntoMasCercano:
    punto1: Punto
    punto2: Punto

def puntos_mas_cercanos(puntos: List[Punto]) -> List[PuntoMasCercano]:
    if len(puntos) <= 1:
        print("Error: Se necesitan como mínimo 2 puntos.")
        return
    resultados = []
    i = 0
    while i < len(puntos):
        punto1 = puntos[i]
        distancia_min = float('inf')
        j = 0
        while j < len(puntos):
            if i == j:
                j += 1
                continue
            punto2 = puntos[j]
            distancia = sqrt((punto2.x-punto1.x)**2 + (punto2.y-punto1.y)**2)
            if distancia < distancia_min:
                puntos_mas_cercanos = PuntoMasCercano(punto1, punto2)
                distancia_min = distancia
            j += 1
        resultados.append(puntos_mas_cercanos)
        i = i + 1
    return resultados