from frame import * # Importando el módulo frame.py
import queue # Importando la librería queue para el algoritmo.
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
        self.cola = [] # Cola para guardar los nodos visitados.
        self.visitas = set() # Lista para guardar los nodos visitados.

        self.Algoritmo() # Llamando al algoritmo.

    # Método action.
    def action(self, s):
        x, y = s # Asignando los valores de s a x e y.

        movs = [] # Lista para guardar los movimientos.

        if ((x, y + 1) in self.blancop) or ((x, y + 1) in self.verdep) or ((x, y + 1) in self.rojop):
            movs.append((x, y + 1)) # Movimiento hacia abajo.
        if ((x + 1, y) in self.blancop) or ((x + 1, y) in self.verdep) or ((x + 1, y) in self.rojop):
            movs.append((x + 1, y))
        if ((x, y - 1) in self.blancop) or ((x, y - 1) in self.verdep) or ((x, y - 1) in self.rojop):
            movs.append((x, y - 1))
        if ((x - 1, y) in self.blancop) or ((x - 1, y) in self.verdep) or ((x - 1, y) in self.rojop):
            movs.append((x - 1, y))
    
        return movs

    def result(self, s, a): # Método result.

        i, j = s # Asignando los valores de s a i y j.
        #print(a) # Asignando los valores de a a x e y.

        # Verificando que el índice no se salga de la matriz.
        if not(0 <= i < len(self.matriz[0]) and 0 <= j < len(self.matriz)):
            return False

        if a not in self.action(s):
            return False
        

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
            print("Objetivo encontrado", self.matriz[i][j])
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
        
        self.cola.append(ini) # Agregando el primer elemento a la cola.
        self.visitas.add(ini) # Agregando el primer elemento a la lista de visitas.
        

        while True: 
            if len(self.cola):
                #print("No se encontró un camino.")       
                sacar = self.cola.pop(0)
                #print("Sacando: ", sacar)
                
                if self.goalTest(sacar): # Verificando si el nodo es el objetivo. 
                    return sacar 
                acciones = self.action(sacar)
                
                #print(self.result(sacar, acciones))

                if self.result(sacar, acciones): # Verificando que no se desborde la búsqueda.
                    return 

                #print(acciones)
                for accion in acciones:
                    if accion not in self.visitas:
                        #print("Agregando: ", accion)
                        self.cola.append(accion)
                        self.visitas.add(accion)
                # print(self.visitas)
                # print(self.cola)
            else:
                return False
            
            #print("Sacando: ", sacar)
            # Ordenando el set de visitas.
            sorted(self.visitas)
            #print("Visitas: ", self.visitas)