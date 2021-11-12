# class Cell:

#     up = None
#     down = None
#     right = None
#     left = None

#     def __init__(self, data, indexX, indexY):
#         self.data: int = data
#         self.indexX: int = indexX
#         self.indexY: int = indexY
        


class Cell:

    def __init__(self, data: int, terrain: str, positionX: int, positionY: int):
        self.data: int = data
        self.terrain: str = terrain
        self.positionX: int = positionX
        self.positionY: int = positionY    
