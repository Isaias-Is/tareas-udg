from random import randint
import csv
from nicegui import events

class Punto:
    _id = 0

    def __init__(self, x, y, radio, color):
        Punto._id += 1
        self.id = Punto._id
        self.x = x
        self.y = y
        self.radio = radio
        self.color = [color[0], color[1], color[2]]

    def a_diccionario(self):
        return {
            'id': self.id,
            'x': self.x,
            'y': self.y,
            'radio': self.radio,
            'color': f"{str(self.color[0])}, {str(self.color[1])}, {str(self.color[2])}"
        }

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id


def punto_aleatorio() -> Punto:
    return Punto(randint(0,500), randint(0,500), randint(5,50), (randint(0,255), randint(0,255), randint(0,255)))


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

    def cargar(self, archivo: events.UploadEventArguments):
        contenido = archivo.content.read().decode('utf-8').splitlines()
        lector = csv.DictReader(contenido)
        self.puntos.clear()
        for fila in lector:
            punto = Punto(int(fila['x']), int(fila['y']), int(fila['radio']), (0,0,0))
            color = fila['color'].strip().split(',')
            color = [i.strip() for i in color]
            punto.color = color
            punto.id = int(fila['id'])
            self.puntos.append(punto)
        #print("PUNTOS\n")
        #print(f"{'ID':<5}{'X':<5}{'Y':<5}{'Radio':<4}{'Color (R,G,B)':<15}")
        #for punto in self.puntos:
            #print(f"{punto.id:<5}{punto.x:<5}{punto.y:<5}{punto.radio:<4}{punto.color[0]:<4}{punto.color[1]:<4}{punto.color[2]:<4}")


    def ordenar_por(self, atributo:str, orden:str=['ascendente', 'descendente']):
        if orden == 'ascendente':
            orden = False
        else:
            orden = True

        if atributo == 'x':
            self.puntos.sort(key=lambda punto: punto.x, reverse=orden)
        elif atributo == 'y':
            self.puntos.sort(key=lambda punto: punto.y, reverse=orden)
        elif atributo == 'radio':
            self.puntos.sort(key=lambda punto: punto.radio, reverse=orden)
        elif atributo == 'color':
            self.puntos.sort(key=lambda punto: punto.color, reverse=orden)
        elif atributo == 'id':
            self.puntos.sort(key=lambda punto: punto.id, reverse=orden)
        else:
            raise ValueError("Atributo no válido para ordenar.")
