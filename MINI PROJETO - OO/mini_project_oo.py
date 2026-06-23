class Funcionario:
    #classe mãe com os atributos que todos os funcionarios possuem
    def __init__(self, nome, matricula, salario_fixo):
        #atributos privados
        self.__nome = nome 
        self.__matricula = matricula
        self.__salario_fixo = salario_fixo

    #getters (para acessar atributos privados)
    def get_nome(self):
        return self.__nome

    def get_matricula(self):
        return self.__matricula

    def get_salario_fixo(self):
        return self.__salario_fixo

    #setters (para alterar atributos privados)
    def set_nome(self, nome):
        self.__nome = nome

    def set_matricula(self, matricula):
        self.__matricula = matricula

    def set_salario_fixo(self, salario_fixo):
        if salario_fixo >= 0:
            self.__salario_fixo = salario_fixo
        else:
            print("O salário não pode ser negativo.")

    def calcular_salario(self):
        return self.__salario_fixo

    #exibir os dados dos funcionarios
    def exibir(self):
        print(
            f"Nome: {self.get_nome()} | "
            f"Matricula: {self.get_matricula()} | "
            f"Tipo: {self.__class__.__name__} | "
            f"Salario: R$ {self.calcular_salario():.2f}"
        )


#CLT, Vendedor e Gerente herdam de Funcionario
class CLT(Funcionario):
    def __init__(self, nome, matricula, salario_fixo):
        super().__init__(nome, matricula, salario_fixo)

    def calcular_salario(self):
        return self.get_salario_fixo()


class Vendedor(Funcionario):
    def __init__(self, nome, matricula, salario_fixo, vendas):
        super().__init__(nome, matricula, salario_fixo)
        self.vendas = vendas

    def calcular_salario(self):
        return self.get_salario_fixo() + (self.vendas * 0.10)


class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario_fixo):
        super().__init__(nome, matricula, salario_fixo)

    def calcular_salario(self):
        return self.get_salario_fixo() + 1500


#objetos

funcionarios = [
    CLT("Ana", "001", 3000),
    Vendedor("Bruno", "002", 2000, 12000),
    Gerente("Carla", "003", 5000)
]

#percorrer a lista

for funcionario in funcionarios:
    funcionario.exibir()

#polimorfismo = cada objeto executa sua própria versão do metodo (calcular_salario)
#super(): reaproveita o construtor da classe mae