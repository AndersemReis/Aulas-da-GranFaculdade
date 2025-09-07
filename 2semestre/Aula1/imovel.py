class Categoria:
    def __init__(self,tipo = ''):
        self.tipo = tipo

    def taxaAgua(self):
        match self.tipo:
            case 'Clinica': return 1
            case 'Restaurante' : return 2
            case 'Hotal' : return 2.5

class Imovel:

    def __init__(self, nome, quartos, suites):
        self.nome = nome 
        self.quartos = quartos
        self.suites = suites

    def __add__(self, other):
        somaSelf = self.quartos + self.suites
        somaOther = other.quartos + other.suites
        return somaSelf + somaOther
    
    def __gt__(self, other):
        somaSelf = self.quartos + self.suites
        somaOther = other.quartos + other.suites
        return somaSelf > somaOther

    def __lt__(self, other):
        somaSelf = self.quartos + self.suites
        somaOther = other.quartos + other.suites
        return somaSelf < somaOther
    
    def detalhar(self):
        return self.__dict__
    
    def somarAposentos(self):
        return self.quartos + self.suites
    
    @staticmethod
    def metodoEstatico():
        print("Chamou o metodo estatico")
        

casarao = Imovel("Casarão",3,4)
casarao = Imovel("Casarão 1",8,5)
mansao = Imovel("Mansão",4,5)

print(casarao.somarAposentos())
categoria = Categoria("Hotel")
hotel = Imovel("Hotel do chico", 0, 150)
hotel.categoria = categoria
print(hotel)

'''
print(mansao.__dict__)
print(casarao.__dict__)
soma = casarao.quartos + mansao.quartos
print(soma)
print(casarao > mansao)
print(casarao < mansao)
'''
Imovel.metodoEstatico()