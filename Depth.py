from frame import * # Importando el módulo frame.py
import queue # Importando la librería queue para el algoritmo.
import Graph as g # Importando el módulo Graph.py

class Depth(FrameWork): 
    def __init__(self, matriz, blanco_pos, rojo_pos, negro_pos, verde_pos, verde, blanco, rojo, negro): # Recibiendo las listas de pixeles.
        self.matriz = matriz
        self.verdep = verde_pos
        self.blancop = blanco_pos
        self.rojop = rojo_pos
        self.negrop = negro_pos
        self.verde = verde
        self.blanco = blanco
        self.rojo = rojo
        self.negro = negro
        self.grafo = 0 # Diccionario para guardar el grafo.

        # Obteniendo el nodo inicial.
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                if self.matriz[i][j] in self.rojo:
                    self.start = (i, j)
        
        # Obteniendo el nodo final.
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                if self.matriz[i][j] in self.verde:
                    self.final = (i, j)

        self.dfs() # Llamando al algoritmo.

    # # Método action.
    # def action(self, s):
    #     if s == "L":
    #         return 1
    #     if s == "R":
    #         return 1
    #     if s == "U":
    #         return 1
    #     if s == "D":
    #         return 1
    
    # # Método result.
    # def result(self, s, moves):
        
    #     # Recorrer la matriz para encontrar el pixel rojo.
    #     for i in range(len(s)):
    #         for j in range(len(s[i])):
    #             #print(self.matriz[i][j] in self.rojo)
    #             if s[i][j] in self.rojo: #Encontrando el inicio.
    #                 #print("Encontrado: ", s[i][j])
    #                 start = (i, j)
        
    #     i = start[0] # Asignando el valor de start a i.
    #     j = start[1] # Asignando el valor de 0 a j.

    #     for move in moves:
    #         if move == "L":
    #             i -= self.action("L")

    #         elif move == "R":
    #             i += self.action("R")

    #         elif move == "U":
    #             j -= self.action("U")

    #         elif move == "D":
    #             j += self.action("D")
        

    #     # Verificando que el índice no se salga de la matriz.
    #     if not(0 <= i < len(s[0]) and 0 <= j < len(s)):
    #         return False
    #     elif self.matriz[i][j] in self.negro:
    #         #print("Found: " + moves)
    #         #printMaze(self.matriz, moves)
    #         return False
    #     return True

    # # Método goalTest.
    # def goalTest(self, s, moves):

    #     # Recorrer la matriz para encontrar el pixel rojo.
    #     for i in range(len(s)):
    #         for j in range(len(s[i])):
    #             #print(self.matriz[i][j] in self.rojo)
    #             if s[i][j] in self.rojo: #Encontrando el inicio.
    #                 #print("Encontrado: ")
    #                 start = (i, j)

    #     i = start[0] # Asignando el valor de start a i.
    #     j = start[1] # Asignando el valor de 0 a j.

    #     for move in moves:
    #         if move == "L":
    #             i -= self.action("L")

    #         elif move == "R":
    #             i += self.action("R")

    #         elif move == "U":
    #             j -= self.action("U")

    #         elif move == "D":
    #             j += self.action("D")

    #     #print(self.matriz[i][j] == (254, 0, 0))
    #     # Verificando que el color verde se encuentre en la matriz original.
    #     #print(i, j)
    #     if s[i][j] in self.verde:
    #         print("Verde: ", s[i][j])
    #         return True
        
    #     return False

    def dfs(self):
        visited = set() # Conjunto de nodos visitados.
        dfs_transversal = list() # Lista de nodos recorridos.

        edges = [] # Lista de aristas.

        # Contando el número de nodos de la matriz.
        nodes = 0
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                nodes += 1

        # Convertir la matriz en un grafo.
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                edges.append((i, j))

        # Creando el grafo.
        self.grafo = g.Graph(edges, nodes)

        print("Grafo: ", self.grafo.printGraph())

        #grafo.printGraph() # Imprimiendo el grafo.
        #print("Grafo: ", grafo)