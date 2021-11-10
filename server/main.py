# import random
# from linkedList import LinkedList
from typing import Deque
from collections import deque 
import random 
from graph import Graph
from cell import Cell
from terrain import TypeTerrain
from breadthFirstSearch import bfs


def main():

    # edges = [('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'B'), ('C', 'E'), ('D', 'A'), ('E', 'B')]


    edges: Deque[Cell] = deque()
    # for i in range(0, 3):

    #     edges: Deque[str] = deque()
    #     lastCell = Cell(0, TypeTerrain.plain)
    for i in range(0, 16):
        newCell = Cell(i+1, random.choice(list(TypeTerrain)))
        # currenCell = (lastCell, newCell)
        # lastCell = currenCell
        edges.append(newCell)

    # edges = [('A', 'B'), ('A', 'D'), ('B', 'E'), ('D', 'E'), ('E', 'C'), ('C', 'A')]
    # edges = [(edges[0], edges[1], edges[4]),
    #          (edges[1], edges[0], edges[2], edges[5]),
    #          (edges[2], edges[1], edges[3], edges[6]),
    #          (edges[3], edges[2], edges[7]),

    #          (edges[4], edges[0], edges[5], edges[8]),
    #          (edges[5], edges[4], edges[1], edges[6], edges[9]),
    #          (edges[6], edges[5], edges[2], edges[7], edges[10]),
    #          (edges[7], edges[6], edges[3], edges[11]),

    #          (edges[8], edges[4], edges[9], edges[12]),
    #          (edges[9], edges[8], edges[5], edges[10], edges[11]),
    #          (edges[10], edges[9], edges[6], edges[11], edges[14]),
    #          (edges[11], edges[10], edges[7], edges[15]),

    #          (edges[12], edges[8], edges[13]),
    #          (edges[13], edges[12], edges[9], edges[14]),
    #          (edges[14], edges[13], edges[10], edges[15]),
    #          (edges[15], edges[14], edges[11]),

    # ]
    for i in range(0, 16):
        print('edges: [ ', i, ' ] | ',  edges[i].data, ', ', edges[i].terrain)

    start: Cell = edges[0]
    end: Cell = edges[15]

    print('start: ', start)
    print('end: ', end)


    newEdges = [(edges[0], edges[1]),
             (edges[0], edges[4]),

             (edges[1], edges[0]),
             (edges[1], edges[2]),
             (edges[1], edges[5]),

             (edges[2], edges[1]),
             (edges[2], edges[3]),
             (edges[2], edges[6]),

             (edges[3], edges[2]),
             (edges[3], edges[7]),

             (edges[4], edges[0]),
             (edges[4], edges[5]),
             (edges[4], edges[8]),

             (edges[5], edges[4]),
             (edges[5], edges[1]),
             (edges[5], edges[6]),
             (edges[5], edges[9]),

             (edges[6], edges[5]),
             (edges[6], edges[2]),
             (edges[6], edges[7]),
             (edges[6], edges[10]),

             (edges[7], edges[6]),
             (edges[7], edges[3]),
             (edges[7], edges[11]),

             (edges[8], edges[4]),
             (edges[8], edges[9]),
             (edges[8], edges[12]),

             (edges[9], edges[8]),
             (edges[9], edges[5]),
             (edges[9], edges[10]),
             (edges[9], edges[11]),

             (edges[10], edges[9]),
             (edges[10], edges[6]),
             (edges[10], edges[11]),
             (edges[10], edges[14]),

             (edges[11], edges[10]),
             (edges[11], edges[7]),
             (edges[11], edges[15]),

             (edges[12], edges[8]),
             (edges[12], edges[13]),

             (edges[13], edges[12]),
             (edges[13], edges[9]),
             (edges[13], edges[14]),

             (edges[14], edges[13]),
             (edges[14], edges[10]),
             (edges[14], edges[15]),

             (edges[15], edges[14]),
             (edges[15], edges[11]),

    ]

    print('Tamanho de edges: ', len(edges))
    i = 0
    for vertice in newEdges:
        print('edges: [ ', i, ' ] | ',  vertice[0].data, ', ', vertice[1].terrain)
        i = i + 1
    graph = Graph(newEdges)

    # aux = ""
    # for vertice in graph.adjacent:
    #     for cell in graph.adjacent[vertice]:
    #         if (vertice != aux):
    #             print('\n[ ', vertice.data ,' ] -> ', cell.data, end="")
    #         else:
    #             print(' -> ', cell.data, end="")
    #
    #          aux = vertice


    # graph = [ [1],           # Vizinhos do vértice 0.
    #       [2, 3],        # Vizinhos do vértice 1.
    #       [1, 4],        # Vizinhos do vértice 2.
    #       [0],           # Vizinhos do vértice 3.
    #       [1]            # Vizinhos do vértice 4.
    #     ]

    # grafo = {
    #       "Z" : [],
    #       "A" : ["B", "F"],
    #       "B" : ["E", "C", "A", "F"],
    #       "C" : ["F", "E", "D", "B"],
    #       "D" : ["E", "C"],
    #       "E" : ["F", "D", "C", "B"],
    #       "F" : ["E", "C", "B", "A"]
    #     }

    # grafo = { "A" : ["B"],
    #       "B" : ["C", "D"],
    #       "C" : ["B", "E"],
    #       "D" : ["A"],
    #       "E" : ["B"]
    #     }

    # grafo = { "A" : ["B", "D"],
    #       "B" : ["E"],
    #       "C" : [],
    #       "D" : ["E"],
    #       "E" : ["C"]
    #     }

    print(bfs(graph, start, end))

    # print(bfs(graph, start, end))



if __name__ == "__main__":
    main()