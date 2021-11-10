from typing import Deque
from collections import deque
from cell import Cell


def isGoal(currentVertice: Cell, verticeEnd: Cell):
    return currentVertice == verticeEnd and True or False


# def bfs(grafo: dict, verticeStart: str, verticeEnd: str):
#     visited: set = set()
#     queue: Deque[str] = deque()
#     queue.append(verticeStart)

#     while queue:
#         vertice: str = queue.pop(0)

#         if (isGoal(vertice, verticeEnd)):

#         if vertice not in visited:
#             visited.add(vertice)
#             newList = grafo[vertice]
#             newList.remove('C')
#             print('newList::', newList)
#             # fila.extend()
#         print('Visitados::',visited)
        
#     return visitados

# def diff(list1, list2):
#     c = set(list1).union(set(list2))  # or c = set(list1) | set(list2)
#     d = set(list1).intersection(set(list2))  # or d = set(list1) & set(list2)
#     return list(c - d)

# def diff(list1, list2):
#     return list(set(list1).symmetric_difference(set(list2)))  # or return list(set(list1) ^ set(list2))

def bfs(grafo: dict, verticeStart: Cell, verticeEnd: Cell):
    visitados: Deque[Cell] = deque()
    queue: Deque[Cell] = deque()
    foundGoal: bool = False
    queue.append(verticeStart)


    print('VerticeStart: ', verticeStart.data - 1)
    print('VerticeEnd: ', verticeEnd.data - 1)



    while queue:
        vertice = queue.popleft()
        print('------')
        print('Vertice: ', vertice.data -1)

        if vertice not in visitados:
            visitados.append(vertice)
            queue.extend(set(grafo[vertice]) - set(visitados))
            
            print('Visitados: ', end="")
            for q in visitados:
                print(', ', q.data - 1, end="")
            
            print('\nQueue: ', end="")
            for q in queue:
                print(', ', q.data -1 , end="")
            print(' ')
            print('É o objetivo ? : ', (isGoal(vertice, verticeEnd)) and 'Sim' or 'Não')

        if isGoal(vertice, verticeEnd):
            foundGoal = True
            return visitados
    
    if not foundGoal:
        return None