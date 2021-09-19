from DAOs.DAO import DAO
from entidade.limpeza import Limpeza


class LimpezaDAO(DAO):
    def __init__(self):
        super().__init__('limpeza.pkl')

    def add(self, limpeza: Limpeza):
        if ((limpeza is not None) and isinstance(limpeza, Limpeza) and isinstance(limpeza.cpf, str)):
            super().add(limpeza.cpf, limpeza)

    def update(self, limpeza: Limpeza):
        if ((limpeza is not None) and isinstance(limpeza, Limpeza) and isinstance(limpeza.cpf, str)):
            super().update(limpeza.cpf, limpeza)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: str):
        if (isinstance(key, str)):
            return super().remove(key)
