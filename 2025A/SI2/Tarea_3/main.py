#Author: Isaias Aldama
#Teacher: Dr. Jorge de Jesús Galvez
#Date: 25 de abril 2025
#Description: Implementation of a PSO and logitical regression.

import numpy as np
import csv

datos_path = r"C:\Users\isald\OneDrive\Escritorio\CUCEI\INRO\2025A\Sistemas Inteligentes II\01 Tareas\tareas-udg\2025A\SI2\Tarea_3\datos.csv"

import pruebas
pruebas = pruebas.Pruebas()
pruebas.importartDatos(datos_path)


#np.random.seed(17)

#Cargar los datos del archivo CSV.
datos = []
def importartDatos(nombreArchivo):
    with open(nombreArchivo, 'r') as archivo:  
        lector = csv.reader(archivo)
        lector.__next__()  # El encabezado es omitido.
        global datos
        for fila in lector:
            fila = [1] + [int(i) for i in fila] # Agregamos una dimensión a los datos del CSV.
            datos.append(fila)
importartDatos(datos_path)
datos = np.array(datos)
numDatos = len(datos) # Anzahl of filas.

#MSE for Logistical Regression
def mse_logistico(x): #Recibe una particula.
    z = np.dot(datos[:, :-1], x[:]) # From datos get all the rows, but ignore the last column which is y.
    yp = 1 / (1 + np.exp(- z)) # yp means Y Prima.
    # This is the part where we calculate the MSE.
    # The transpose is necessary to make the subtraction work, because datos[:, -1:] is a column vector and yp is a row vector.
    tot = np.transpose(datos[:, -1:])[0]
    tot = tot - yp # Remove the nested lists and substract yp.
    #print("datos - yp")
    #print(datos[:, -1:])
    #print(yp)
    #print(tot)
    tot = tot**2
    tot = np.sum(tot)
    if not pruebas.probar_se(x, tot):
        raise ValueError("ERROR: Los SE calculados son equivocos.")
    return tot / numDatos

#Hard-coded PSO params.
dim = datos[0].size - 1 # Gets the number of dimensions, we don't take into consideration the y value.
#Tunable
max_iter = 100 # Máximo número de iteraciones.
num_particulas = 10 #Número de partículas que exploran el espacio
lims = np.array([-1, 1]) # Límites del espacio de búsqueda.
w = .9 # Factor de incercia.
c1 = 1.5 # Constante de aceleración 1.
c2 = 1.5 # Constante de aceleración 2.

#BetterNotTouch
iter =  0 # Keeps track of current iterations.
#Matrix
x = np.zeros((num_particulas, dim)) # Partículas de la iteración.
xp = np.zeros((num_particulas, dim)) # Mejores partículas históricamente.
vel_x = np.zeros((num_particulas, dim)) # Para calcular las "velocidades" de las partículas.
fit = np.empty((num_particulas)) # Fitness de las partículas.
fit_xp = np.empty((num_particulas)) # Mejores fitness de cada partícula hitóricamente.
best_of_best = np.zeros(dim) # Mejor partícula global.
best_of_best_fitness = float("inf") # Mejor fitness global, float("inf") inits it to inifity.

def actualizar_mejor_fitness(i):
    global best_of_best, best_of_best_fitness
    if fit[i] < best_of_best_fitness:
        best_of_best = x[i].copy()
        best_of_best_fitness = fit[i].copy()
    if fit[i] < fit_xp[i]:
        xp[i] = x[i].copy()
        fit_xp[i] = fit[i].copy()

#Etapa: Inicialización
for i in range(dim):
    x[:, i] = np.random.rand(num_particulas) * abs(lims[1]-lims[0]) + lims[0]
xp = x

for i in range(num_particulas):
    fit[i] = mse_logistico(x[i])
    fit_xp[i] = fit[i]
    if i == 0:
        best_of_best = x[i]
        best_of_best_fitness = fit[i]
    actualizar_mejor_fitness(i)

#Testing
"""
print("Initial positions (x):", x)
print("Initial velocities (vel_x):", vel_x)
print("Initial fitness values (fit):", fit)
print("Initial personal bests (xp):", xp)
print("Initial personal best fitness values (fit_xp):", fit_xp)
print("Initial global best position:", best_of_best)
print("Initial global best fitness:", best_of_best_fitness)
"""

#Etapa: Main Loop
while iter < max_iter:
    for i in range(num_particulas):
        vel_x[i] = w * vel_x[i] + c1 * np.random.rand() * (xp[i] - x[i]) + c2 * np.random.rand() * (best_of_best - x[i])
        x[i] = np.clip(x[i] + vel_x[i], lims[0], lims[1])
        fit[i] = mse_logistico(np.array(x[i]))
        #pruebas.correr_pruebas(best_of_best, best_of_best_fitness) # For testing.
        actualizar_mejor_fitness(i)
    #print("Iteración: ", iter, " | Mejor fitness: ", best_of_best_fitness, " | Mejor particula: ", best_of_best)
    iter += 1
    w = .9 - .5 * (iter / max_iter) #Actualizar w so the algorithm behaves besser.

#pruebas.correr_pruebas(best_of_best, best_of_best_fitness) # For testing.
print("Iteración: ", iter)
print("Mejor solución: ", best_of_best, " | Mejor fitness: ", best_of_best_fitness)