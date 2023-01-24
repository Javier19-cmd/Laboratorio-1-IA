"""
Nombre: Javier Sebastián Valle Balsells
Carnet: 20159
Sección de clase: 20
Clase FrameWork: Esta clase se encarga de crear la matriz que se utilizará para el frame y para definir las acciones, stepCost(s, a, s'), etc.
Se tiene que usar el paradigma de programación orientada a objetos.
"""
import math as m # Importando la librería math para poder usar la función sqrt.
import queue # Importando la librería queue para poder usar la función PriorityQueue.

class FrameWork(object):
    def __init__(self, matriz):
        self.matriz = matriz

        self.posiciones_blancos = [] # Posiciones en donde se encuentran los colores blancos.

        self.posiciones_negros = [] # Posiciones en donde se encuentran los colores negros.

        self.posiciones_verdes = [] # Posiciones en donde se encuentran los colores verdes.
        
        self.color_temporal = []
        self.colores_blancos = []

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
                        print("Color rojo", self.matriz[i][j])
                        self.posiciones_rojos.append((i, j))
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

        for i in range(len(self.posiciones_verdes)):
            self.solucion = self.busqueda_meta(self.estado_inicial, self.posiciones_verdes[i], self.posiciones_verdes)

        #print(self.distancias)
        # Detectando cual es la distancia más pequeña y obteniendo el estado inicial.
        for i in range(len(self.distancias)):
            if self.distancias[i] == min(self.distancias):
                # Encontrando la posición del pixel verde en la lista temporal.
                self.posf = self.distancias.index(min(self.distancias))
        
        # Sacando las posiciones del pixel verde.
        #print("Posición: ", self.posf)
        self.meta = self.posiciones_verdes[self.posf]
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

        # Algoritmo BFS.
        cola = queue.Queue()
        #cola.put(self.camino_i[0]) # Estado inicial del laberinto. (Pixel de color blanco)
        add = self.camino_i[0] # Estado actual.
        cola.put(add) # Estado inicial del laberinto. (Pixel de color blanco)
    
        while True: 
            add = cola.get()
            
            a = self.goalTest(add)

            if a == True:
                print("Meta")
                break


        # while not self.goalTest(add):
        #     add = cola.get() # Obteniendo el primer elemento de la cola.

        #     print(add)
        
            # # Buscando los vecinos del estado actual en la lista de blancos.
            # for a in range(len(self.posiciones_blancos)):
            #     if self.posiciones_blancos[a][0] == add[0] or self.posiciones_blancos[a][0] == add[0] + 1 or self.posiciones_blancos[a][0] == add[0] - 1:
            #         if self.posiciones_blancos[a][1] == add[1] or self.posiciones_blancos[a][1] == add[1] + 1 or self.posiciones_blancos[a][1] == add[1] - 1:
            #             cola.put(self.posiciones_blancos[a])
            #             antiguos = add

            #             #print("Estado anterior: ", antiguos)

            #             #print("Estado actual: ", self.camino_i[a])

            #             #self.valido(self.camino_i[a], self.meta)

            #             # Verificando que el siguiente pixel no sea negro.
            #             if self.valido(add):
            #                 cola.put(self.posiciones_blancos[a])




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


    def valido(self, s):
        
        #start = 0
        for x, pos in enumerate(self.matriz):
            # Si la posición actual es igual a la posición del pixel rojo, entonces se guarda la posición.
            if pos in self.posiciones_rojos:
                self.start = x

        i = self.start
        j = 0

       # print(s)

        # print("S: ", type(s))
        # print("Matriz: ", self.matriz_posiciones[0])

        for m in s:
            # Si el indice 0 de la posición antigua es menor al indice 0 de la posición actual, entonces se mueve hacia arriba.
            if self.matriz_posiciones[m][0] < s[0]:
                i = s[0] - 1
                #print("Reducción en x: ", i)
                return (i, j)
            # Si el indice 0 de la posición antigua es mayor al indice 0 de la posición actual, entonces se mueve hacia abajo.
            elif self.matriz_posiciones[m][1] > s[0]:
                i = s[0] + 1
                #print("Aumento en x: ", i)
                return (i, j)
            # Si el indice 1 de la posición antigua es menor al indice 1 de la posición actual, entonces se mueve hacia la izquierda.
            elif self.matriz_posiciones[m][0] < s[1]:
                j = s[1] - 1
                #print("Reducción en y: ", j)
                return (i, j)
            # Si el indice 1 de la posición antigua es mayor al indice 1 de la posición actual, entonces se mueve hacia la derecha.
            elif self.matriz_posiciones[m][1] > s[1]:
                j = s[1] + 1
                return (i, j)
                #print("Aumento en y: ", j)

        
        return (i, j)

    def goalTest(self, s):
        # Si el estado actual es igual al estado meta, entonces se ha llegado a la meta.
        for x in range(len(self.matriz)):
            for y in range(len(self.matriz[x])):
                #print("Estado actual: ", s)
                if (s in self.posiciones_blancos) and (self.estado_inicial in self.posiciones_rojos):
                    start = s

        # Índices de la posición actual.
        i = start

        #print("Primer punto blanco: ", i)
        
        # Buscar los puntos que están cerca del punto blanco.
        for x in range(len(self.matriz)):
            for y in range(len(self.matriz[x])):
                if (x, y) in self.posiciones_blancos:
                    #print("Punto blanco: ", (x, y))

                    if ((x + 1, y) in self.posiciones_blancos) and ((x + 1, y) > i):
                        #print("Punto blanco: ", (x + 1, y))
                        # print("Punto blanco: ", (x + 1, y))
                        # print("I: ", i)
                        i = (x + 1, y)
                        #print("I: ", i)

                        # Verificando que el siguiente punto sea verde.
                        if (x + 1, y) in self.posiciones_verdes:
                            print("Punto verde: ", i)
                            return True

                    if ((x - 1, y) in self.posiciones_blancos) and ((x - 1, y) > i):
                        #print("Punto blanco: ", (x - 1, y))
                        # print("Punto blanco: ", (x - 1, y))
                        # print("I: ", i)
                        i = (x - 1, y)
                        #print("I: ", i)
                        
                        # Verificando que el siguiente punto sea verde.
                        if (x - 1, y) in self.posiciones_verdes:
                            print("Punto verde: ", i)
                            return True
                            
                    if ((x, y + 1) in self.posiciones_blancos) and ((x, y + 1) > i):
                        #print("Punto blanco: ", (x, y + 1))
                        # print("Punto blanco: ", (x, y + 1))
                        # print("I: ", i)
                        i = (x, y + 1)
                        
                        # Verificando que el siguiente punto sea verde.
                        if (x, y + 1) in self.posiciones_verdes:
                            print("Punto verde: ", i)
                            return True

                    if ((x, y - 1) in self.posiciones_blancos) and ((x, y - 1) < i):
                        #print("Punto blanco: ", (x, y - 1))
                        # print("Punto blanco: ", (x, y - 1))
                        # print("I: ", i)
                        i = (x, y - 1)
                        #print("I: ", i)
                        

                        # Verificando que el siguiente punto sea verde.
                        if (x, y - 1) in self.posiciones_verdes:
                            
                            print("Punto verde: ", i)
                            return True


                    

        # for m in s: 
        #     # Si el indice 0 de la posición antigua es menor al indice 0 de la posición actual, entonces se mueve hacia arriba.
        #     if antiguo[0] < s[0]:
        #         i -= 1
        #     # Si el indice 0 de la posición antigua es mayor al indice 0 de la posición actual, entonces se mueve hacia abajo.
        #     elif antiguo[0] > s[0]:
        #         i += 1
        #     # Si el indice 1 de la posición antigua es menor al indice 1 de la posición actual, entonces se mueve hacia la izquierda.
        #     elif antiguo[1] < s[1]:
        #         j -= 1
        #     # Si el indice 1 de la posición antigua es mayor al indice 1 de la posición actual, entonces se mueve hacia la derecha.
        #     elif antiguo[1] > s[1]:
        #         j += 1

        # if self.matriz[i][j] in self.posiciones_verdes: # Si la posición está en la lista de las posiciones verdes, entonces se devuelve verde.
        #     #print("Se ha llegado a la meta.")
        #     return True
        # elif self.matriz[i][j] not in self.posiciones_verdes:
        #     #print("No se ha llegado a la meta.")
        #     return False
        
        return True

    # Método que detecta el stepcots.
    def step_cost(self, s, a, ss):
        pass