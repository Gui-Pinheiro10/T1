from entidade.vacina import Vacina
from entidade.consulta import Consulta


class TipoAgendamento():
    def __init__(self, tipo: Vacina or Consulta):
        self.__tipo = tipo

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo: Vacina or Consulta):
        self.__tipo = tipo
