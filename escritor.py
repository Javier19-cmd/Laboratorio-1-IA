"""
Nombre: Javier Sebastián Valle Balsells
Carnet: 20159
Fecha: 19/01/2023
"""
import cv2
import PIL as pil
from utilidades import *

class Escritor(object):
    def __init__(self, matriz, ancho, alto):
        self.matriz = matriz
        self.width = ancho
        self.height = alto

        self.colors = bytes((0, 0, 0))

        self.color_pixeles = []

        self.barrido()
        #self.cambio_color()
        self.escribir_imagen()

    def barrido(self): 
        self.color_pixeles = [
            [self.colors for x in range(self.width)]
                for y in range(self.height)
        ]


    def cambio_color(self):
        
        # Definiendo el tamaño del pixel.
        pixel = 5

        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                # Convirtiendo cada pixel a un color.
                color = self.matriz[i][j]

                # Convirtiendo el color a bytes.
                color = bytes(color)
                
                #print(color)

                # Reemplazando el color del pixel en la matriz color_pixeles.
                for k in range(pixel):
                    for l in range(pixel):
                        self.color_pixeles[pixel + k][pixel + l] = color

    def escribir_imagen(self):

        #print(self.color_pixeles)


        #self.cambio_color()

        # Creando archivo jpg con el nombre de la imagen.
        f = open("imagen.bmp", "bw")
        #Haciendo el pixel header.
        f.write(char('B'))
        f.write(char('M'))
        #Escribiendo el tamaño del archivo en bytes.
        f.write(dword(14 + 40 + self.width * self.height * 3))
        f.write(dword(0)) #Cosa que no se utilizará en este caso.
        f.write(dword(14 + 40)) #Offset a la información de la imagen. 14 bytes para el header, 40 para la información de la imagen. Aquí empieza la data.
        #Lo anterior suma 14 bytes.

        #Información del header.
        f.write(dword(40)) #Este es el tamaño del header. Esto es de 4 bytes, por eso se utiliza el dword.
        f.write(dword(self.width)) #Ancho de la imagen. Esto es de 4 bytes, por eso se utiliza el dword.
        f.write(dword(self.height)) #Alto de la imagen. Esto es de 4 bytes, por eso se utiliza el dword.
        f.write(word(1)) #Número de planos. Esto es de 2 bytes, por eso se utiliza el word.
        f.write(word(24)) #24 bits por pixel. Esto es porque usa el true color y el RGB.
        f.write(dword(0)) #Esto es la compresión. Esto es de 4 bytes, por eso se utiliza el dword.
        f.write(dword(self.width * self.height * 3)) #Tamaño de la imagen sin el header.
        #Pixels que no se usarán mucho.
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        #Lo anterior suma 40 bytes.

        #print("Framebuffer", framebuffer)
        #Pintando el archivo de color negro.
        for y in range(self.height):
            for x in range(self.width):
                f.write(self.color_pixeles[y][x])
        
        #print("Archivo escrito")

        f.close() #Cerrando el archivo que se escribió.

    def crear_cuadricula(): #Método para crear la cuadrícula de la imagen.
        
        pass
