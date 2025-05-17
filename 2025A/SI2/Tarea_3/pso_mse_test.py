#Author: Isaias Aldama
#Teacher: Dr. Jorge de Jesús Galvez
#Description: Implementation of a PSO and logitical regression.

from operator import le
import numpy as np
from matplotlib import cm
import time
import matplotlib.pyplot as plt

np.random.seed(14)

datos = []
def importartDatos(nombreArchivo):
    with open(nombreArchivo, 'r') as archivo:
        archivo.readline() # Skip the header line
        global datos
        for fila in archivo:
            lineaDatos = fila.strip()
            lineaDatos = [1] + [int(i) for i in lineaDatos.split(',')]
            datos.append(lineaDatos)
importartDatos(r'C:\Users\isald\OneDrive\Escritorio\CUCEI\INRO\2025A\Sistemas Inteligentes II\01 Tareas\tareas-udg\2025A\SI2\Tarea_3\datos.csv')
datos = np.array(datos)
print("Datos CSV: ", end="")

def mse(x):
    sumTot = 0
    for i in range(len(datos)):
        # This is the part where we calculate the MSE.
        yp = np.dot(np.transpose(datos[i][:-1]), x[:]) # yp means Y Prima.
        tot = np.sum(datos[i][-1:] - yp) # In order to substract two vectors, they must be of the same shape.
        tot = tot**2
        sumTot += np.sum(tot)
    return sumTot/dim

#Hard-coded PSO params.
dim = datos[0].size - 1 # Gets the number of dimensions, we don't take into consideration the y value.
#Tunable
max_iter = 50 # Máximo número de iteraciones.
num_particulas = 10 #Número de partículas que exploran el espacio
lims = np.array([-50, 50]) # Límites del espacio de búsqueda.
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
        #Copy most be used to avoid reference issues.
        # If not then changes in the reference will afecct the global best and personal bests too.

#Etapa: Inicialización
for i in range(dim):
    x[:, i] = np.random.rand(num_particulas) * abs(lims[1]-lims[0]) + lims[0]
xp = x

for i in range(num_particulas):
    fit[i] = mse(x[i])
    fit_xp[i] = fit[i]
    if i == 0:
        best_of_best = x[i]
        best_of_best_fitness = fit[i]
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
            arr = [xv[i, j], yv[i, j]]
            fitnessGraph[i, j] = mse(np.asarray(arr))
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
        p1 = w * vel_x[i]
        p2 =  c1 * np.random.rand() * (xp[i] - x[i]) 
        p3 = c2 * np.random.rand() * (best_of_best - x[i])
        vel_x[i] = w * vel_x[i] + c1 * np.random.rand() * (xp[i] - x[i]) + c2 * np.random.rand() * (best_of_best - x[i])
        x[i] = np.clip(x[i] + vel_x[i], lims[0], lims[1])
        fit[i] = mse(np.array(x[i]))
        actualizar_mejor_fitness(i)
        # THE FOLLOWING BLOCK OF CODE IS COPIED FROM THE TEACHER'S CODE:
        # In this example, the Sphere function is plotted to
        # visually validate the movement of the search agents.
        if dim == 2 and max_iter * .1 > iter:
            plt.cla()
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            plt.title('Sphere Function', fontsize=20)
            ax.plot_surface(xv, yv, fitnessGraph, alpha=0.6, cmap=cm.viridis)
            ax.scatter(x[:, 0], x[:, 1], fit[:], c='red', s=10, marker="o")
            fig.canvas.draw()
            fig.canvas.flush_events()
            time.sleep(0.001)
    print("Iteración: ", iter, " | Mejor fitness: ", best_of_best_fitness, " | Mejor particula: ", best_of_best)
    iter += 1
    w = .9 - .6 * (iter / max_iter) #Actualizar w so the algorithm behaves besser.

print("-----Fin PSO------")
print("Mejor solución: ", best_of_best, " | Mejor fitness: ", best_of_best_fitness)
