from cell import Cell
import math

def isGoal(currentVertice: Cell, verticeEnd: Cell) -> bool:
    """Verifica se a celula atual é o objetivo"""
    return currentVertice == verticeEnd and True or False

def distanceBetweenTwoCell(cellOne: Cell, cellTwo: Cell) -> float:
    """Calcula a distancia duas celula"""

    a = ((cellOne.positionX)- cellTwo.positionX)**2
    b = (cellOne.positionY - cellTwo.positionY)**2
    return math.sqrt(a + b)

def cellMinDistance(queue: list, cellGoal: Cell) -> Cell:
    """Retorna a celula com a menor distancia"""

    cellShortDistance = queue[0] # primeiro elemento da lista

    for cell in queue:
        #verifica se a celula atual tem a distancia menor que a celula minima anterior
        if (distanceBetweenTwoCell(cell, cellGoal) < distanceBetweenTwoCell(cellShortDistance, cellGoal)):
            cellShortDistance = cell

    return cellShortDistance

def cellMinDistanceAndCost(queue: list, cellGoal: Cell) -> Cell:
    """Retorna a celula com a menor distancia e menor custo"""

    cellShortDistance: Cell = queue[0] # primeiro elemento da lista

    for cell in queue:
        currentCell = (distanceBetweenTwoCell(cell, cellGoal) + cell.terrain.value)
        currentCellMinDistance = (distanceBetweenTwoCell(cellShortDistance, cellGoal) + cellShortDistance.terrain.value)
        #verifica se a celula atual tem a distancia menor que a celula minima anterior
        if (currentCell < currentCellMinDistance):
            cellShortDistance = cell

    return cellShortDistance

def maxSizeOfListCellNeighbors(currentValue: int,  sizeListCellNeighbors: int):
    if(currentValue < sizeListCellNeighbors):
        return sizeListCellNeighbors
    return currentValue

def printlListCell(listCell: list) -> None:
    if(listCell):
        for cell in listCell:
                print(', ', cell.data, end="")