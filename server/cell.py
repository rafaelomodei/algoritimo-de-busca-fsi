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

    def __init__(self, data: int, terrain: str):
        self.data: int = data
        self.terrain: str = terrain

        
