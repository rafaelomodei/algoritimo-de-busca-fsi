from cell import Cell
from typing import Deque
from collections import deque
from terrain import TypeTerrain
from utils.search.utilSearch import isGoal, maxSizeOfListCellNeighbors

def breadthFirstSearch(graph: dict, initialCell: Cell, goalCell: Cell) -> float and Cell and None:
    punishment: float = 0
    maxSizeOfNeighbors: int = 0
    queueCellVisiteds: Deque[Cell] = deque()
    queueCell: Deque[Cell] = deque()
    
    queueCell.append(initialCell)

    print('initialCell: ', initialCell.data)
    print('goalCell: ', goalCell.data)
    punishment = punishment - initialCell.terrain.value
    while queueCell:

        currentCell = queueCell.popleft() #remove o primeiro elemento que entrou na lista
        maxSizeOfNeighbors = maxSizeOfListCellNeighbors(maxSizeOfNeighbors, len(queueCell))
        print('------')
        print('Celula com menor distancia: ', currentCell.data)
        print('Celula atual: ', currentCell.data)
        print('Tamanho da fila das celulas visitadas: ', len(queueCellVisiteds))
        print('Tamanho da fila das celulas visinhas: ', maxSizeOfNeighbors)

        if (currentCell.terrain != TypeTerrain.wall):
            if (currentCell not in queueCellVisiteds):
                punishment = punishment + currentCell.terrain.value
                queueCellVisiteds.append(currentCell)
                queueCell.extend(set(graph[currentCell]) - set(queueCellVisiteds))

                if isGoal(currentCell, goalCell):
                    print('É o objetivo ? : ', (isGoal(currentCell, goalCell)) and 'Sim' or 'Não')
                    return punishment, maxSizeOfNeighbors, queueCellVisiteds
            
        print('Fila de celulas VISITADAS:: ', end="")
        for cell in queueCellVisiteds:
            print(', ', cell.data, end="")
        
        print('\nFila de celulas VISINHAS:  ', end="")
        for cell in queueCell:
            print(', ', cell.data , end="")
        print(' ')
        print('É o objetivo ? : ', (isGoal(currentCell, goalCell)) and 'Sim' or 'Não')
    
    return punishment, maxSizeOfNeighbors, None