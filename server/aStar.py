import math
from typing import Deque
from collections import deque
from cell import Cell


def isGoal(currentVertice: Cell, verticeEnd: Cell) -> bool:
    return currentVertice == verticeEnd and True or False

# def isMin(queue: Deque[Cell]):
#     minVertex = list(queue[0])[0] # Primeiro filho

#     for i in  range(0, len(list(queue[0]))): # Percorre todos os filhos do nó
#         if(list(queue[0])[i].data < minVertex.data):
#             minVertex = list(queue[0])[i]

#     return minVertex # retorna o menor filho

def distanceBetweenTwoCell(cellOne: Cell, cellTwo: Cell) -> float:
    """Calcula a distancia duas celula"""

    a = ((cellOne.positionX)- cellTwo.positionX)**2
    b = (cellOne.positionY - cellTwo.positionY)**2
    return math.sqrt(a + b)

def cellMinDistance(queue: list, cellGoal: Cell) -> Cell:
    """Retorna a celula com a menor distancia"""

    cellShortDistance: Cell = queue[0] # primeiro elemento da lista

    for cell in queue:
        #verifica se a celula atual tem a distancia menor que a celula minima anterior
        if ((distanceBetweenTwoCell(cell, cellGoal) + cell.terrain.value) < (distanceBetweenTwoCell(cellShortDistance, cellGoal) + cellShortDistance.terrain.value)):
            cellShortDistance = cell

    return cellShortDistance



def aStar(graph: dict, initialCell: Cell, goalCell: Cell) -> float and list and None:

    punishment: float = 0
    listCellVisiteds: list[Cell] = list()
    listCellNeighbors: list[Cell] = list()

    if (isGoal(initialCell, goalCell)):
        return [initialCell]

    listCellVisiteds.append(initialCell)

    for cell in list(graph[initialCell]): # Add a celulas visinhas em uma lista
        listCellNeighbors.append(cell)

    print('\nVerticeStart: ', initialCell.data)
    print('VerticeEnd: ', goalCell.data)

    print('Quantidade de visinhos: ', len(listCellNeighbors))

    i = 0
    while listCellNeighbors:

       
        print('------')
        cell = cellMinDistance(listCellNeighbors, goalCell)
        print('Celula com menor distancia: ', cell.data)
        print('celula atual: ', cell.data)
        print('Tamanho dos visitados: ', len(listCellVisiteds))

        

        # lastCell: Cell = cell

        if cell not in listCellVisiteds:
            punishment = punishment + cell.terrain.value
            listCellVisiteds.append(cell)
            
                
            
            
            # uniqList = list(dict.fromkeys(listCellNeighbors))
            # print('Lista com elemento unicos: ')
            # for cell in uniqList:
            #     print(', ', cell.data, end="")
            # print('')
            listCellNeighbors.extend((set(graph[cell]) - set(listCellVisiteds)))
            # listCellNeighbors = list(dict.fromkeys(listCellNeighbors)) # Remove elementos repetidos

            # listCellNeighbors.remove(cell)

        

            # if (c.data == cell.data):

            if isGoal(cell, goalCell):
                return punishment, listCellVisiteds
        print('Visitados: ', end="")
        for visitedCell in listCellVisiteds:
            print(', ', visitedCell.data, end="")
        
        print('\nMELHHORES - List: ', end="")
        for neighborCell in listCellNeighbors:
            print(', ', neighborCell.data, end="")
        print(' ')
        print('É o objetivo ? : ', (isGoal(cell, goalCell)) and 'Sim' or 'Não')

        for c in listCellNeighbors:
            if(c.data == cell.data):
                listCellNeighbors.remove(cell)
                print('Removido!! ', cell.data)

        i = i + 1
    
    return punishment, None