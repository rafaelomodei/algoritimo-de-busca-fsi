from searchAlgorithms.breadthFirstSearch import breadthFirstSearch
from searchAlgorithms.depthFirstSearch import depthFirstSearch
from searchAlgorithms.greedySearch import greedySearch
from searchAlgorithms.aStarSearch import aStarSearch
from scenery.scenery import scenery
from utils.search.utilSearch import printlListCell



def main():

    initialPosition, goalPosition, scenaryGraph = scenery(0, 3)

    print('\n\n----------------------------------')
    print('Algoritimo: Busca Profundidade')
    print('----------------------------------\n')
    resultCostDepthFirstSearch, maxSizeOfListCellNeighborsDepthFirstSearch, resultCelVisitedsDepthFirstSearch = depthFirstSearch(scenaryGraph, initialPosition, goalPosition)
    

    print('\n\n----------------------------------')
    print('Algoritimo: Busca Largura')
    print('----------------------------------\n')
    resultCostBreadthFirstSearch, maxSizeOfListCellNeighborsBreadthFirstSearch, resultCelVisitedsBreadthFirstSearch = breadthFirstSearch(scenaryGraph, initialPosition, goalPosition)
    
    print('\n\n----------------------------------')
    print('Algoritimo: Busca Gulosa')
    print('----------------------------------\n')
    resultCostGreedySearch, maxSizeOfListCellNeighborsGreedySearch, resultCelVisitedsGreedySearch = greedySearch(scenaryGraph, initialPosition, goalPosition)
    
    
    print('\n\n----------------------------------')
    print('Algoritimo: Busca A*')
    print('----------------------------------\n')
    resultCostAStarSearch, maxSizeOfListCellNeighborsAStarSearch, resultCelVisitedsAStarSearch = aStarSearch(scenaryGraph, initialPosition, goalPosition)

    print('\n\n----------------------------------')
    print('Algoritimo: Busca Profundidade')
    print('Custo: ', resultCostDepthFirstSearch)
    print('Tamanho maximo de visinho visitados: ', maxSizeOfListCellNeighborsDepthFirstSearch)
    print('Lista de celulas VISITADAS: ',not resultCelVisitedsAStarSearch and 'Não possiu solução', end="")
    printlListCell(resultCelVisitedsDepthFirstSearch)
    print('')
    print('----------------------------------')

    print('\n\n----------------------------------')
    print('Algoritimo: Busca Largura')
    print('Custo: ', resultCostBreadthFirstSearch)
    print('Tamanho maximo de visinho visitados: ', maxSizeOfListCellNeighborsBreadthFirstSearch)
    print('Lista de celulas VISITADAS: ', not resultCelVisitedsAStarSearch and 'Não possiu solução', end="")
    printlListCell(resultCelVisitedsBreadthFirstSearch)
    print('')
    print('----------------------------------')

    print('\n\n----------------------------------')
    print('Algoritimo: Busca Gulosa')
    print('Custo: ', resultCostGreedySearch)
    print('Tamanho maximo de visinho visitados: ', maxSizeOfListCellNeighborsGreedySearch)
    print('Lista de celulas VISITADAS: ', not resultCelVisitedsAStarSearch and 'Não possiu solução', end="")
    printlListCell(resultCelVisitedsGreedySearch)
    print('')
    print('----------------------------------')

    print('\n\n----------------------------------')
    print('Algoritimo: Busca A*')
    print('Custo: ', resultCostAStarSearch)
    print('Tamanho maximo de visinho visitados: ', maxSizeOfListCellNeighborsAStarSearch)
    print('Lista de celulas VISITADAS: ', not resultCelVisitedsAStarSearch and 'Não possiu solução', end="")
    printlListCell(resultCelVisitedsAStarSearch)
    print('')
    print('----------------------------------')



if __name__ == "__main__":
    main()
