from entidade.pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome: str, cpf: str, idade: int, rua: str, numero: int, complemento: str):
        super().__init__(nome, cpf, idade, rua, numero, complemento)
