from random import randint
import csv

class Punto:
    _id = 0
    def __init__(self, x, y, radio, r, g, b):
        self._id += 1
        self.id = Punto._id
        self.x = x
        self.y = y
        self.radio = radio
        self.color = (r, g, b)

    def a_diccionario(self):
        return {
            'id': self.id,
            'x': self.x,
            'y': self.y,
            'radio': self.radio,
            'color': (self.color[0], self.color[1], self.color[2])
        }

    def ordenar_por(self, atributo:str):
        if atributo == 'x':
            self.puntos.sort(key=lambda punto: punto.x)
        elif atributo == 'y':
            self.puntos.sort(key=lambda punto: punto.y)
        elif atributo == 'radio':
            self.puntos.sort(key=lambda punto: punto.radio)
        elif atributo == 'color':
            self.puntos.sort(key=lambda punto: punto.color)
        elif atributo == 'id':
            self.puntos.sort(key=lambda punto: punto.id)
        else:
            raise ValueError("Atributo no válido para ordenar.")

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

def punto_aleatorio() -> Punto:
    return Punto(randint(0,500), randint(0,500), randint(5,50), randint(0,255), randint(0,255), randint(0,255))

class AdministradorPuntos:
    def __init__(self):
        self.puntos = []

    def limpiar(self):
        self.puntos.clear()

    def insertar_al_final(self, punto:Punto):
        self.puntos.append(punto)

    def generar(self):
        self.puntos.append(punto_aleatorio())

    def mostrar_en_tabla(self):
        print("-" * 20 + "PUNTOS" + "-" * 20)
        print(f"{'ID':<5}{'X':<5}{'Y':<5}{'Radio':<4}{'Color (R,G,B)':<15}")
        for punto in self.puntos:
            print(f"{punto.id:<5}{punto.x:<5}{punto.y:<5}{punto.radio:<4}{punto.color[0]:<4}{punto.color[1]:<4}{punto.color[2]:<4}")
        print("-" * 45)

    def respaldar(self, nombre_archivo:str):
        with open (nombre_archivo, 'w') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=['id', 'x', 'y', 'radio', 'color'], lineterminator='\n')
            escritor.writeheader()
            escritor.writerows([i.a_diccionario() for i in self.puntos])

    def recuperar(self, nombre_archivo:str):
        with open(nombre_archivo, 'r') as archivo:
            lector = csv.DictReader(archivo)
            self.puntos.clear()
            for fila in lector:
                punto = Punto(int(fila['x']), int(fila['y']), int(fila['radio']), int(fila['color'][1]), int(fila['color'][3]), int(fila['color'][5]))
                punto.id = int(fila['id'])
                self.puntos.append(punto)        
