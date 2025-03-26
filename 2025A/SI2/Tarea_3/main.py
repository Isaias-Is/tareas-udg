#Author: Isaias Aldama
#Teacher: Dr. Jorge de Jesús Galvez
#Date: 25 de abril 2025
#Description: Implementation of a PSO and logitical regression.

import csv
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import time

#Hard-coded PSO params.
#Tunable
dim = 2 #Hard code number of dimensions.
max_iter = 100 # Máximo número de iteraciones.
num_particulas = 6 #Número de partículas que exploran el espacio
lims = np.array([-5,5]) # Límites del espacio de búsqueda.
w = 0.5 # Factor de incercia.
c1 = 1 # Constante de aceleración 1.
c2 = 1 # Constante de aceleración 2.

#BetterNotTouch
it =  0 # Keeps track of current iterations.
#Matrix
x = np.zeros((num_particulas, dim)) #Partículas de la iteración.
#xp = np.zeros((num_particulas, dim)) #Mejores partículas históricamente.
vel_x = np.zeros((num_particulas, dim)) #Para calcular las "velocidades" de las partículas.
fit = np.empty((num_particulas)) #Fitness de las partículas.
fit_xp = np.empty((num_particulas)) #Mejores fitness de cada partícula hitóricamente.
best_of_best = np.zeros(dim) #Mejor partícula global.
best_of_best_fitness = np.nan #Mejor fitness global.

#Obtener datos del archivo CSV.
datos = []
def importartDatos(nombreArchivo):
    with open(nombreArchivo, 'r') as archivo:  
        lector = csv.DictReader(archivo)
        global datos
        for fila in lector:
            datos.append([1, int(fila['x1']), int(fila['x2']), int(fila['y'])])
importartDatos('datos.csv')

#MSE for Logistical Regression
def mse_logistico(x): #Recibe la matriz con todas las partículas.
    n = len(datos) #Número de datos.
    tot = 0
    for i in range(n):
        tot += 1 / (1 + np.exp(-1 * np.dot(np.array(datos[i][:]), x)))
    return tot

def actualizar_mejor_fitness(i):
    if fit[i] < best_of_best_fitness:
        best_of_best = x[i]
        best_of_best_fitness = fit[i]
    if fit[i] < fit_xp[i]:
        xp[i] = x[i]
        fit_xp[i] = fit[i]

#Etapa: Inicialización
#Only works for 2D!!! #Replace using teacher initializaction method.
for i in range(dim):
    x[:, i] = np.random.rand(num_particulas) * (lims[0]+lims[1]) - lims[0]
xp = x

for i in range(num_particulas):
    fit[i] = mse_logistico(np.array(x[i]))
    fit_xp[i] = fit[i]
    actualizar_mejor_fitness(i)

#Etapa: Main Loop
while iter < max_iter:
    for i in range(num_particulas):
        vel_x[i] = w * vel_x[i] + c1 * np.random.rand() * (xp[i] - x[i]) + c2 * np.random.rand() * (best_of_best - x[i])
        x[i] = x[i] + vel_x[i]
        fit[i] = mse_logistico(np.array(x[i]))
        actualizar_mejor_fitness(i)

    # THE FOLLOWING BLOCK OF CODE IS COPIED FROM THE TEACHER'S CODE:
    # Graph initialization parameters only for fitness functions
    # defined by 2 decision variables.
    if dim == 2:
        res = 32
        xGraph = np.linspace(lims[0], lims[1], res)
        yGraph = np.linspace(lims[0], lims[1], res)
        xv, yv = np.meshgrid(xGraph, yGraph)
        fitnessGraph = np.zeros((res, res))
        for i in range(res):
            for j in range(res):
                arr = [[xv[i, j], yv[i, j]]]
                fitnessGraph[i, j] = mse_logistico(np.asarray(arr))
        plt.ion()
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        plt.title('mse Function', fontsize=20)
        ax.plot_surface(xv, yv, fitnessGraph, alpha=0.6, cmap=cm.viridis)
        ax.scatter(x[:, 0], x[:, 1], fit[:], c='red', s=10, marker="o")
        fig.canvas.draw()
        fig.canvas.flush_events()
        time.sleep(0.000000001)

