"""
Nombre: Javier Sebastián Valle Balsells
Carnet: 20159
Fecha: 19/01/2023
Pilow podría ser lo mínimo para el manejo de imágenes, pero no es el único.
"""

# import pygame as pg

# # Inicialización de Pygame
# pg.init()

from PIL import Image

class Main(object):
    def __init__(self, image):
        self.image = image # Imagen a mostrar.
        self.matrix = [] # Matriz de la imagen.
        self.leer_imagen() # Mostrar imagen.

    def leer_imagen(self): #Método que se encarga de leer y recorrer el mapa de bits de la imagen.
        imagen = Image.open(self.image)
        
        # Obtener el ancho y alto de la imagen.
        ancho, alto = imagen.size
        #print("Ancho: ", ancho, "Alto: ", alto)
        
        #Leyendo el mapa de bits de la imagen.
        for i in range(alto):
            self.matrix.append([])
            for j in range(ancho):
                self.matrix[i].append(imagen.getpixel((j,i)))
        
        print(self.matrix)
        

if __name__ == "__main__":

    #Pidiendo al usuario que de el nombre de la imagen.
    nombre_imagen = input("Ingrese el nombre de la imagen con su extensión: ")
    main = Main(nombre_imagen)