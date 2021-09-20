from entidade.tipoAgendamento import TipoAgendamento
from entidade.cliente import Cliente


class Agendamento():
    def __init__(self, horario: str, valor: int, data: str, cliente: Cliente, tipoAgendamento: TipoAgendamento, codigo: int):
        self.__horario = horario
        self.__valor = valor
        self.__data = data
        self.__cliente = cliente
        self.__tipoAgendamento = tipoAgendamento
        self.__codigo = codigo

    @property
    def horario(self):
        return self.__horario

    @horario.setter
    def horario(self, horario: str):
        if isinstance(horario, str):
            self.__horario = horario

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor: int):
        if isinstance(valor, int):
            self.__valor = valor

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data: str):
        if isinstance(data, str):
            self.__data = data

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente: Cliente):
        if isinstance(cliente, Cliente):
            self.__cliente = cliente

    @property
    def tipoAgendamento(self):
        return self.__tipoAgendamento
    
    @cliente.setter
    def cliente(self, tipoAgendamento: TipoAgendamento):
        if isinstance(tipoAgendamento, TipoAgendamento):
            self.__tipoAgendamento = tipoAgendamento

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        if isinstance(codigo, int):
            self.__codigo = codigo

