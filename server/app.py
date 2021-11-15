# app.py
import json
from flask import Flask, request, jsonify

from searchAlgorithms.breadthFirstSearch import breadthFirstSearch
from searchAlgorithms.depthFirstSearch import depthFirstSearch
from searchAlgorithms.greedySearch import greedySearch
from searchAlgorithms.aStarSearch import aStarSearch
from scenery.scenery import scenery
from utils.scenery.sceneryToJson import sceneryToJson

app = Flask(__name__)

initialPosition, goalPosition, scenaryGraph = scenery(0, 3)
scenaryJson = sceneryToJson(scenaryGraph)

# resultCostDepthFirstSearch, resultCelVisitedsDepthFirstSearch = depthFirstSearch(scenaryGraph, initialPosition, goalPosition)
# resultCostBreadthFirstSearch, resultCelVisitedsBreadthFirstSearch = breadthFirstSearch(scenaryGraph, initialPosition, goalPosition)
# resultCostGreedySearch, resultCelVisitedsGreedySearch = greedySearch(scenaryGraph, initialPosition, goalPosition)
# resultCostAStarSearch, resultCelVisitedsAStarSearch = aStarSearch(scenaryGraph, initialPosition, goalPosition)

# print('Custo - Largura: ', resultCelVisitedsBreadthFirstSearch, 'Custo - Gulosa: ', resultCelVisitedsGreedySearch, 'Custo - A*:', resultCelVisitedsAStarSearch )

# print('Custo - Profundidade: ', resultCostDepthFirstSearch, ' | Custo - Largura: ', resultCostBreadthFirstSearch, ' | Custo - Gulosa: ', resultCostGreedySearch, ' | Custo - A*:', resultCostAStarSearch )

countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
]

@app.get("/countries")
def get_countries():
    return jsonify(countries)

@app.get("/scenary")
def get_astar_custo():
    return jsonify({"teste": "omodei"})


# def _find_next_id():
#     return max(country["id"] for country in countries) + 1

# @app.get("/countries")
# def get_countries():
#     return jsonify(countries)

# @app.post("/countries")
# def add_country():
#     if request.is_json:
#         country = request.get_json()
#         country["id"] = _find_next_id()
#         countries.append(country)
#         return country, 201
#     return {"error": "Request must be JSON"}, 415

# @app.get("/astar")
# def get_astar():
#     return jsonify(pathList)

