from PIL import Image
import matplotlib.pyplot as plt

class Main2(object):
    def __init__(self, path):
        self.path = path

        self.leer(path)

    def leer(self, path):
        
        #Abriendo la imagen.
        imagen = Image.open(path)
        

        # Haciendo un resize de la imagen.
        o_size = (150, 150) # Tamaño del output.
        otp = imagen.resize(o_size, Image.NEAREST) # Imagen redimensionada.

        # Guardando la imagen redimensionada.
        otp.save("imagen_n.bmp")

        #Enseñando la imagen.
        plt.imshow(imagen)
        imagen.show() 


if __name__ == "__main__":

    img = input("Ingrese el nombre de la imagen con su extensión: ")
    Main2(img)