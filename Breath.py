from frame import * # Importando el módulo frame.py
import queue # Importando la librería queue para el algoritmo.
class Breath(FrameWork): 
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
        self.visitas = [] # Lista para guardar los nodos visitados.
        self.cola = queue.Queue() # Cola para guardar los nodos visitados.

        self.Algoritmo() # Llamando al algoritmo.

    # Método action.
    def action(self, s):
        x, y = s # Asignando los valores de s a x e y.

        movs = [] # Lista para guardar los movimientos.

        if ((x, y + 1) in self.blancop) or ((x, y + 1) in self.verdep) or ((x, y + 1) in self.rojop):
            movs.append((x, y + 1)) # Movimiento hacia abajo.
        elif ((x + 1, y) in self.blancop) or ((x + 1, y) in self.verdep) or ((x + 1, y) in self.rojop):
            movs.append((x + 1, y))
        elif ((x, y - 1) in self.blancop) or ((x, y - 1) in self.verdep) or ((x, y - 1) in self.rojop):
            movs.append((x, y - 1))
        elif ((x - 1, y) in self.blancop) or ((x - 1, y) in self.verdep) or ((x - 1, y) in self.rojop):
            movs.append((x - 1, y))
        
        return movs
        
    
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
    #     if not(0 <= i < len(self.matriz[0]) and 0 <= j < len(self.matriz)):
    #         return False
    #     elif self.matriz[i][j] in self.negro:
    #         #print("Found: " + moves)
    #         #printMaze(self.matriz, moves)
    #         return False

    #     # Ingresando los nodos visitados a la lista visitas.
    #     self.visitas.append((i, j))
        
    #     # Si el nodo no se encuentra en la lista visitas, se agrega.
    #     if (i, j) not in self.visitas:
    #         self.visitas.append((i, j))
    #     else:
    #         return False

    #     return True

    # Método goalTest.
    def goalTest(self, s):

        i, j = s # Asignando los valores de s a i y j.
        
        #print(self.matriz[i][j] == (254, 0, 0))
        # Verificando que el color verde se encuentre en la matriz original.
        #print(i, j)
        # Verificando que el índice no se salga de la matriz.
        if not(0 <= i < len(self.matriz[0]) and 0 <= j < len(self.matriz)):
            return s
        elif self.matriz[i][j] in self.verde:
            #printMaze(self.matriz, moves)
            #print("Gola")
            return True

        # # Verificando que los nodos visitados no se encuentren en la lista visitas.
        # if (i, j) not in self.visitas:
        #     self.visitas.append((i, j))
        # else: 
        #     return False
        
        return False

    def Algoritmo(self): 
        #print(inicioc)

        # cola = queue.Queue() # Creando la cola.
        # cola.put(ini) # Agregando el primer elemento a la cola.
        # inicioc = self.rojo[-1] # Obteniendo el último elemento de la lista de pixeles rojos.
        # add = "" # Variable que almacenará el camino.

        # res = queue.Queue() # Lista que almacenará el camino.

        # while not self.goalTest(inicioc, add):
            
        #     col = cola.get() # Obteniendo el primer elemento de la cola.

        #     for j in ["L", "R", "U", "D"]:
        #         add = col + j
        ini = self.rojop.pop(0) # Obteniendo el último elemento de la lista de pixeles rojos.

        print("Inicio: ", ini)
        #print("Matriz", self.matriz)

        # Recorriendo la matriz para encontrar el pixel rojo.
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                #print(self.matriz[i][j] in self.rojo)
                if self.matriz[i][j] in self.rojo:
                    #print("Encontrado: ", self.matriz[i][j], i, j)
                    #start = (i, j)
                    pass
        
        self.cola.put(ini) # Agregando el primer elemento a la cola.
        self.visitas.append(ini) # Agregando el primer elemento a la lista de visitas.

        while True: 
            if self.cola.empty() == False:
                #print("No se encontró un camino.")

                
                sacar = self.cola.get()
                if self.goalTest(sacar): 
                    return sacar
                acciones = self.action(sacar)

                for accion in acciones:
                    if accion not in self.visitas:
                        #print("Agregando: ", accion)
                        self.cola.put(accion)
                        self.visitas.append(accion)
            else:
                return False
            
    
        