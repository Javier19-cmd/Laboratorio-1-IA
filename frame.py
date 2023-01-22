"""
Nombre: Javier Sebastián Valle Balsells
Carnet: 20159
Sección de clase: 20
Clase FrameWork: Esta clase se encarga de crear la matriz que se utilizará para el frame y para definir las acciones, stepCost(s, a, s'), etc.
Se tiene que usar el paradigma de programación orientada a objetos.
"""
import math as m # Importando la librería math para poder usar la función sqrt.

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

        self.estado_inicial = () # Estado inicial del agente.

        # Creando una lista temporal para guardar los estados.
        self.lista_temporal = []

        self.distancias = [] # Lista que almacenará las distancias entre los estados.

        self.posf = () # Posición final del agente.

        self.action() # Definiendo las acciones que tomará el agente para llegar a la meta.

    def action(self): # Definiendo las acciones que tomará el agente para llegar a la meta.

        # # Buscando el color rojo en la matriz.
        # for i in range(len(self.matriz)):
        #     for j in range(len(self.matriz[i])):
        #         # Verificando que cada color empiece con 235, 0, 0 y termine con 255, 0, 0 y que no tenga colores intermedios.
        #         if self.matriz[i][j] >= (230, 0, 0) and self.matriz[i][j] <= (255, 0, 0):
        #             #print("El color es rojo")
        #             #print("Posición: ", i, j)
        #             self.rojo.append((self.matriz[i][j]))
        
        # # Detectando que las segundas y las terceras posiciones de las tuplas sean menores a 100.
        # for i in range(len(self.rojo)):
        #     if self.rojo[i][1] < 100 and self.rojo[i][2] < 100:
        #         #print("El color es rojo")
        #         #print("Posición: ", i, j)
        #         #self.posiciones.append((i, j))
        #         self.final.append(self.rojo[i])

        # #print("Final", self.final)
        
        # # Almacenando cada color rojo de la lista final en una variable temporal para buscarlo en la lista matriz.
        # for i in range(len(self.final)):
        #     self.a = self.final[i]
        #     #print("A", self.a)

        # # Buscando cada color rojo en la lista matriz.
        # for i in range(len(self.matriz)):
        #     for j in range(len(self.matriz[i])):
        #         if self.matriz[i][j] == self.a:
        #             #print("El color es rojo")
        #             #print("Posición: ", i, j)
        #             self.posiciones_rojos.append((i, j))

        # Buscando el color rojo en la matriz.
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                # Verificando que cada color empiece con 235, 0, 0 y termine con 255, 0, 0 y que no tenga colores intermedios.
                if self.matriz[i][j] >= (230, 0, 0) and self.matriz[i][j] <= (255, 0, 0):
                    # #print("El color es rojo")
                    # #print("Posición: ", i, j)
                    # self.rojo.append((self.matriz[i][j]))
                    if self.matriz[i][j][1] < 100 and self.matriz[i][j][2] < 100:
                        #print("El color es rojo")
                        #print("Posición: ", i, j)
                        #self.posiciones.append((i, j))
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
        
        # Recorriendo la matriz e identificando los colores que sean verdes.
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                # Verificar si el color esté en el rango de los colores negros.
                if self.matriz[i][j] >= (0, 100, 0) and self.matriz[i][j] <= (0, 255, 0):
                    #print("El color es verde", self.matriz[i][j])

                    # Verificando que las segundas y las terceras posiciones de las tuplas sean menores a 100.
                    if self.matriz[i][j][0] < 100 and self.matriz[i][j][2] < 100:
                        #print("El color es verde", self.matriz[i][j])
                        #print("Posición: ", i, j)
                        self.posiciones_verdes.append((i, j))

        #print(self.posiciones_verdes)


        #print("Posiciones: ", self.posiciones_negros)
        
        #print("Posiciones blancos", self.posiciones_blancos)

        # Definiendo el estado inicial del agente.
        self.estado_inicial = self.posiciones_rojos[0]

        # Realizando la búsqueda de la solución. La solución es la posición más cercana al color verde.
        #self.solucion = self.busqueda_solucion(self.estado_inicial, self.posiciones_verdes)

        #print(self.posiciones_verdes)
        #print("Posiciones negros: ", self.posiciones_negros)

        for i in range(len(self.posiciones_verdes)):
            self.solucion = self.busqueda_meta(self.estado_inicial, self.posiciones_verdes[i], self.posiciones_verdes)

        #print(self.distancias)
        # Detectando cual es la distancia más pequeña y obteniendo el estado inicial.
        for i in range(len(self.distancias)):
            if self.distancias[i] == min(self.distancias):
                # Encontrando la posición del pixel verde en la lista temporal.
                self.posf = self.distancias.index(min(self.distancias))
        
        # Sacando las posiciones del pixel verde.
        print("Posición: ", self.posf)
        meta = self.lista_temporal[self.posf]
        print("Meta: ", meta)

    def busqueda_meta(self, estado_inicial, estado_final, posiciones_verdes): # Este método se encarga de buscar la solución.
        # Creando una lista para guardar las distancias entre el estado inicial y el estado final.
        #distancias = []
        
        # print("Estado inicial: ", estado_inicial)
        # print("Estado final: ", estado_final)

        # Detectando cual estado es el más cercano al estado final.
        #print("Estado inicial: ", estado_inicial)
        #print("Estado final: ", estado_final)

        # Calculando la distancia entre el estado inicial y el estado final.
        distancia = m.sqrt((estado_final[0] - estado_inicial[0])**2 + (estado_final[1] - estado_inicial[1])**2)

        self.distancias.append(distancia) # Guardando la distancia en la lista de distancias.

        # Copiando la lista de posiciones de los puntos verdes en una lista temporal.
        self.lista_temporal = posiciones_verdes.copy()

        #print("Distancia: ", distancia)
        #print(self.distancias)


    def result(self, s, a): # s es el estado actual y a es la acción a realizar.
        # Devuelve el estado que resulta de realizar la acción a en el estado s.
        
        print("Estado actual: ", s)
        print("Acción a realizar: ", a)

        # Si la acción es moverse hacia arriba.
        if a == "arriba":
            print("Moverse hacia arriba")
            print("Posición: ", s[0], s[1])
            
            # print("Posición: ", s[0] - 1, s[1])
            # print("Posición: ", s[0] - 2, s[1])
            # print("Posición: ", s[0] - 3, s[1])
            # print("Posición: ", s[0] - 4, s[1])
            # print("Posición: ", s[0] - 5, s[1])
            # print("Posición: ", s[0] - 6, s[1])
            # print("Posición: ", s[0] - 7, s[1])
            # print("Posición: ", s[0] - 8, s[1])
            # print("Posición: ", s[0] - 9, s[1])
            # print("Posición: ", s[0] - 10, s[1])
            # print("Posición: ", s[0] - 11, s[1])
            # print("Posición: ", s[0] - 12, s[1])
            # print("Posición: ", s[0] - 13, s[1])
            # print("Posición: ", s[0] - 14, s[1])
            # print("Posición: ", s[0] - 15, s[1])
            # print("Posición: ", s[0] - 16, s[1])
            # print("Posición: ", s[0] - 17, s[1])
            # print("Posición: ", s[0] - 18, s[1])
            # print("Posición: ", s[0] - 19, s[1])
            # print("Posición: ", s[0] - 20, s[1])
            # print("Posición: ", s[0] - 21, s[1])
            # print("Posición: ", s[0] - 22, s[1])
            # print("Posición: ", s[0] - 23, s[1])
            # print("Posición: ", s[0] - 24, s[1])

        elif a == "abajo":
            print("Moverse hacia abajo")
            print("Posición: ", s[0], s[1])
        elif a == "izquierda":
            print("Moverse hacia la izquierda")
            print("Posición: ", s[0], s[1])
        elif a == "derecha":
            print("Moverse hacia la derecha")
            print("Posición: ", s[0], s[1])

    def goalTest(self, s):
        # Si el estado actual es igual al estado meta, entonces se ha llegado a la meta.
        pass

    def pathCost(self, c, s, a, sd):
        pass