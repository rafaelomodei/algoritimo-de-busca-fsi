from cell import Cell
from typing import Deque
from collections import deque
from utils.search.utilSearch import isGoal

def breadthFirstSearch(graph: dict, initialCell: Cell, goalCell: Cell) -> float and Cell and None:
    punishment: float = 0
    queueCellVisiteds: Deque[Cell] = deque()
    queueCell: Deque[Cell] = deque()
    
    queueCell.append(initialCell)

    print('initialCell: ', initialCell.data)
    print('goalCell: ', goalCell.data)
    punishment = punishment - initialCell.terrain.value
    while queueCell:

        currentCell = queueCell.popleft() #remove o primeiro elemento que entrou na lista
        print('------')
        print('currentCell: ', currentCell.data)

        if (currentCell not in queueCellVisiteds):
            punishment = punishment + currentCell.terrain.value
            queueCellVisiteds.append(currentCell)
            queueCell.extend(set(graph[currentCell]) - set(queueCellVisiteds))

            if isGoal(currentCell, goalCell):
                print('É o objetivo ? : ', (isGoal(currentCell, goalCell)) and 'Sim' or 'Não')
                return punishment, queueCellVisiteds
            
        print('queueCellVisiteds: ', end="")
        for cell in queueCellVisiteds:
            print(', ', cell.data, end="")
        
        print('\nFila: ', end="")
        for cell in queueCell:
            print(', ', cell.data , end="")
        print(' ')
        print('É o objetivo ? : ', (isGoal(currentCell, goalCell)) and 'Sim' or 'Não')
    
    return punishment, None