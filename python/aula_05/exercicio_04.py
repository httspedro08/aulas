class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def apresentar(self):
        print("Aluno")
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("Matrícula:", self.matricula)
        print()


class Professor(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def apresentar(self):
        print("Professor")
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("Salário:", self.salario)
        print()


lista = [
    Aluno("João", 20, "2024001"),
    Professor("Maria", 45, 6000),
    Aluno("Ana", 22, "2024002"),
    Professor("Pedro", 50, 7500)
]

for pessoa in lista:
    pessoa.apresentar()