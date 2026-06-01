class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        novo_preco = self.preco - (self.preco * percentual / 100)
        return novo_preco


produto = Produto("Celular", 1000.0)

print(produto.desconto(10))
