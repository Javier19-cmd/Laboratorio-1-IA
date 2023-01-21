"""
Nombre: Javier Sebastián Valle Balsells
Carnet: 20159
Sección de clase: 20

Referencias: 

1. Pixelar una imagen: https://towardsdatascience.com/convert-photo-into-pixel-art-using-python-d0b9bd235797
"""

from PIL import Image
import matplotlib.pyplot as plt

class Main2(object):
    def __init__(self, path):
        self.path = path
        self.pixels = []
        self.leer(path)

    def leer(self, path):
        
        #Abriendo la imagen.
        imagen = Image.open(path)
    
        # Obteniendo el tamaño de la imagen.
        width, height = imagen.size

        # Si las son mayores a 500, se reduce el tamaño de la imagen.
        if width > 500 and height > 500:
            an = int(width//4)
            al = int(height//4)
        # Si las dimensiones son menores a 500, se aumenta el tamaño de la imagen.
        elif width <= 500 and height <= 500:
            an = int(width//14)
            al = int(height//14)


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


if __name__ == "__main__":

    img = input("Ingrese el nombre de la imagen con su extensión: ")
    Main2(img)