class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

produto1 = Produto("Salgado", 8.00)
produto2 = Produto("Refrigerante", 5.00)

print(produto1.nome)
print(produto1.preco)
print(produto2.nome)
print(produto2.preco)