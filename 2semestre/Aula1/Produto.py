class Produto:
    def __init__(self):
        self._nome = ""
        self._marca = ""
        self._quantidade = ""
        self._modelo = ""
        self._valor = ""


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self,nome):
        self._nome = nome

    def vender(self, quantidade):
        if (quantidade > self.quantidade):
            print("Não temos estoque")
        else:
            self.quantidade -= quantidade
    
    def comprar(self,quantidade):
        self.quantidade += quantidade



produto = Produto()

produto.total = "LG"
print(produto)