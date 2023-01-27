# Una clase para representar un objeto graph
class Graph:
    # Constructor
    def __init__(self, edges, n):
        # asigna memoria para la lista de adyacencia
        self.adjList = [[] for _ in range(n)]
        # Lista de conexiones.
        self.connections = [[] for _ in range(n)]
 
        #print("Edges: ", edges)

        # Revisando los vecinos de cada nodo.
        for edge in edges: 
            #print("Edge: ", edge)
            self.adjList[edge[0]].append(edge[1])
            self.adjList[edge[1]].append(edge[0])

        #print("AdjList: ", self.adjList)

    #Print the graph.
    def printGraph(self):
        for i in range(len(self.adjList)):
            print("Nodo: ", i, " -> ", self.adjList[i])
