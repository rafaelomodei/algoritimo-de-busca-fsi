import random
from linkedList import LinkedList

def main():
    list = LinkedList()
    
    x = random.randint(1, 10)

    for i in range(x):
        list.append(random.randint(1, 100))
    
    print(list)

    # print('Tamanho da lista: ', len(list))

    # valueInList = list[0]
    # print('Valor procurando na lista: ',valueInList)
    # for i in range(1):
    #     print('[', i, '] = ', list.index(valueInList))

if __name__ == "__main__":
    main()