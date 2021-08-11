from pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome: str, cpf: int, rua: str, numero: int, complemento: str, idade: int,  codigo: int):
        super().__init__(nome, cpf, rua, numero, complemento, idade)
        if isinstance(codigo, int):
            self.__codigo = codigo

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        if isinstance(codigo, int):
            self.__codigo = codigo
