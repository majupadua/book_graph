import sys
from collections import defaultdict, deque

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)  # Usando defaultdict para listas

    def printSolution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(node, "\t", dist[node])

    def minDistance(self, dist, sptSet):
        min_distance = sys.maxsize
        min_index = -1
        for u in range(self.V):
            if dist[u] < min_distance and not sptSet[u]:
                min_distance = dist[u]
                min_index = u
        return min_index

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for _ in range(self.V):
            x = self.minDistance(dist, sptSet)
            sptSet[x] = True
            
            for y, weight in self.graph[x]:  # Percorre a lista de adjacência
                if not sptSet[y] and dist[y] > dist[x] + weight:
                    dist[y] = dist[x] + weight

        self.printSolution(dist)

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))  # Adiciona a aresta na lista de adjacência
        self.graph[v].append((u, weight))  # Se o grafo for não direcionado

if __name__ == "__main__":
    g = Graph(5)
    
    # Adicionando as arestas com os respectivos pesos
    g.add_edge(0, 1, 1)
    g.add_edge(0, 4, 1)
    g.add_edge(1, 2, 1)
    g.add_edge(1, 3, 2)
    g.add_edge(2, 3, 4)
    g.add_edge(2, 4, 2)
    g.add_edge(3, 0, 3)
    g.add_edge(4, 0, 2)
    g.add_edge(3, 4, 1)

    g.dijkstra(src=0)
