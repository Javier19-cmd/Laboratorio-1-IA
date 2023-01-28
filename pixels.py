import Breath as br # Importando el módulo Breath.py
import Depth as dp # Importando el módulo Depth.py
import AStar as ast # Importando el módulo AStar.py

class Pixels(object): 
    def __init__(self, matriz):
        self.matriz = matriz

        self.posiciones_blancos = [] # Posiciones en donde se encuentran los colores blancos.

        self.posiciones_negros = [] # Posiciones en donde se encuentran los colores negros.

        self.posiciones_verdes = [] # Posiciones en donde se encuentran los colores verdes.
        
        self.color_temporal = []

        # Matrices de colores.
        self.colores_blancos = []
        self.colores_rojos = []
        self.colores_negros = []
        self.colores_verdes = []

        # Creando una matriz con todas las posiciones de la matriz original.
        self.matriz_posiciones = []

        self.posiciones_rojos = [] # Posiciones en donde se encuentran los colores rojos.
        self.rojo = [] # Guardando los rojos temporales.
        self.final = [] # Lista que almacenará los colores rojos que se encuentren en la matriz.
        self.buscar = () # Variable que almacenará el color rojo que se encuentre en la matriz.

        self.estado_inicial = () # Estado inicial del agente.

        # Creando una lista temporal para guardar los estados.
        self.lista_temporal = []

        self.distancias = [] # Lista que almacenará las distancias entre los estados.

        self.meta = () # Estado meta del agente.

        self.posf = () # Posición final del agente.

        self.camino_i = [] # Lista que almacenará el camino inicial.

        self.antiguo = [] # Estado antiguo del movimiento.

        self.start = () # Estado inicial del agente.

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
                        #print("Color rojo", self.matriz[i][j])
                        self.posiciones_rojos.append((i, j))
                        self.colores_rojos.append(self.matriz[i][j])
                        self.matriz_posiciones.append((i, j))

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
                        self.colores_blancos.append(self.matriz[i][j])
                        self.matriz_posiciones.append((i, j))

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
                        self.colores_negros.append(self.matriz[i][j])
                        self.matriz_posiciones.append((i, j))
        
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
                        self.colores_verdes.append(self.matriz[i][j])
                        self.matriz_posiciones.append((i, j))

        #print(self.posiciones_verdes)

        #print("Posiciones: ", self.posiciones_negros)
        
        #print("Posiciones blancos", self.posiciones_blancos)

        # Definiendo el estado inicial del agente.
        self.estado_inicial = self.posiciones_rojos[0]

        # Realizando la búsqueda de la solución. La solución es la posición más cercana al color verde.
        #self.solucion = self.busqueda_solucion(self.estado_inicial, self.posiciones_verdes)

        #print(self.posiciones_verdes)
        #print("Posiciones negros: ", self.posiciones_negros)
        #print(self.estado_inicial, self.posiciones_verdes)

        # for i in range(len(self.posiciones_verdes)):
        #     self.solucion = self.busqueda_meta(self.estado_inicial, self.posiciones_verdes[i], self.posiciones_verdes)

        #print(self.distancias)
        # Detectando cual es la distancia más pequeña y obteniendo el estado inicial.
        for i in range(len(self.distancias)):
            if self.distancias[i] == min(self.distancias):
                # Encontrando la posición del pixel verde en la lista temporal.
                self.posf = self.distancias.index(min(self.distancias))
        
        # Sacando las posiciones del pixel verde.
        #print("Posición: ", self.posf)
        #self.meta = self.posiciones_verdes[self.posf]
        #print(self.posiciones_verdes)
        # print("Meta: ", self.meta)

        # # Imprimiendo el estado inicial.
        # print("Estado inicial: ", self.estado_inicial)

        #print("Distancias: ", self.distancias)

        # Hay que encontrar los pixeles blancos que sirvan de camino para llegar a la meta.
        #print("Posiciones blancos: ", self.posiciones_blancos)
        for i in range(len(self.posiciones_blancos)):
            # print("Camino: ", self.posiciones_blancos[i])
            # print("Meta: ", self.meta)
            # print("Estado inicial: ", self.estado_inicial)
            pass

        #Obteniendo un pixel blanco que sirva de camino.
        for i in range(len(self.posiciones_blancos)):
            #print("Camino: ", self.posiciones_blancos[i])
            #print("Meta: ", self.meta)
            #print("Estado inicial: ", self.estado_inicial)
            # Verificando esté en cualquier posición cercana al estado inicial.
            if self.posiciones_blancos[i][0] == self.estado_inicial[0] or self.posiciones_blancos[i][0] == self.estado_inicial[0] + 1 or self.posiciones_blancos[i][0] == self.estado_inicial[0] - 1:
                if self.posiciones_blancos[i][1] == self.estado_inicial[1] or self.posiciones_blancos[i][1] == self.estado_inicial[1] + 1 or self.posiciones_blancos[i][1] == self.estado_inicial[1] - 1:
                    #print("Camino: ", self.posiciones_blancos[i])
                    #print("Meta: ", self.meta)
                    #print("Estado inicial: ", self.estado_inicial)
                    #print("Posición: ", i)
                    self.camino_i.append(self.posiciones_blancos[i])
                    #print("Camino: ", self.camino)
            
        #print("Camino: ", self.camino_i)

        br.Breath(self.matriz, self.posiciones_blancos, self.posiciones_rojos, self.posiciones_negros, self.posiciones_verdes, self.colores_verdes, self.colores_blancos, self.colores_rojos, self.colores_negros)
        
        # Sacando copias de todas las listas para poder utilizarlas en la búsqueda de la solución.
        self.posiciones_blancos_copia = self.posiciones_blancos.copy()
        self.posiciones_rojos_copia = self.posiciones_rojos.copy()
        self.posiciones_verdes_copia = self.posiciones_verdes.copy()
        self.posiciones_negros_copia = self.posiciones_negros.copy()
        self.colores_blancos_copia = self.colores_blancos.copy()
        self.colores_rojos_copia = self.colores_rojos.copy()
        self.colores_verdes_copia = self.colores_verdes.copy()
        self.colores_negros_copia = self.colores_negros.copy()
        
        dp.Depth(self.matriz, self.posiciones_blancos, self.posiciones_rojos, self.posiciones_negros, self.posiciones_verdes, self.colores_verdes, self.colores_blancos, self.colores_rojos, self.colores_negros)
        
        ast.AStart(self.matriz, self.posiciones_blancos_copia, self.posiciones_rojos_copia, self.posiciones_negros_copia, self.posiciones_verdes_copia, self.colores_verdes_copia, self.colores_blancos_copia, self.colores_rojos_copia, self.colores_negros_copia)