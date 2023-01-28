"""
Nombre: Javier Valle
Carnet: 20159
"""
from frame import * # Importando el módulo frame.py
from math import sqrt

class AStart(FrameWork):
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

            self.D = 1 # Longitud de cada nodo.
            self.D2 = 1.4142135623730951 # Longitud entre cada nodo.

            self.open_list = set() # Lista para guardar los nodos visitados, pero que los vecinos no se han inspeccionado aún.
            self.closed_list = set() # Lista para guardar los nodos visitados.

            self.algoritmo() # Llamando al algoritmo.

        def manhattan(self, s): # Heurística de ruta máxima.
            final = self.verdep.pop(0) # Obteniendo el nodo final.
            x, y = s # Obteniendo los valores de s.

            return max(abs(x - final[0]), abs(y - final[1]))

        def euClides(self, s): # Heuristica de euclides.
            final = self.verdep.pop(0)
            x, y = s

            h = sqrt((x - final[0])**2 + (y - final[1])**2)

            return h

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

            # Verificando que los puntos de a no sean puntos negros.
            if a in self.negrop:
                return False

        def cost(self, s, a, s2): # Método cost.
            pass


        def algoritmo(self):
            # Obteniendo el nodo inicial.
            ini = self.rojop.pop(0)
            col = self.rojo.pop(0)

            self.open_list.add(ini) # Agregando el nodo inicial a la lista de nodos visitados.

            # # Buscando el nodo inicial en la matriz original.
            # for i in range(len(self.matriz)):
            #     for j in range(len(self.matriz[0])):
            #         if self.matriz[i][j] in self.rojo:
            #             ini = (i, j)
            #             print(ini, self.matriz[i][j])

            # Mientras open_list no esté vacía, encontrar el nodo con el menor valor de f.
            while len(self.open_list) > 0:
                # Encuentra el nodo con el menor valor de f.
                valor = min(self.open_list, key=lambda s: s[1])

                # Quitando el nodo del open_list.
                self.open_list.remove(valor)

                # Agregando el nodo al closed_list.
                self.closed_list.add(valor)

                #Generando los vecinos.
                vecinos = self.action(valor)

                for vecino in vecinos:

                    if vecino in self.closed_list: # Verificnado que el vecino esté en la lista cerrada.
                        continue

                    if vecino not in self.open_list: # Verificando que el vecino no esté en la lista abierta.
                        self.open_list.add(vecino)

                    print(vecino)
