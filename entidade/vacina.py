from entidade.enfermeiro import Enfermeiro


class Vacina():
    def __init__(self, tipo_da_vacina: str, enfermeiro: Enfermeiro):
        self.__tipo_da_vacina = tipo_da_vacina
        self.__enfermeiro = enfermeiro
    
    @property
    def tipo_da_vacina(self):
        return self.__tipo_da_vacina

    @tipo_da_vacina.setter
    def tipo_da_vacina(self, tipo_da_vacina: str):
        self.__tipo_da_vacina = tipo_da_vacina
    
    @property
    def enfermeiro(self):
        return self.__enfermeiro

    @enfermeiro.setter
    def enfermeiro(self, enfermeiro: Enfermeiro):
        self.__enfermeiro = enfermeiro
