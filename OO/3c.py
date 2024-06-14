class Quadrilatero (object):
    __base = 0.0
    __altura = 0.0

    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    def calcular_area(self):
        return self.__base * self.__altura

    def calcular_perimetro(self):
        return (2 * self.__base) + (2 * self.__altura) 
    
    def voltar_altura(self):
        return self.__altura
    
    def voltar_base(self):
        return self.__base
    
class Quadrado (Quadrilatero):

    def __init__(self, tamanho):
        super().__init__(tamanho, tamanho)

class Trapezio (Quadrilatero):
    __base_menor = 0.0

    def __init__(self, base, base_menor, altura):
        super().__init__(base, altura)
        self.__base_menor = base_menor

    def calcular_area(self):
        return (((super().voltar_base() + self.__base_menor)* super().voltar_altura())/2)   

if __name__ == "__main__":
    q1 = Quadrilatero(2.4,1.5)
    q2 = Quadrado(2)
    q3 = Trapezio(2,3,4)
    i = 0
    nome = ["Quadrilatero", "Quadrado", "Trapezio"]
    quadrilateros = [q1,q2,q3]

    for q in quadrilateros:
        print(f"{nome[i]}")
        print(f"Area = {q.calcular_area():.2f}")
        print(f'Perimetro = {q.calcular_perimetro():.2f}\n')
        i = i +1 
