class lista_num (object):
    __nums = []

    def __init__(self, l):
        self.__nums = l 
    
    def maior(self):
        return max(self.__nums)
    
    def menor(self):
        return min(self.__nums)

if __name__ == "__main__":          
    lista = lista_num([int(num) for num in input().split()])

    print(f'Maior numero da lista = {lista.maior()}')
    print(f'Memor numero da lista = {lista.menor()}')
