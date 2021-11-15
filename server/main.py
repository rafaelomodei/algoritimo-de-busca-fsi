from searchAlgorithms.breadthFirstSearch import breadthFirstSearch
from searchAlgorithms.depthFirstSearch import depthFirstSearch
from searchAlgorithms.greedySearch import greedySearch
from searchAlgorithms.aStarSearch import aStarSearch
from scenery.scenery import scenery
from utils.scenery.sceneryToJson import sceneryToJson



def main():

    initialPosition, goalPosition, scenaryGraph = scenery(0, 3)
    scenaryJson = sceneryToJson(scenaryGraph)

    # resultCostDepthFirstSearch, resultCelVisitedsDepthFirstSearch = depthFirstSearch(scenaryGraph, initialPosition, goalPosition)
    # resultCostBreadthFirstSearch, resultCelVisitedsBreadthFirstSearch = breadthFirstSearch(scenaryGraph, initialPosition, goalPosition)
    # resultCostGreedySearch, resultCelVisitedsGreedySearch = greedySearch(scenaryGraph, initialPosition, goalPosition)
    # resultCostAStarSearch, resultCelVisitedsAStarSearch = aStarSearch(scenaryGraph, initialPosition, goalPosition)

    # print('Custo - Largura: ', resultCelVisitedsBreadthFirstSearch, 'Custo - Gulosa: ', resultCelVisitedsGreedySearch, 'Custo - A*:', resultCelVisitedsAStarSearch )

    # print('Custo - Profundidade: ', resultCostDepthFirstSearch, ' | Custo - Largura: ', resultCostBreadthFirstSearch, ' | Custo - Gulosa: ', resultCostGreedySearch, ' | Custo - A*:', resultCostAStarSearch )




if __name__ == "__main__":
    main()
