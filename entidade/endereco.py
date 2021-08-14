class Endereco:
    def __init__(self, rua: str, numero: int, complemento: str):
        if isinstance(rua, str):
            self.__rua = rua
        if isinstance(numero, int):
            self.__numero = numero
        if isinstance(complemento, str):
            self.__complemento = complemento

    @property
    def rua(self):
        return self.__rua

    @property
    def numero(self):
        return self.__numero

    @property
    def complemento(self):
        return self.__complemento

    @rua.setter
    def rua(self, rua: str):
        if isinstance(rua, str):
            self.__rua = rua

    @numero.setter
    def numero(self, numero: int):
        if isinstance(numero, int):
            self.__numero = numero

    @complemento.setter
    def complemento(self, complemento: str):
        if isinstance(complemento, str):
            self.__complemento = complemento
            
