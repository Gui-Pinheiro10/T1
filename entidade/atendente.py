from entidade.funcionario import Funcionario


class Atendente(Funcionario):
    def __init__(self, nome: str, idade: int, cpf: str, rua: str, numero: int, complemento: str,
                 matricula: int, salario: float):
        super().__init__(nome, cpf, idade, rua, numero, complemento, matricula, salario)
