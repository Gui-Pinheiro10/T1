from abc import ABC, abstractmethod
from pessoa import Pessoa


class Funcionario(Pessoa, ABC):
    @abstractmethod
    def __init__(self, matricula: int, salario: float):
        super().__init__() ##arrumar classe Pessoa para terminar aqui
        self.__matricula = matricula
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
