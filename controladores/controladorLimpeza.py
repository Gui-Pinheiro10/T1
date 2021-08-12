from entidade.limpeza import Limpeza
from telas.telaLimpeza import TelaLimpeza


class ControladorLimpeza:
    self.__tela_limpeza = TelaLimpeza(self)
    self.__limpezas = []

    def inclui_limpeza(self, matricula):
        pass

    def exclui_limpeza(self, matricula):
        pass

    def altera_limpeza(self, matricula):
        pass

    def listar_limpezas(self, matricula):
        pass

    def pega_limpeza_por_matricula(self, matricula):
        pass

    def inicia(self):
        self.abre_tela_limpeza()

    def finalizar(self):
        pass
    
    def abre_tela_limpeza(self):
        opcoes = {0: self.finalizar, 1: self.inclui_limpeza, 2: self.altera_limpeza, 3: self.exclui_limpeza, 4: self.listar_limpezas}
        while True:
            opcao = self.__tela_limpeza.mostra_tela_opcoes()
            funcao_escolhida = opcoes[opcao]
            funcao_escolhida()
