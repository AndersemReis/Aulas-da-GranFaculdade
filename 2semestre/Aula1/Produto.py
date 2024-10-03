class Produto:
    def __init__(self):
        self.nome = ""
        self.marca = ""
        self.quantidade = ""
        self.modelo = ""
        self.valor = ""

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