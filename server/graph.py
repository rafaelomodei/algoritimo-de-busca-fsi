from typing import Deque

from collections import defaultdict
from typing import Tuple
from cell import Cell

class Graph(object):
    """Implementação basica de um grafo"""
    def __init__(self: Deque[Cell], edges: list, directed: bool = False):
        """Inicializa as estruturas base do grafo."""
        self.adjacent: defaultdict[Deque[Cell], set] = defaultdict(set)
        self.directed = directed
        self.addEdges(edges)
    
    def getVertices(self):
        """ Retorna a lista de vértices do grafo. """
        return list(self.adjacent.keys())
    
    def getEdges(self):
        """ Retorna a lista de edges do grafo. """
        return [(cell, vertice) for cell in self.adjacent.keys() for vertice in self.adjacent[cell]]
    
    def addEdges(self, edges: list):
        """ Adiciona edges ao grafo. """
        for cell, vertice in edges:
            self.addBow(cell, vertice)


    def addBow(self, cell: Cell, vertice: Tuple):
        """ Adiciona uma ligação (arco) entre os nodos 'u' e 'v'. """
        self.adjacent[cell].add(vertice)
        # Se o grafo é não-direcionado, precisamos adicionar arcos nos dois sentidos.
        if not self.directed:
            self.adjacent[vertice].add(cell)


    def hasEdges(self, cell: Cell, vertice: Tuple):
        """ Existe uma aresta entre os vértices 'u' e 'v'? """
        return cell in self.adjacent and vertice in self.adjacent[cell]


    def __len__(self):
        return len(self.adjacent)


    def __str__(self):
        for adj in self.adjacent:
            print(adj.terrain)
        return '{}'.format(dict(self.adjacent))


    def __getitem__(self, vertice: Tuple):
        return self.adjacent[vertice]
