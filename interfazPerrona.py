import tkinter as tk
from tkinter import ttk
from matplotlib.ticker import MaxNLocator
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandas import pandas as pd

#Leemos el csv con la información+
errorDeLectura = True
try:
    dogData = pd.read_csv('datos_perros.csv')
except:
    errorDeLectura = False



#Inicialización de la interfaz.
root = tk.Tk()
root.title('Interfaz Perrona')
root.geometry('1200x600')

if (errorDeLectura):
    #Gráfica de la edad de los perros:
    dogAgesFrame = pd.DataFrame(dogData) #Convertimos la información a un dataFrame legible por matplotlib
    dogAgesFigure = plt.figure(figsize=(3, 3), dpi = 100, edgecolor='blue') #Creamos la figura para graficar, definimos resolución y tamaño
    ageAxis = dogAgesFigure.add_subplot(111) #Creamos uno de los ejes para la graficación de las edades
    ageGraph = FigureCanvasTkAgg(dogAgesFigure, root) #Pasamos la figura a la ventana de tkinter
    ageGraph.get_tk_widget().pack(side = tk.LEFT, fill= tk.BOTH) #Pasamos parámetros para el acomdo de el gráfico en la ventana
    dogAgesFrame = dogAgesFrame[['edad']].round(decimals = 0).value_counts().sort_index() #Formateamos el dataFrame para que sea edad->cantidad_de_perros

    #Damos formato a los ejes
    ageAxis.yaxis.set_major_locator(MaxNLocator(integer=True))
    ageAxis.xaxis.set_major_locator(MaxNLocator(integer=True))
    #Gráficamos la cantidad de perros según su edad.
    dogAgesFrame.plot(kind='bar', legend=False, ax = ageAxis)
    ageAxis.set_title('Distribución de perros por edad')


    dogBreedFrame = pd.DataFrame(dogData)
    dogBreedFigure = plt.figure(figsize=(10,3), dpi = 100)
    breedAxis = dogBreedFigure.add_subplot(111)

    breedGraph = FigureCanvasTkAgg(dogBreedFigure, root) #Pasamos la figura a la ventana de tkinter
    breedGraph.get_tk_widget().pack(side = tk.LEFT, fill= tk.BOTH, ipady= 50) #Pasamos parámetros para el acomdo de el gráfico en la ventana

    dogBreedFrame = dogBreedFrame[['raza']].value_counts().sort_values()
    dogBreedFrame.plot(kind = 'bar', legend = False, ax = breedAxis)
    breedAxis.set_title('Gráfico de Frecuencia de razas de perro')


    print (dogBreedFrame)

#
mensajeDeError = tk.Label(root, text='Error al cargar los datos: El archivo no existe' )
mensajeDeError.pack()




root.mainloop()