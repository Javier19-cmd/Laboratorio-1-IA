"""
Nombre: Javier Sebastián Valle Balsells
Carnet: 20159
Sección de clase: 20
Clase FrameWork: Esta clase se encarga de crear la matriz que se utilizará para el frame y para definir las acciones, stepCost(s, a, s'), etc.
Se tiene que usar el paradigma de programación orientada a objetos.
"""

class FrameWork(object):
    def __init__(self, matriz):
        self.matriz = matriz

        self.posiciones_blancos = [] # Posiciones en donde se encuentran los colores blancos.

        self.posiciones_negros = [] # Posiciones en donde se encuentran los colores negros.

        self.posiciones_verdes = [] # Posiciones en donde se encuentran los colores verdes.
        
        self.color_temporal = []
        self.colores_blancos = []

        self.posiciones_rojos = [] # Posiciones en donde se encuentran los colores rojos.
        self.rojo = [] # Guardando los rojos temporales.
        self.final = [] # Lista que almacenará los colores rojos que se encuentren en la matriz.
        self.buscar = () # Variable que almacenará el color rojo que se encuentre en la matriz.

        #print(self.matriz)

        self.action() # Definiendo las acciones que tomará el agente para llegar a la meta.

    def action(self): # Definiendo las acciones que tomará el agente para llegar a la meta.

        # Buscando el color rojo en la matriz.
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                # Verificando que cada color empiece con 235, 0, 0 y termine con 255, 0, 0 y que no tenga colores intermedios.
                if self.matriz[i][j] >= (230, 0, 0) and self.matriz[i][j] <= (255, 0, 0):
                    #print("El color es rojo")
                    #print("Posición: ", i, j)
                    self.rojo.append((self.matriz[i][j]))
        
        # Detectando que las segundas y las terceras posiciones de las tuplas sean menores a 100.
        for i in range(len(self.rojo)):
            if self.rojo[i][1] < 100 and self.rojo[i][2] < 100:
                #print("El color es rojo")
                #print("Posición: ", i, j)
                #self.posiciones.append((i, j))
                self.final.append(self.rojo[i])

        #print("Final", self.final)
        
        # Almacenando cada color rojo de la lista final en una variable temporal para buscarlo en la lista matriz.
        for i in range(len(self.final)):
            self.a = self.final[i]
            #print("A", self.a)

        # Buscando cada color rojo en la lista matriz.
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                if self.matriz[i][j] == self.a:
                    #print("El color es rojo")
                    #print("Posición: ", i, j)
                    self.posiciones_rojos.append((i, j))
        
        #print("Posiciones", self.posiciones_rojos)
        
        
        # Recorriendo la matriz e identificando los colores que sean blancos o parecidos.
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                
                # Verificar si el color esté en el rango de los colores blancos.

                if self.matriz[i][j] >= (217, 217, 217) and self.matriz[i][j] <= (255, 255, 255):
                   # print("El color es blanco")
                    #print("Posición: ", i, j)
                    #print("Color blanco", self.matriz[i][j])
                    
                    # Detectando que las segundas y las terceras posiciones de las tuplas sean mayores a 100.
                    if self.matriz[i][j][1] > 100 and self.matriz[i][j][2] > 100:
                        #print("El color es blanco")
                        #print("Posición: ", i, j)
                        #print("Color blanco", self.matriz[i][j])
                        # self.color_temporal.append((self.matriz[i][j]))
                        # self.colores_blancos.append((i, j))
                        #print("Color: ", self.matriz[i][j])

                        # Guardando las posiciones de los colores blancos en una lista.
                        self.posiciones_blancos.append((i, j))

        #print("Posiciones blancos: ", self.posiciones_blancos)

        # Recorriendo la matriz e identificando los colores que sean negros.
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                # Verificar si el color esté en el rango de los colores negros.
                if self.matriz[i][j] >= (0, 0, 0) and self.matriz[i][j] <= (50, 50, 50):
                    #print("El color es negro", self.matriz[i][j])

                    # Verificando que las segundas y las terceras posiciones de las tuplas sean menores a 100.
                    if self.matriz[i][j][1] < 100 and self.matriz[i][j][2] < 100:
                        self.posiciones_negros.append((i, j))
        
        #print("Posiciones: ", self.posiciones_negros)
        
        # Recorriendo la matriz e identificando los colores que sean negros.
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                # Verificar si el color esté en el rango de los colores negros.
                if self.matriz[i][j] >= (0, 100, 0) and self.matriz[i][j] <= (0, 255, 0):
                    #print("El color es negro", self.matriz[i][j])

                    # Verificando que las segundas y las terceras posiciones de las tuplas sean menores a 100.
                    if self.matriz[i][j][1] < 100 and self.matriz[i][j][2] < 100:
                        #print("El color es verde", self.matriz[i][j])
                        self.posiciones_verdes.append((i, j))

        #print(self.posiciones_verdes)


        #print("Posiciones: ", self.posiciones_negros)
        
        #print("Posiciones blancos", self.posiciones_blancos)

        # # Guardando la matriz de posición de los colores blancos en un archivo de texto.
        # with open("posiciones.txt", "w") as f:
        #     for i in range(len(self.posiciones)):
        #         f.write(str(self.posiciones[i]))
        #         f.write("\n")

        # #Guardando la matriz de colores blancos en un archivo de texto.
        # with open("colores_blancos.txt", "w") as f:
        #     for i in range(len(self.colores_blancos)):
        #         f.write(str(self.colores_blancos[i]))
        #         f.write("\n")

        # # Guardando la matriz original en un archivo de texto.
        # with open("matriz_original.txt", "w") as f:
        #     for i in range(len(self.matriz)):
        #         f.write(str(self.matriz[i]))
        #         f.write("\n")
            
        #     f.close()

    def result(self, s, a):
        pass

    def goalTest(self, s):
        # Si el estado actual es igual al estado meta, entonces se ha llegado a la meta.
        pass

    def pathCost(self, c, s, a, sd):
        pass