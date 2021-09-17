from DAOs.dao import DAO
from entidade.medico import Medico


class MedicoDAO(DAO):
    def __init__(self):
        super().__init__('medicos..pkl')

    def add(self, medico: Medico):
        if ((medico is not None) and isinstance(medico, Medico) and isinstance(medico.cpf, str)):
            super().add(medico.cpf, medico)

    def update(self, medico: Medico):
        if ((medico is not None) and isinstance(medico, Medico) and isinstance(medico.cpf, str)):
            super().update(medico.cpf, medico)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if (isinstance(key, str)):
            return super().remove(key)
