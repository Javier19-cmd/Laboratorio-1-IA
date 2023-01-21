"""
Nombre: Javier Sebastián Valle Balsells
Carnet: 20159
Fecha: 19/01/2023
Pilow podría ser lo mínimo para el manejo de imágenes, pero no es el único.
"""

# import pygame as pg

# # Inicialización de Pygame
# pg.init()

from PIL import Image, ImageDraw
import escritor as esc
from OpenGL.GL import *

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
        
        #Leyendo el mapa de bits de la imagen y guardando el valor de cada pixel en una matriz.
        for i in range(alto):
            self.matrix.append([])
            for j in range(ancho):
                self.matrix[i].append(imagen.getpixel((j,i)))
                # Imprimiendo la matriz.
                #print(self.matrix[i][j], end=" ")
        
        esc.Escritor(self.matrix, ancho, alto) #Creando la imagen con el mapa de bits de la imagen original.

        # # Open the image file
        # im = Image.open(self.image)

        # # Create a copy of the image
        # im_squares = im.copy()

        # # Create an ImageDraw object
        # draw = ImageDraw.Draw(im_squares)

        # # Define the size of the squares
        # square_size = 1

        # # Get the color of each pixel
        # pixels = im.load()

        # # Loop through all the pixels
        # for x in range(im.width):
        #     for y in range(im.height):
        #         # Get the color of the current pixel
        #         color = pixels[x, y]

        #         # Draw a square for the current pixel
        #         draw.rectangle((x*square_size, y*square_size, (x+1)*square_size, (y+1)*square_size), fill=(100, 15, 12))

        # # Save the image with squares to a new file
        # im_squares.save("imagen.bmp")


        #esc.Escritor(self.matrix)
if __name__ == "__main__":

    #Pidiendo al usuario que de el nombre de la imagen.
    nombre_imagen = input("Ingrese el nombre de la imagen con su extensión: ")
    main = Main(nombre_imagen)