from entidade.funcionario import Funcionario

class Medico(Funcionario):
    def __init__(self, nome: str, cpf: str, idade: int, rua: str, numero: int, complemento: str,
                 matricula: int, salario: int, crm: str):
        super().__init__(nome, cpf, idade, rua, numero, complemento, matricula, salario)
        if isinstance(crm, str):
            self.__crm = crm

    @property
    def crm(self):
        return self.__crm

    @crm.setter
    def crm(self, crm: str):
        if isinstance(crm, str):
            self.__crm = crm
