from frame import * # Importando el módulo frame.py

class Breath(FrameWork): 
    def __init__(self, blanco, rojo, negro): # Recibiendo las listas de pixeles.
        self.blanco = blanco
        self.rojo = rojo
        self.negro = negro

        self.Algoritmo() # Llamando al algoritmo.

    # Método action.
    def action(self, s):
        pass
    
    # Método result.
    def result(self, s, a):
        pass

    # Método goalTest.
    def goalTest(self, s):
        pass

    def Algoritmo(self): 
        print("Dentro del algoritmo")
