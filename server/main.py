# import random
# from linkedList import LinkedList
from typing import Deque
from collections import deque 
import random 
from graph import Graph
from cell import Cell
from terrain import TypeTerrain
from breadthFirstSearch import bfs
from greedySearch import greedySearch
from aStar import aStar



def main():

    # edges = [('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'B'), ('C', 'E'), ('D', 'A'), ('E', 'B')]
    #a = posiçãox posiçãoy, terreno

    cellList: Deque[Cell] = deque()
    # for i in range(0, 3):

    #     edges: Deque[str] = deque()
    #     lastCell = Cell(0, TypeTerrain.plain)

   
    
    # for i in range(0, lines * column):
    #     currentCell = Cell(i+1, random.choice(list(TypeTerrain)))
    #     # currenCell = (lastCell, newCell)
    #     # lastCell = currenCell
    #     cellList.append(currentCell)

    
    lines: int = 4
    column: int = 4

    i = 0
    for x in range(0, lines):
        for y in range(0,column):
            currentCell = Cell(i, random.choice(list(TypeTerrain)), x, y)
            cellList.append(currentCell)
            i = i + 1



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
    # for i in range(0, 16):
    #     print('edges: [ ', i, ' ] | ',  edges[i].data, ', ', edges[i].terrain)

    # i=0
    # for x in range(0, lines):
    #     for y in range(0,column):
    #         print('edges: [ ', cellList[i].data, ' ] | ', cellList[i].terrain, ' | ', cellList[i].positionX, ', ', cellList[i].positionY,)
    #         i = i + 1

    start: Cell = cellList[0]
    end: Cell = cellList[15]
    # end: Cell = Cell(88, random.choice(list(TypeTerrain)), 200, 200)


    print('start: ', start.data)
    print('end: ', end.data)


    newCellList = [(cellList[0], cellList[1]),
             (cellList[0], cellList[4]),

             (cellList[1], cellList[0]),
             (cellList[1], cellList[2]),
             (cellList[1], cellList[5]),

             (cellList[2], cellList[1]),
             (cellList[2], cellList[3]),
             (cellList[2], cellList[6]),

             (cellList[3], cellList[2]),
             (cellList[3], cellList[7]),

             (cellList[4], cellList[0]),
             (cellList[4], cellList[5]),
             (cellList[4], cellList[8]),

             (cellList[5], cellList[4]),
             (cellList[5], cellList[1]),
             (cellList[5], cellList[6]),
             (cellList[5], cellList[9]),

             (cellList[6], cellList[5]),
             (cellList[6], cellList[2]),
             (cellList[6], cellList[7]),
             (cellList[6], cellList[10]),

             (cellList[7], cellList[6]),
             (cellList[7], cellList[3]),
             (cellList[7], cellList[11]),

             (cellList[8], cellList[4]),
             (cellList[8], cellList[9]),
             (cellList[8], cellList[12]),

             (cellList[9], cellList[8]),
             (cellList[9], cellList[5]),
             (cellList[9], cellList[10]),
             (cellList[9], cellList[11]),

             (cellList[10], cellList[9]),
             (cellList[10], cellList[6]),
             (cellList[10], cellList[11]),
             (cellList[10], cellList[14]),

             (cellList[11], cellList[10]),
             (cellList[11], cellList[7]),
             (cellList[11], cellList[15]),

             (cellList[12], cellList[8]),
             (cellList[12], cellList[13]),

             (cellList[13], cellList[12]),
             (cellList[13], cellList[9]),
             (cellList[13], cellList[14]),

             (cellList[14], cellList[13]),
             (cellList[14], cellList[10]),
             (cellList[14], cellList[15]),

             (cellList[15], cellList[14]),
             (cellList[15], cellList[11]),

    ]

    print('Tamanho da CellList: ', len(newCellList))
    # i = 0
    # for vertice in newEdges:
    #     print('edges: [ ', i, ' ] | ',  vertice[0].data, ', ', vertice[1].terrain)
    #     i = i + 1
    graph = Graph(newCellList)

    aux = ""
    for vertice in graph.adjacent:
        for cell in graph.adjacent[vertice]:
            if (vertice != aux):
                print('\n[ ', vertice.data ,' | ', vertice.terrain.value, ' ] ->  ', cell.data, end="")
            else:
                print(' -> ', cell.data, end="")
    
            aux = vertice


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

    # print(bfs(graph, start, end))

    print(aStar(graph, start, end))



if __name__ == "__main__":
    main()