from cell import Cell
from terrain import TypeTerrain
from utils.search.utilSearch import isGoal, cellMinDistanceAndCost, maxSizeOfListCellNeighbors, printlListCell

def aStarSearch(graph: dict, initialCell: Cell, goalCell: Cell) -> float and list and None:
    """Calcula a menor rota com o menor custo"""

    punishment: float = 0
    maxSizeOfNeighbors: int = 0
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
        maxSizeOfNeighbors = maxSizeOfListCellNeighbors(maxSizeOfNeighbors, len(listCellNeighbors))
        print('------')
        print('Celula com menor distancia e menor custo: ', currentCell.data)
        print('Celula atual: ', currentCell.data)
        print('Tamanho da lista das celulas visitadas: ', len(listCellVisiteds))
        print('Tamanho da lista das celulas visinhas: ', maxSizeOfNeighbors)


        if (currentCell.terrain != TypeTerrain.wall):
            if (currentCell not in listCellVisiteds):
                punishment = punishment + currentCell.terrain.value
                listCellVisiteds.append(currentCell)
                listCellNeighbors.extend((set(graph[currentCell]) - set(listCellVisiteds)))
        
                if (isGoal(currentCell, goalCell)):
                    return punishment, maxSizeOfNeighbors, listCellVisiteds

        print('Lista de celulas VISITADAS: ', end="")
        printlListCell(listCellVisiteds)
        
        
        print('\nLista de celulas VISINHAS: ', end="")
        printlListCell(listCellNeighbors)
        print('')
        print('É o objetivo ? : ', (isGoal(currentCell, goalCell)) and 'Sim' or 'Não')

        for cell in listCellNeighbors:
            if(cell.data == currentCell.data):
                listCellNeighbors.remove(cell)
                print('Removido!! ', cell.data)

    return punishment, maxSizeOfNeighbors, None