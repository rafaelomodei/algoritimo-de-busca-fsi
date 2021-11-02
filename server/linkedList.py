from cell import Cell


class LinkedList:
    def __init__(self):
        self.head = None
        self.trailer = None
        self._size = 0

    def __getitem__(self, index):
        pointer = self._getCell(index)
        
        if pointer:
            return pointer.data
        raise IndexError("list index out of range")

    def __setitem__(self, index, cell):
        pointer = self._getCell(index)
        if pointer:
            pointer.data = cell
        else:
            raise IndexError("list index out of range")
    
    def __len__(self):
        return self._size
    
    def __repr__(self):
        # head =  str("HEADER: " + str(self.head.data) + "\nTRAILER: " + str(self.trailer.data))
        r = ""

        print("HEADER: ", self.head.data)
        print("TRAILER: ", self.trailer.data)

        pointer = self.head
        while(pointer):
            if (self._size):
                r = r + "\n" + (pointer.prev and str(pointer.prev.data) or "NULL") + " <- " + str(pointer.data) + " -> " + (pointer.next and str(pointer.next.data) or "NULL")

            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()
    
    def _getCell(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                    pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        return pointer

    def append(self, cell):
        currentCell = Cell(cell)

        if (self._size):
            print("append::if")
            # Inserção quando já existe elemento na lista
            self.trailer.next = currentCell
            currentCell.prev = self.trailer
            currentCell.next = None
            self.trailer = currentCell
        else:
            print("append::else")
            # Primeiro elemento add na lista
            self.head = self.trailer = Cell(cell)
        self._size = self._size + 1

    # Retorna o index da celula
    def index(self, cell):
        pointer = self.head
        i = 0
        while(pointer):
            if (pointer.data == cell):
                return i
            pointer = pointer.next
            i = i+1
            raise ValueError("{} is not in list".format(cell))

    def insert(self, index, cell):
        currentCell = Cell(cell)
        if (not(self._size)):  # inserindo a celula na primeira posição
            print("Header Null")
            self.head = currentCell
            self.trailer = currentCell
        elif (index == 0):
            print("elif")
            currentCell.next = self.head
            self.head.prev = currentCell
            self.head = currentCell

        elif (self._size == index):
            self.append(cell)
            self._size = self._size - 1
        else:
            print("else")
            pointer = self._getCell(index - 1) # -1 para inserir o elemento antes do index informado
            currentCell.next = pointer.next
            currentCell.prev = pointer
            pointer.next = currentCell
            currentCell.next.prev = currentCell
        self._size = self._size + 1
    
    def remove(self, cell):
        if (self.head == None):
            raise ValueError("{} is not in list".format(cell))
        elif (self.head.data == cell):
            self.head.next.prev = None
            self.head = self.head.next
            self._size = self._size - 1
            return True
        elif (self.trailer.data == cell):
            self.trailer.prev.next = None
            self.trailer = self.trailer.prev
            self._size = self._size - 1
            return True
        else:
            currentPrev = self.head 
            pointer = self.head.next
            while(pointer):
                if (pointer.data == cell):
                    currentPrev.next = pointer.next
                    pointer.next.prev = currentPrev
                    pointer.next = None
                currentPrev = pointer
                pointer = pointer.next
            self._size = self._size - 1
            return True
        raise ValueError("{} is not in list".format(cell)) #Caso percorra toda lista e não encontra o elemento
    

