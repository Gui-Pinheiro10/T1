from DAOs.dao import DAO
from entidade.atendente import Atendente


class AtendenteDAO(DAO):
    def __init__(self):
        super().__init__('atendentes.pkl')

    def add(self, atendente: Atendente):
        if((atendente is not None) and isinstance(atendente, Atendente) and isinstance(atendente.cpf, str)):
            super().add(atendente.cpf, atendente)

    def update(self, atendente: Atendente):
        if((atendente is not None) and isinstance(atendente, Atendente) and isinstance(atendente.cpf, str)):
            super().update(atendente.cpf, atendente)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)