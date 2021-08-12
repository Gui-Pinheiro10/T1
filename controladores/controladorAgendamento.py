from entidade.agendamento import Agendamento
from telas.telaAgendamento import TelaAgendamento


class ControladorAgendamento(self):
    self.__tela_agendamento = TelaAgendamento(self)
    self.__agendamentos = []

    def inclui_agendamento(self, matricula):
        pass

    def exclui_agendamento(self, matricula):
        pass

    def altera_agendamento(self, matricula):
        pass

    def listar_agendamentos(self, matricula):
        pass

    def inicia(self):
        self.abre_tela_agendamento()

    def finalizar(self):
        pass
    
    def abre_tela_agendamento(self):
        opcoes = {0: self.finalizar, 1: self.inclui_agendamento, 2: self.altera_agendamento, 3: self.exclui_agendamento, 4: self.listar_agendamentos}
        while True:
            opcao = self.__tela_agendamento.mostra_tela_opcoes()
            funcao_escolhida = opcoes[opcao]
            funcao_escolhida()
