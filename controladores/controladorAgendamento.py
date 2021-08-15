from entidade import agendamento
from entidade.agendamento import Agendamento
from telas.telaAgendamento import TelaAgendamento
from controladorSistema import ControladorSistema


class ControladorAgendamento:
    def __init__(self, controlador_sistema: ControladorSistema):
        self.__tela_agendamento = TelaAgendamento(self)
        self.__agendamentos = []
        self.__controlador_sistema = controlador_sistema

    def pega_agendamento_por_codigo(self, codigo: int):
        for agendamento in self.__agendamentos:
            if agendamento.codigo == codigo:
                return agendamento
        return None

    def inclui_agendamento(self):
        dados_agendamento = self.__tela_agendamento.pega_dados_agendamento()
        codigo_agendamento = self.__tela_agendamento.seleciona_agendamento()
        agendamento = Agendamento(dados_agendamento["horario"], dados_agendamento["valor"], dados_agendamento["data"], dados_agendamento["cliente"], dados_agendamento["tipoAgendamento"], dados_agendamento["codigo"])
        for agendamento in self.__agendamentos:
            if codigo_agendamento == agendamento.codigo:
                self.__tela_agendamento.mostra_mesagem('Não foi possível cadastrar o agendamento pois o código já existe!')
                break
            else:
                self.__agendamentos.append(agendamento)
                self.__tela_agendamento.mostra_mesagem('Agendamento cadastrado com sucesso!')

    def exclui_agendamento(self):
        self.listar_agendamentos()
        codigo_agendamento_excluido = self.__tela_agendamento.seleciona_agendamento()
        agendamento_excluido = self.pega_agendamento_por_codigo(codigo_agendamento_excluido)
        for agendamento in self.__agendamentos:
            if agendamento.codigo == codigo_agendamento_excluido:
                self.__agendamentos.remove(agendamento_excluido)
                self.__tela_agendamento.mostra_mesagem('Agendamento excluído com sucesso!')
                self.listar_agendamentos()
            else:
                self.__tela_agendamento.mostra_mesagem('Não foi possível excluir o agendamento, pois o código informado não está na lista!')

    def altera_agendamento(self):
        codigo_agendamento_alterado = self.__tela_agendamento.seleciona_agendamento()
        agendamento_alterado = self.pega_agendamento_por_codigo(codigo_agendamento_alterado)
        if agendamento_alterado is not None:
            dados_agendamento = self.__tela_agendamento.pega_dados_para_alterar_agendamento()
            agendamento_alterado.horario = dados_agendamento["horario"]
            agendamento_alterado.data = dados_agendamento["data"]
            agendamento_alterado.valor = dados_agendamento["valor"]
            agendamento_alterado.cliente = dados_agendamento["cliente"]
            agendamento_alterado.tipoAgendamento = dados_agendamento["tipoAgendamento"]
            self.__tela_agendamento.mostra_mesagem('Agendamento alterado com sucesso!\n')
        else:
            self.__tela_agendamento.mostra_mesagem('Não foi possível alterar o agendamento, pois o código informado não está na lista!')

    def listar_agendamentos(self):
        print('Listagem de agendamentos cadastrados:\n')
        for agendamento in self.__agendamentos:
            print(f'Horário: {agendamento.horario} | Data: {agendamento.data} | Valor: {agendamento.valor} | Código: {agendamento.codigo} ')

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela_agendamento(self):
        opcoes = {0: self.retornar, 1: self.inclui_agendamento, 2: self.altera_agendamento, 3: self.exclui_agendamento, 4: self.listar_agendamentos}
        while True:
            opcao = self.__tela_agendamento.mostra_tela_opcoes()
            funcao_escolhida = opcoes[opcao]
            funcao_escolhida()
