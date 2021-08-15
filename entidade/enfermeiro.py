from funcionario import Funcionario


class Enfermeiro(Funcionario):
    def __init__(self, nome, cpf, idade, rua, numero, complemento, matricula, salario):
        super().__init__(nome, cpf, idade, rua, numero, complemento, matricula, salario)
