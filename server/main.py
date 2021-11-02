import random
from linkedList import LinkedList

def main():
    list = LinkedList()
    
    for i in range(10):
        list.append(random.randint(1, 10))
    

    print('Tamanho da lista: ', len(list))

    valueInList = list[0]
    print('Valor procurando na lista: ',valueInList)
    for i in range(1):
        print('[', i, '] = ', list.index(valueInList))

if __name__ == "__main__":
    main()