from entidade.tipoAgendamento import TipoAgendamento
from entidade.cliente import Cliente
from datetime import date


class Agendamento():
    def __init__(self, horario: date, valor: int, data: date, cliente: Cliente, tipoAgendamento: TipoAgendamento, codigo: int):
        self.__horario = horario
        self.__valor = valor
        self.__data = data
        self.__cliente = cliente # mudei Cliente para cliente
        self.__tipoAgendamento = tipoAgendamento
        self.__codigo = codigo

    @property
    def horario(self):
        return self.__horario

    @horario.setter
    def horario(self, horario: date):
        if isinstance(horario, date):
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
    def data(self, data: date):
        if isinstance(data, date):
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

