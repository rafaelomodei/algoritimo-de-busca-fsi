from cell import Cell


class LinkedList:
    def __init__(self):
        self.head = None
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
        r = ""
        pointer = self.head
        while(pointer):
            r = r + str(pointer.data) + " -> "
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
        if self.head:
            # Inserção quando já existe elemento na lista
            pointer = self.head
            # Percorre todos os elementos até chegar ao ultimo elemento
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Cell(cell)
        else:
            # Primeiro elemento
            self.head = Cell(cell)
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
        cell = Cell(cell)
        if (index == 0):  # inserindo a celula na primeira posição
            cell = Cell(cell)
            cell.next = self.head
            self.head = cell
        else:
            pointer = self._getCell(index -1) # -1 pq quero inserir o elemento antes dele
            cell.next = pointer.next
            pointer.next = cell
        self._size = self._size + 1
    
    def remove(self, cell):
        if (self.head == None):
            raise ValueError("{} is not in list".format(cell))
        elif (self.head.data == cell):
            self.head = self.head.next
            self._size = self._size - 1
            return True
        else:
            ancestor = self.head 
            pointer = self.head.next
            while(pointer):
                if (pointer.data == cell):
                    ancestor.next = pointer.next
                    pointer.next = None
                ancestor = pointer
                pointer = pointer.next
            self._size = self._size - 1
            return True
        raise ValueError("{} is not in list".format(cell)) #Caso percorra toda lista e não encontra o elemento
    

