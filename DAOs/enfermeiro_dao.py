from DAOs.dao import DAO
from entidade.enfermeiro import Enfermeiro


class EnfermeiroDAO(DAO):
    def __init__(self):
        super().__init__('enfermeiro.pkl')

    def add(self, enfermeiro: Enfermeiro):
        if ((enfermeiro is not None) and isinstance(enfermeiro, Enfermeiro) and isinstance(enfermeiro.cpf, int)):
            super().add(enfermeiro.cpf, enfermeiro)

    def update(self, enfermeiro: Enfermeiro):
        if ((enfermeiro is not None) and isinstance(enfermeiro, Enfermeiro) and isinstance(enfermeiro.cpf, int)):
            super().update(enfermeiro.cpf, enfermeiro)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key: int):
        if (isinstance(key, int)):
            return super().remove(key)
