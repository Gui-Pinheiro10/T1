from abc import ABC, abstractmethod
from endereco import Endereco

class Pessoa(Endereco, ABC):
    @abstractmethod
    def __init__(self, nome: str, cpf: int, rua: str, numero: int, complemento: str, idade: int):
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(cpf, int):
            self.__cpf = cpf
        if isinstance(idade, int):
            self.__idade = idade
        self.__endereco = Endereco(rua, numero, complemento)

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: int):
        if isinstance(cpf, int):
            self.__cpf = cpf

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco: str):
        if isinstance(endereco, str):
            self.__endereco = endereco
