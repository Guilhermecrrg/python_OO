class Imovel(object):
    __inscricao = 0
    __area = 0.0
    __valor_m2 = 0.0

    def __init__(self, i, a, v):
        self.__inscricao = i
        self.__area = a
        self.__valor_m2 = v

    def calcularIPTU(self):
        return self.__area * self.__valor_m2

    def exibir(self):
        return f'Numero de inscrição: {self.__inscricao}'
    
class Casa(Imovel):
    __area_construida = 0.0
    __taxa_construcao = 0.0

    def __init__(self, i, a, v, ac, tc):
        super().__init__(i, a, v)
        self.__area_construida = ac
        self.__taxa_construcao = tc

    def calcularIPTU(self):
        return super().calcularIPTU() + self.__area_construida * self.__taxa_construcao 

    
if __name__ == "__main__":
    im1 = Imovel(1, 200.5, 40.5)
    im2 = Imovel(2, 400.9, 30.8)
    im3 = Imovel(3, 500.7, 67.5)
    cs1 = Casa(4, 300, 40.3, 100, 30.2)
    cs2 = Casa(5, 230, 23.5, 90.5, 45.7)
    
    IPTU_total = 0
    imoveis = [im1, im2, im3, cs1 , cs2]

    for im in imoveis:
        print(im.exibir())
        print(f'Valor do IPTU: R${im.calcularIPTU():.2f}\n')
        IPTU_total = im.calcularIPTU() + IPTU_total

    print(f"Valor total dos IPTU: R${IPTU_total:.2f}\n")