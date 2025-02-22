import math

def areaCirculo(radio):
    return math.pi * radio**2

def areaCuadrado(lado):
    return lado**2

def areaTriangulo(base, altura):
    return (base * altura) / 2

def menu():
    print("---------------MENÚ----------------")
    print("- 1. Calcular el área de un círculo")
    print("- 2. Calcular el área de un cuadrado")
    print("- 3. Calcular el área de un triángulo")
    print("- 4. Salir")
    print("-----------------------------------")
    op = int(input("Opción: "))
    if op == 1:
        radio = float(input("Ingrese el radio del círculo: "))
        print("El área del círculo es:", areaCirculo(radio))
    elif op == 2:
        lado = float(input("Ingrese el lado del cuadrado: "))
        print("El área del cuadrado es:", areaCuadrado(lado))
    elif op == 3:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        print("El área del triángulo es:", areaTriangulo(base, altura))
    return op

menu()