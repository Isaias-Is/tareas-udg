from random import randint

#Base class.
class Materia:
    def __init__(self):
        self.nombre = ""
        self.clave = ""
        self.carrera = ""
        self.creditos = 0
    
    def __repr__(self):
        return f"nombre={self.nombre},clave={self.clave},carrera={self.carrera},creditos={self.creditos}"

#Funcion que genera materias aleatorias.
nombres = ["Calculo", "Algebra", "Fisica", "Quimica", "Biologia", "Programacion", "Base de Datos", "Redes", "Sistemas Operativos", "Estructura de Datos", "Analisis de Algoritmos", "Inteligencia Artificial", "Mineria de Datos", "Probabilidad y Estadistica", "Matemáticas Discretas", "Lógica y Conjuntos", "Teoria de la Computacion", "Compiladores", "Sistemas Embebidos"]
carreras = ["INRO", "INCO", "INBI", "INME", "INCE", "INFO", "INQU"]
creditos = [5,8]
def generarMateriaAleatoria() -> Materia:
    materia = Materia()
    materia.nombre = f"{nombres[randint(0, len(nombres)-1)]}"
    materia.clave = f"{chr(randint(65,90))}{randint(1000,9999)}"
    materia.carrera = f"{carreras[randint(0, len(carreras)-1)]}"
    materia.creditos = creditos[randint(0,1)]
    return materia