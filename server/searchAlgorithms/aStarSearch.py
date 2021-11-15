from utils.search.utilSearch import isGoal, cellMinDistanceAndCost
from cell import Cell

def aStarSearch(graph: dict, initialCell: Cell, goalCell: Cell) -> float and list and None:
    """Calcula a menor rota com o menor custo"""

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
    
    while listCellNeighbors:

        currentCell = cellMinDistanceAndCost(listCellNeighbors, goalCell)
        print('------')
        print('Celula com menor distancia: ', currentCell.data)
        print('celula atual: ', currentCell.data)
        print('Tamanho dos visitados: ', len(listCellVisiteds))

        if (currentCell not in listCellVisiteds):
            punishment = punishment + currentCell.terrain.value
            listCellVisiteds.append(currentCell)
            listCellNeighbors.extend((set(graph[currentCell]) - set(listCellVisiteds)))
    
            if (isGoal(currentCell, goalCell)):
                return punishment, listCellVisiteds

        print('Visitados: ', end="")
        for visitedCell in listCellVisiteds:
            print(', ', visitedCell.data, end="")
        
        print('\nMELHHORES - List: ', end="")
        for neighborCell in listCellNeighbors:
            print(', ', neighborCell.data, end="")
        print(' ')
        print('É o objetivo ? : ', (isGoal(currentCell, goalCell)) and 'Sim' or 'Não')

        for cell in listCellNeighbors:
            if(cell.data == currentCell.data):
                listCellNeighbors.remove(cell)
                print('Removido!! ', cell.data)

    return punishment, None