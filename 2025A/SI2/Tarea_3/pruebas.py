import csv
import numpy as np

class Pruebas:
    def __init__(self):
        self.datos = []
        pass

    def probar_producto_punto(self, particula, zMain):
        z = []
        temp = 0
        for i in range(len(self.datos)):
            x = np.array(self.datos[i][:-1])
            temp = np.dot(x, particula)
            z.append(temp)
        #print(f"{"Z Main":^60} | {"Z Prueba":^60}")
        #print(f"{str(zMain):^70} | {str(z):^70}")
        for i in range(len(z)):
            if z[i] != zMain[i]:
                return False
        #print("Exito")
        return True

    def probar_sigmoides(self, particula, sigmoidesMain):
        z = []
        temp = 0
        for i in range(len(self.datos)):
            x = np.array(self.datos[i][:-1])
            temp = np.dot(x, particula)
            z.append(temp)
        z = np.array(z)
        sigmoides = 1 / (1 + np.exp(- z))
        #print(f"{"Sigmoides Main":^60} | {"Sigmoides Prueba":^60}")
        #print(f"{str(sigmoidesMain):^70} | {str(sigmoides):^70}")
        for i in range(len(z)):
            if sigmoides[i] != sigmoidesMain[i]:
                return False
        #print("Exito")
        return True

    def probar_se(self, particula, seMain):
        z = []
        temp = 0
        for i in range(len(self.datos)):
            x = np.array(self.datos[i][:-1])
            temp = np.dot(x, particula)
            z.append(temp)
        z = np.array(z)
        sigmoides = 1 / (1 + np.exp(- z))
        se = []
        for i in range(len(self.datos)):
            x = np.array(self.datos[i][-1:])
            temp = x - sigmoides[i]
            temp = temp ** 2
            se.append(temp)
        #print(f"| {"SE Main":^20} | {"SE Prueba":^20} |")
        #print(f"| {str(seMain):^20} | {str(np.sum(se)):^20} |")
        for i in range(len(z)):
            if np.sum(se) != np.sum(seMain):
                return False
        #print("Exito")
        return True

    def calcular_resultado(self, mejor_particula):
        errorTot = 0
        #print("-------Particula: ", mejor_particula)
        for i in range(len(self.datos)):
            x = np.array(self.datos[i][:-1])
            y = np.array(self.datos[i][-1:])
            #Calculando la predicción logistica.
            z = np.dot(x, mejor_particula)
            yp = 1 / (1 + np.exp(-z))
            error = (y - yp) ** 2
            errorTot += np.sum(error)
            #print("X: ", x, " Error: ", error, " Predicción: ", yp, " y: ", y)
            #print("Z: ", z)
            #print("Error Acumulado: ", errorTot)
        return errorTot / len(self.datos)

    def caso(self, x, res):
        resReal = self.calcular_resultado(x)
        if np.allclose(res, resReal):
            print("Exito")
        else:
            print("Fallo")
        print("Resultado Real | Resultado Dado\n", f"{str(resReal):<14}|{res:<14}")

    def importartDatos(self, nombreArchivo):
        with open(nombreArchivo, 'r') as archivo:  
            lector = csv.DictReader(archivo)
            for fila in lector:
                self.datos.append([1, int(fila['x1']), int(fila['x2']), int(fila['y'])])

    def correr_pruebas(self, mejor_particula, resultado):
        print("-" * 100)
        print(f"| {"RESULTADO":^22} | {"RESULTADO ESPERADO":^22} | {"MEJOR PARTICULA":^46} |")
        print("-" * 100)
        #for i in range(len(self.datos)):
        res = self.calcular_resultado(mejor_particula)
        print(f"| {resultado:^22} | {str(res):^22} | {str(mejor_particula):^46} |")
        print("-" * 100)

#prueba = Pruebas()
#prueba.correr_pruebas()