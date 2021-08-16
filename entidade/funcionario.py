from abc import ABC, abstractmethod
from entidade.pessoa import Pessoa


class Funcionario(Pessoa, ABC):
    @abstractmethod
    def __init__(self, nome: str, cpf: str, idade: int, rua: str, numero: int, complemento: str, matricula: int, salario: float):
        super().__init__(nome, cpf, idade, rua, numero, complemento)
        if isinstance(matricula, int):
            self.__matricula = matricula
        if isinstance(salario, float):
            self.__salario = salario

    @property
    def matricula(self):
        return self.__matricula
    
    @matricula.setter
    def matricula(self, matricula: int):
        if isinstance(matricula, int):
            self.__matricula = matricula
    
    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, salario: float):
        if isinstance(salario, float):
            self.__salario = salario
