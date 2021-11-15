from typing import Deque
from collections import deque 
import random 
from graph import Graph
from cell import Cell
from terrain import TypeTerrain


def scenery(initialPosition: int, goalPosition: int) -> Graph and Cell:

    cellList: Deque[Cell] = deque()
    lines: int = 4
    column: int = 4


    i = 0
    for x in range(0, lines):
        for y in range(0,column):
            currentCell = Cell(i, random.choice(list(TypeTerrain)), x, y)
            cellList.append(currentCell)
            i = i + 1
    
    start: Cell = cellList[initialPosition]
    end: Cell = cellList[goalPosition]

    newCellList = [
        (cellList[0], cellList[1]),
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

    graph = Graph(newCellList)

    aux = ""
    for vertice in graph.adjacent:
        for cell in graph.adjacent[vertice]:
            if (vertice != aux):
                print('\n[ ', vertice.data ,' | ', vertice.terrain.value, ' ] ->  ', cell.data, end="")
            else:
                print(' -> ', cell.data, end="")
    
            aux = vertice
    print('')

    return start, end, graph
