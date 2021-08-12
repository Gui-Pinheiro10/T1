from entidade.enfermeiro import Enfermeiro
from telas.telaEnfermeiro import TelaEnfermeiro


class ControladorEnfermeiro:
    self.__tela_enfermeiro = TelaEnfermeiro(self)
    self.__enfermeiros = []

    def inclui_enfermeiro(self, matricula):
        pass

    def exclui_enfermeiro(self, matricula):
        pass

    def altera_enfermeiro(self, matricula):
        pass

    def listar_enfermeiros(self, matricula):
        pass

    def pega_enfermeiro_por_matricula(self, matricula):
        pass

    def inicia(self):
        self.abre_tela_enfermeiro()
    
    def finalizar(self):
        pass

    def abre_tela_enfermeiro(self):
        opcoes = {0: self.finalizar, 1: self.inclui_enfermeiro, 2: self.altera_enfermeiro, 3: self.exclui_enfermeiro, 4: self.listar_enfermeiros}
        while True:
            opcao = self.__tela_enfermeiro.mostra_tela_opcoes()
            funcao_escolhida = opcoes[opcao]
            funcao_escolhida()
