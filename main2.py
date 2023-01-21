"""
Nombre: Javier Sebastián Valle Balsells
Carnet: 20159
Sección de clase: 20

Referencias: 

1. Pixelar una imagen: https://towardsdatascience.com/convert-photo-into-pixel-art-using-python-d0b9bd235797
"""

from PIL import Image
import matplotlib.pyplot as plt
from frame import * # Importando el módulo frame.py

class Main2(object):
    def __init__(self, path):
        self.path = path
        self.pixels = []
        self.leer(path)
        #self.barrer()

    def leer(self, path):
        
        #Abriendo la imagen.
        imagen = Image.open(path)
    
        # Obteniendo el tamaño de la imagen.
        width, height = imagen.size

        print("Ancho: ", width, "Alto: ", height)


        # Si las dimensiones son menores a 500, se aumenta el tamaño de la imagen.
        if width <= 500 and height <= 500:
            
            print("Llegué acá tercero")
            an = int(width//14)
            al = int(height//14)

        # Si las dimensiones están entre 500 y 1000, se reduce el tamaño de la imagen.
        elif (width >= 500 and height >= 500) and (width < 1000 and height < 1000):
            
            print("Llegué acá primero")
            an = int(width//4)
            al = int(height//4)        
        
        elif (width >= 1000 and height >= 1000) and (width < 1500 and height < 1500):
            
            print("Llegué acá segundo")
            an = int(width//14)
            al = int(height//14)

        # Si las dimensiones están entre 1500 y 2000, se reduce el tamaño de la imagen.
        if (width > 1500 and height > 1500) and (width <= 2000 and height <= 2000):
            
            print("Llegué acá tercero")
            an = int(width//26)
            al = int(height//26)

        # Haciendo un resize de la imagen.
        o_size = (an, al) # Tamaño del output.
        otp = imagen.resize(o_size, Image.NEAREST) # Imagen redimensionada.

        # Guardando la imagen redimensionada.
        otp.save("res.bmp")

        #Enseñando la imagen.
        #plt.imshow(imagen)
        #imagen.show()

        #Leyendo el mapa de bits de la imagen y guardando el valor de cada pixel en una matriz.
        for i in range(width):
            self.pixels.append([])
            for j in range(height):
                self.pixels[i].append(imagen.getpixel((j,i)))
                # Imprimiendo la matriz.
                #print(self.matrix[i][j], end=" ")

        # # Escribiendo la matriz en un archivo.
        # with open("matriz.txt", "w") as f:
        #     for i in range(width):
        #         for j in range(height):
        #             f.write(str(self.pixels[i][j]))
        #         f.write("\n")

        #print(self.pixels)
    
    # Método para barrer los pixeles que no son completamente negros, rojos o verdes.
    def barrer(self):
        # Recorriendo la matriz.
        for i in range(len(self.pixels)):
            for j in range(len(self.pixels[i])):
                # Si el pixel no es completamente rojo o verde, se convierten a blanco.
                if self.pixels[i][j] != (255, 0, 0) or self.pixels[i][j] != (0, 255, 0): # Verde o rojo.
                    
                    self.pixels[i][j] = (255, 255, 255) # Blanco.

                if self.pixels[i][j] != (0, 0, 0): # Si el pixel es diferente de negro, entonces se convierte a blanco.
                    
                    self.pixels[i][j] = (255, 255, 255) # Blanco.
        
        #print(self.pixels)


if __name__ == "__main__":

    img = input("Ingrese el nombre de la imagen con su extensión (la extensión debe ser .bmp): ")
    Main2(img)