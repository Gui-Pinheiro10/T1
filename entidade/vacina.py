from medico import Medico


class Vacina():
    def __init__(self, tipo_da_vacina: str, medico: Medico):
        self.__tipo_da_vacina = tipo_da_vacina
        self.__medico = medico
    
    @property
    def tipo_da_vacina(self):
        return self.__tipo_da_vacina

    @tipo_da_vacina.setter
    def tipo_da_vacina(self, tipo_da_vacina: str):
        self.__tipo_da_vacina = tipo_da_vacina
    
    @property
    def medico(self):
        return self.__medico

    @medico.setter
    def medico(self, medico: Medico):
        self.__medico = medico
