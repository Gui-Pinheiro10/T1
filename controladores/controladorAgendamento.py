from entidade.vacina import Vacina
from entidade.consulta import Consulta
from entidade.agendamento import Agendamento
from telas.telaAgendamento import TelaAgendamento
from controladores.controladorCliente import ControladorCliente
from controladores.controladorMedico import ControladorMedico
from controladores.controladorEnfermeiro import ControladorEnfermeiro


class ControladorAgendamento:
    def __init__(self, controlador_sistema):
        self.__tela_agendamento = TelaAgendamento()
        self.__agendamentos = []
        self.__controlador_sistema = controlador_sistema
        self.__controlador_cliente = ControladorCliente(self)
        self.__controlador_medico = ControladorMedico(self)
        self.__controlador_enfermeiro = ControladorEnfermeiro(self)

    def pega_agendamento_por_codigo(self, codigo: int):
        for agendamento in self.__agendamentos:
            if agendamento.codigo == codigo:
                return agendamento
        return None

    def inclui_agendamento(self):
        tipoAgendamento_agendamento = ''
        dados_agendamento = self.__tela_agendamento.pega_dados_agendamento()
        cliente_agendamento = self.__controlador_cliente.pega_cliente_por_codigo(dados_agendamento["codigo_cliente"])
        medico_agendamento = self.__controlador_medico.pega_medico_por_matricula(dados_agendamento["matricula_medico_ou_enfermeiro"])
        enfermeiro_agendamento = self.__controlador_enfermeiro.pega_enfermeiro_por_matricula(dados_agendamento["matricula_medico_ou_enfermeiro"])
        if dados_agendamento["numero_tipoAgendamento"] == 1:
            tipoAgendamento_agendamento == Consulta(dados_agendamento["nome_tipoAgendamento"], medico_agendamento)
            agendamento_para_incluir = Agendamento(dados_agendamento["horario"], dados_agendamento["valor"], dados_agendamento["data"], cliente_agendamento, tipoAgendamento_agendamento, dados_agendamento["codigo"])
        elif dados_agendamento["numero_tipoAgendamento"] == 2:
            tipoAgendamento_agendamento == Vacina(dados_agendamento["nome_tipoAgendamento"], enfermeiro_agendamento)
            agendamento_para_incluir = Agendamento(dados_agendamento["horario"], dados_agendamento["valor"], dados_agendamento["data"], cliente_agendamento, tipoAgendamento_agendamento, dados_agendamento["codigo"])
        for agendamento in self.__agendamentos:
            if  agendamento_para_incluir.codigo == agendamento.codigo:
                self.__tela_agendamento.mostra_mesagem('Não foi possível cadastrar o agendamento pois o código já existe!')
                break
            else:
                self.__agendamentos.append(agendamento_para_incluir)
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
        self.__tela_agendamento.mostra_mesagem("LISTA DE AGENDAMENTO".center(30, '-'))
        for agendamento in self.__agendamentos:
            self.__tela_agendamento.mostra_mesagem(f'Horário: {agendamento.horario} | Data: {agendamento.data} | Valor (R$): {agendamento.valor}\nCliente: {agendamento.cliente} | Código: {agendamento.codigo}')
        if len(self.__agendamentos) == 0:
            self.__tela_agendamento.mostra_mesagem("No momento a lista de agendamentos está vazia.")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela_agendamento(self):
        opcoes = {0: self.retornar, 1: self.inclui_agendamento, 2: self.altera_agendamento, 3: self.exclui_agendamento, 4: self.listar_agendamentos}
        while True:
            opcao = self.__tela_agendamento.tela_opcoes()
            funcao_escolhida = opcoes[opcao]
            funcao_escolhida()
