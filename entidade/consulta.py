from entidade.medico import Medico


class Consulta():
    def __init__(self, especialidade: str, medico: Medico):
        self.__especialidade = especialidade
        self.__medico = medico
    
    @property
    def especialidade(self):
        return self.__especialidade

    @especialidade.setter
    def especialidade(self, especialidade: str):
        self.__especialidade = especialidade
    
    @property
    def medico(self):
        return self.__medico

    @medico.setter
    def medico(self, medico: Medico):
        self.__medico = medico
