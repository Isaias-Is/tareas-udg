#Author: Isaias Aldama
#Teacher: Dr. Jorge de Jesús Galvez
#Date: 25 de abril 2025
#Description: Implementation of a PSO and logitical regression.

import csv
import logging
import numpy as np
import time
import matplotlib.pyplot as plt
from matplotlib import cm
from pprint import pprint

#Cargar los datos del archivo CSV.
datos = []
def importartDatos(nombreArchivo):
    with open(nombreArchivo, 'r') as archivo:  
        lector = csv.DictReader(archivo)
        global datos
        for fila in lector:
            datos.append([1, int(fila['x1']), int(fila['x2']), int(fila['y'])])
importartDatos('datos.csv')
datos = np.array(datos)
print("Datos CSV: ", end="")
pprint(datos)
logging.info("Datos CSV:\n", datos)

#MSE for Logistical Regression
def mse_logistico(x): #Recibe la matriz con todas las partículas.
    #print("x: ", end="") or pprint(x)
    z = np.dot(datos[:, :-1], x[:]) # From datos get all the rows, but ignore the last column which is y.
    yp = 1 / (1 + np.exp(- z)) # yp means Y Prima.
    #This is the part where we calculate the MSE.
    """
    for j in range(len(yp)):
        print((datos[j, -1:] - yp[j])**2)
    """
    # The transpose is necessary to make the subtraction work, because datos[:, -1:] is a column vector and yp is a row vector.
    tot = (np.transpose(datos[:, -1:]) - yp) # In order to substract two vectors, they must be of the same shape.
    tot = tot**2
    tot = np.sum(tot)
    print("tot: ", tot/dim)
    return tot / dim

#Hard-coded PSO params.
dim = datos[0].size - 1 # Gets the number of dimensions, we don't take into consideration the y value.
#Tunable
max_iter = 20 # Máximo número de iteraciones.
num_particulas = 15 #Número de partículas que exploran el espacio
lims = np.array([-1, 2]) # Límites del espacio de búsqueda.
w = 1.5 # Factor de incercia.
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
        best_of_best = x[i]
        best_of_best_fitness = fit[i]
    if fit[i] < fit_xp[i]:
        xp[i] = x[i]
        fit_xp[i] = fit[i]

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
    ax.scatter(x[:, 0], x[:, 1], fit[:], c='red', s=10, marker="x")
    fig.canvas.draw()
    fig.canvas.flush_events()
# COPING ENDS HERE.

#Etapa: Main Loop
while iter < max_iter:
    for i in range(num_particulas):
        vel_x[i] = w * vel_x[i] + c1 * np.random.rand() * (xp[i] - x[i]) + c2 * np.random.rand() * (best_of_best - x[i])
        x[i] = np.clip(x[i] + vel_x[i], lims[0], lims[1])
        fit[i] = mse_logistico(np.array(x[i]))
        actualizar_mejor_fitness(i)
        #print(x[i], fit[i])
        # THE FOLLOWING BLOCK OF CODE IS COPIED FROM THE TEACHER'S CODE:
        # In this example, the Sphere function is plotted to
        # visually validate the movement of the search agents.
        if dim == 2:
            plt.cla()
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            plt.title('Sphere Function', fontsize=20)
            ax.plot_surface(xv, yv, fitnessGraph, alpha=0.6)
            ax.scatter(x[:, 0], x[:, 1], fit[:], c='red', s=10, marker="o")
            fig.canvas.draw()
            fig.canvas.flush_events()
            #time.sleep(0.000000001)
            time.sleep(0.1)
    print("Iteración: ", iter, " | Mejor fitness: ", best_of_best_fitness, " | Mejor particula: ", best_of_best)
    #pprint(x)
    iter += 1
    w = .9 - .5 * (iter / max_iter) #Actualizar w so the algorithm behaves besser.
    #print("Iteración: ", iter, " | Mejor fitness: ", best_of_best_fitness, " | Mejor particula: ", best_of_best)

print("Iteración: ", iter)
print("Mejor solución: ", best_of_best, " | Mejor fitness: ", best_of_best_fitness)