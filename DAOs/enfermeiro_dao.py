from DAOs.DAO import DAO
from entidade.enfermeiro import Enfermeiro


class EnfermeiroDAO(DAO):
    def __init__(self):
        super().__init__('enfermeiro.pkl')

    def add(self, enfermeiro: Enfermeiro):
        if ((enfermeiro is not None) and isinstance(enfermeiro, Enfermeiro) and isinstance(enfermeiro.cpf, str)):
            super().add(enfermeiro.cpf, enfermeiro)

    def update(self, enfermeiro: Enfermeiro):
        if ((enfermeiro is not None) and isinstance(enfermeiro, Enfermeiro) and isinstance(enfermeiro.cpf, str)):
            super().update(enfermeiro.cpf, enfermeiro)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: str):
        if (isinstance(key, str)):
            return super().remove(key)
