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

    def action(self):
        pass
    
    def stepCost(self, s, a, sd):
        pass

    def result(self, s, a):
        pass

    def goalTest(self, s):
        pass

    def pathCost(self, c, s, a, sd):
        pass

    def value(self, s):
        pass