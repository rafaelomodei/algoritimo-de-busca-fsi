from graph import Graph

def sceneryToJson(graph: Graph) -> dict:
    """Retorna o mapa com a estrutura de json"""

    listCellJson: list = list()
    listCellAdjacentJson: list = list()

    for vertice in graph.adjacent:
        for cell in graph.adjacent[vertice]:

            listCellJson.append({
                "data": cell.data,
                "terrain": cell.terrain.value,
                "positionX": cell.positionX,
                "positionY": cell.positionY,
            })
        
        listCellAdjacentJson.append({
            vertice.data : list(listCellJson)
        })
        listCellJson.clear()

    return { "scenary" : listCellAdjacentJson}