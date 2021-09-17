from DAOs.DAO import DAO
from entidade.agendamento import Agendamento


class AgendamentoDAO(DAO):
    def __init__(self):
        super().__init__('agendamento.pkl')

    def add(self, agendamento: Agendamento):
        if ((agendamento is not None) and isinstance(agendamento, Agendamento) and isinstance(agendamento.codigo, int)):
            super().add(agendamento.codigo, agendamento)

    def update(self, agendamento: Agendamento):
        if ((agendamento is not None) and isinstance(agendamento, Agendamento) and isinstance(agendamento.codigo, int)):
            super().update(agendamento.codigo, agendamento)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key: int):
        if (isinstance(key, int)):
            return super().remove(key)
