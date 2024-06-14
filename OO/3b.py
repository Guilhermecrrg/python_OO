class list (object):
    __num = []
    __mediap = 0
    __peso = []

    def __init__(self, l):
        self.__num = l
        self.__mediap = 0
        self.__peso = []

    def media_ponderada (self):
        tamanho = len(self.__num)
        cont = 0

        for n in self.__num:
            if(cont == 0 or cont == 1 or cont == (tamanho - 2) or cont == (tamanho - 1)):
                self.__num[cont] = (n * 0.3)
                self.__peso.append(0.3)
                cont= cont + 1
            else:
                self.__num[cont] = (n  * 0.1)
                self.__peso.append(0.1)
                cont= cont + 1

        self.__mediap = (sum(self.__num)) / (sum(self.__peso))
        return self.__mediap
    
    def len_list (self):
        return len(self.__num)
    
if __name__ == "__main__":

    num = list([float(n) for n in input().split()])
    if(num.len_list()>=5):
        print(num.media_ponderada())
    else:
        print("Digite no minimo 5 valores\n")