from typing import Deque
from collections import deque 
import random 
from graph import Graph
from cell import Cell
from terrain import TypeTerrain


def scenery(initialPosition: int, goalPosition: int) -> Graph and Cell:

    cellList: Deque[Cell] = deque()
    lines: int = 6
    column: int = 6
    initialPositionCreated: bool = False

    i = 0
    for x in range(0, lines):
        for y in range(0,column):

            if((not initialPositionCreated) and (initialPosition + 1) == ((x + 1) * (y + 1))): # Para a celula inicial sempre ser um terreno solido de custo 1
                currentCell = Cell(i, TypeTerrain.plain, x, y)
                initialPositionCreated = True
                print('initialPosition: ', initialPosition)
                print('Resultado: ', (x  * y ))
            elif(((initialPosition + 1) * (goalPosition + 1)) == ((x + 1) * (y + 1))): # Para o objetivo sempre ser um terreno solido de custo 1
                currentCell = Cell(i, TypeTerrain.solid, x, y)
                print('-------')
                print('initialPosition: ', initialPosition)
                print('goalPosition: ', goalPosition)
                print('Resultado: ', (x ) * (y ))
            else:
                currentCell = Cell(i, random.choice(list(TypeTerrain)), x, y)




            cellList.append(currentCell)
            i = i + 1
    
    start: Cell = cellList[initialPosition]
    end: Cell = cellList[goalPosition]

    newCellList = [
        #Lina 0 Coluna 0
        (cellList[0], cellList[1]),
        (cellList[0], cellList[6]),
        (cellList[0], cellList[7]),

        #Lina 0 Coluna 1
        (cellList[1], cellList[0]),
        (cellList[1], cellList[2]),
        (cellList[1], cellList[6]),
        (cellList[1], cellList[7]),
        (cellList[1], cellList[8]),

        #Lina 0 Coluna 2
        (cellList[2], cellList[1]),
        (cellList[2], cellList[3]),
        (cellList[2], cellList[7]),
        (cellList[2], cellList[8]),
        (cellList[2], cellList[9]),

        #Lina 0 Coluna 3
        (cellList[3], cellList[2]),
        (cellList[3], cellList[4]),
        (cellList[3], cellList[8]),
        (cellList[3], cellList[9]),
        (cellList[3], cellList[10]),

        #Lina 0 Coluna 4
        (cellList[4], cellList[3]),
        (cellList[4], cellList[5]),
        (cellList[4], cellList[9]),
        (cellList[4], cellList[10]),
        (cellList[4], cellList[11]),

        #Lina 0 Coluna 5
        (cellList[5], cellList[4]),
        (cellList[5], cellList[10]),
        (cellList[5], cellList[11]),

        #Lina 1 Coluna 0
        (cellList[6], cellList[0]),
        (cellList[6], cellList[1]),
        (cellList[6], cellList[7]),
        (cellList[6], cellList[12]),
        (cellList[6], cellList[13]),

        #Lina 1 Coluna 1
        (cellList[7], cellList[0]),
        (cellList[7], cellList[1]),
        (cellList[7], cellList[2]),
        (cellList[7], cellList[6]),
        (cellList[7], cellList[8]),
        (cellList[7], cellList[12]),
        (cellList[7], cellList[13]),
        (cellList[7], cellList[14]),

        #Lina 1 Coluna 2
        (cellList[8], cellList[1]),
        (cellList[8], cellList[2]),
        (cellList[8], cellList[3]),
        (cellList[8], cellList[7]),
        (cellList[8], cellList[9]),
        (cellList[8], cellList[13]),
        (cellList[8], cellList[14]),
        (cellList[8], cellList[15]),

        #Lina 1 Coluna 3
        (cellList[9], cellList[2]),
        (cellList[9], cellList[3]),
        (cellList[9], cellList[4]),
        (cellList[9], cellList[8]),
        (cellList[9], cellList[10]),
        (cellList[9], cellList[14]),
        (cellList[9], cellList[15]),
        (cellList[9], cellList[16]),


        #Lina 1 Coluna 4
        (cellList[10], cellList[3]),
        (cellList[10], cellList[4]),
        (cellList[10], cellList[5]),
        (cellList[10], cellList[9]),
        (cellList[10], cellList[11]),
        (cellList[10], cellList[15]),
        (cellList[10], cellList[16]),
        (cellList[10], cellList[17]),


        #Lina 1 Coluna 5
        (cellList[11], cellList[4]),
        (cellList[11], cellList[5]),
        (cellList[11], cellList[10]),
        (cellList[11], cellList[16]),
        (cellList[11], cellList[17]),


        #Lina 2 Coluna 0
        (cellList[12], cellList[6]),
        (cellList[12], cellList[7]),
        (cellList[12], cellList[13]),
        (cellList[12], cellList[18]),
        (cellList[12], cellList[19]),


        #Lina 2 Coluna 1
        (cellList[13], cellList[6]),
        (cellList[13], cellList[7]),
        (cellList[13], cellList[8]),
        (cellList[13], cellList[12]),
        (cellList[13], cellList[14]),
        (cellList[13], cellList[18]),
        (cellList[13], cellList[19]),
        (cellList[13], cellList[20]),

        #Lina 2 Coluna 2
        (cellList[14], cellList[7]),
        (cellList[14], cellList[8]),
        (cellList[14], cellList[9]),
        (cellList[14], cellList[13]),
        (cellList[14], cellList[15]),
        (cellList[14], cellList[19]),
        (cellList[14], cellList[20]),
        (cellList[14], cellList[21]),



        #Lina 2 Coluna 3
        (cellList[15], cellList[8]),
        (cellList[15], cellList[9]),
        (cellList[15], cellList[10]),
        (cellList[15], cellList[14]),
        (cellList[15], cellList[16]),
        (cellList[15], cellList[20]),
        (cellList[15], cellList[21]),
        (cellList[15], cellList[22]),

        #Lina 2 Coluna 4
        (cellList[16], cellList[9]),
        (cellList[16], cellList[10]),
        (cellList[16], cellList[11]),
        (cellList[16], cellList[16]),
        (cellList[16], cellList[17]),
        (cellList[16], cellList[21]),
        (cellList[16], cellList[22]),
        (cellList[16], cellList[23]),

        #Lina 2 Coluna 5
        (cellList[17], cellList[10]),
        (cellList[17], cellList[11]),
        (cellList[17], cellList[16]),
        (cellList[17], cellList[22]),
        (cellList[17], cellList[23]),

        #Lina 3 Coluna 0
        (cellList[18], cellList[12]),
        (cellList[18], cellList[13]),
        (cellList[18], cellList[19]),
        (cellList[18], cellList[24]),
        (cellList[18], cellList[25]),

        #Lina 3 Coluna 1
        (cellList[19], cellList[12]),
        (cellList[19], cellList[13]),
        (cellList[19], cellList[14]),
        (cellList[19], cellList[18]),
        (cellList[19], cellList[20]),
        (cellList[19], cellList[24]),
        (cellList[19], cellList[25]),
        (cellList[19], cellList[26]),

        #Lina 3 Coluna 2
        (cellList[20], cellList[13]),
        (cellList[20], cellList[14]),
        (cellList[20], cellList[15]),
        (cellList[20], cellList[18]),
        (cellList[20], cellList[21]),
        (cellList[20], cellList[25]),
        (cellList[20], cellList[26]),
        (cellList[20], cellList[27]),

        #Lina 3 Coluna 3
        (cellList[21], cellList[14]),
        (cellList[21], cellList[15]),
        (cellList[21], cellList[16]),
        (cellList[21], cellList[20]),
        (cellList[21], cellList[22]),
        (cellList[21], cellList[26]),
        (cellList[21], cellList[27]),
        (cellList[21], cellList[28]),

        #Lina 3 Coluna 4
        (cellList[22], cellList[15]),
        (cellList[22], cellList[16]),
        (cellList[22], cellList[17]),
        (cellList[22], cellList[21]),
        (cellList[22], cellList[23]),
        (cellList[22], cellList[27]),
        (cellList[22], cellList[28]),
        (cellList[22], cellList[29]),

        #Lina 3 Coluna 5
        (cellList[23], cellList[16]),
        (cellList[23], cellList[17]),
        (cellList[23], cellList[22]),
        (cellList[23], cellList[28]),
        (cellList[23], cellList[29]),

        #Lina 4 Coluna 0
        (cellList[24], cellList[18]),
        (cellList[24], cellList[19]),
        (cellList[24], cellList[25]),
        (cellList[24], cellList[30]),
        (cellList[24], cellList[31]),

        #Lina 4 Coluna 1
        (cellList[25], cellList[18]),
        (cellList[25], cellList[19]),
        (cellList[25], cellList[20]),
        (cellList[25], cellList[24]),
        (cellList[25], cellList[26]),
        (cellList[25], cellList[30]),
        (cellList[25], cellList[31]),
        (cellList[25], cellList[32]),

        #Lina 4 Coluna 2
        (cellList[26], cellList[18]),
        (cellList[26], cellList[20]),
        (cellList[26], cellList[21]),
        (cellList[26], cellList[25]),
        (cellList[26], cellList[27]),
        (cellList[26], cellList[31]),
        (cellList[26], cellList[32]),
        (cellList[26], cellList[33]),

        #Lina 4 Coluna 3
        (cellList[27], cellList[20]),
        (cellList[27], cellList[21]),
        (cellList[27], cellList[22]),
        (cellList[27], cellList[26]),
        (cellList[27], cellList[28]),
        (cellList[27], cellList[32]),
        (cellList[27], cellList[33]),
        (cellList[27], cellList[34]),

        #Lina 4 Coluna 4
        (cellList[28], cellList[21]),
        (cellList[28], cellList[22]),
        (cellList[28], cellList[23]),
        (cellList[28], cellList[27]),
        (cellList[28], cellList[29]),
        (cellList[28], cellList[33]),
        (cellList[28], cellList[34]),
        (cellList[28], cellList[35]),

        #Lina 4 Coluna 5
        (cellList[29], cellList[22]),
        (cellList[29], cellList[23]),
        (cellList[29], cellList[28]),
        (cellList[29], cellList[34]),
        (cellList[29], cellList[35]),

        #Lina 5 Coluna 0
        (cellList[30], cellList[24]),
        (cellList[30], cellList[25]),
        (cellList[30], cellList[31]),

        #Lina 5 Coluna 1
        (cellList[31], cellList[24]),
        (cellList[31], cellList[25]),
        (cellList[31], cellList[26]),
        (cellList[31], cellList[30]),
        (cellList[31], cellList[32]),

        #Lina 5 Coluna 2
        (cellList[32], cellList[25]),
        (cellList[32], cellList[26]),
        (cellList[32], cellList[27]),
        (cellList[32], cellList[31]),
        (cellList[32], cellList[33]),

        #Lina 5 Coluna 3
        (cellList[33], cellList[26]),
        (cellList[33], cellList[27]),
        (cellList[33], cellList[28]),
        (cellList[33], cellList[32]),
        (cellList[33], cellList[34]),

        #Lina 5 Coluna 4
        (cellList[34], cellList[27]),
        (cellList[34], cellList[28]),
        (cellList[34], cellList[29]),
        (cellList[34], cellList[33]),
        (cellList[34], cellList[35]),

        #Lina 5 Coluna 5
        (cellList[35], cellList[28]),
        (cellList[35], cellList[29]),
        (cellList[35], cellList[34]),


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
