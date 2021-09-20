from entidade.vacina import Vacina
from entidade.consulta import Consulta
from entidade.agendamento import Agendamento
from telas.telaAgendamento import TelaAgendamento
from DAOs.agendamenteo_dao import AgendamentoDAO
from Cliente_ou_Medico_Enfermeiro_Nao_Existe import ClienteOuMedicoEnfermeiroNaoExiste


class ControladorAgendamento:
    def __init__(self, controlador_sistema):
        self.__tela_agendamento = TelaAgendamento()
        self.__controlador_sistema = controlador_sistema
        self.__agendamento_DAO = AgendamentoDAO()

    def pega_agendamento_por_codigo(self, codigo: int):
        for agendamento in self.__agendamento_DAO.get_all():
            if agendamento.codigo == codigo:
                return agendamento
        return None

    def inclui_agendamento(self):
        cliente_agendamento = ''
        medico_agendamento = ''
        enfermeiro_agendamento = ''
        lista_de_clientes = self.__controlador_sistema.retorna_lista_clientes_sistema()
        lista_de_medicos = self.__controlador_sistema.retorna_lista_medicos_sistema()
        lista_de_enfemeiros = self.__controlador_sistema.retorna_lista_enfermeiros_sistema()
        dados_agendamento = self.__tela_agendamento.pega_dados_agendamento()
        for cliente in lista_de_clientes:
            if dados_agendamento["cpf_cliente"] == cliente.cpf:
                cliente_agendamento = cliente
                break
        if dados_agendamento["numero_tipoAgendamento"] == 2:
            for medico in lista_de_medicos:
                if dados_agendamento["cpf_medico_ou_enfermeiro"] == medico.cpf:
                    medico_agendamento = medico
                    break
            tipoAgendamento_agendamento = Consulta(dados_agendamento["nome_tipoAgendamento"],
                                                 medico_agendamento)
            agendamento_para_incluir = Agendamento(dados_agendamento["horario"], 150, dados_agendamento["data"],
                                                   cliente_agendamento, tipoAgendamento_agendamento,
                                                   dados_agendamento["codigo"])
        elif dados_agendamento["numero_tipoAgendamento"] == 1:
            for enfermeiro in lista_de_enfemeiros:
                if dados_agendamento["cpf_medico_ou_enfermeiro"] == enfermeiro.cpf:
                    enfermeiro_agendamento = enfermeiro
                    break
            tipoAgendamento_agendamento = Vacina(dados_agendamento["nome_tipoAgendamento"],
                                                 enfermeiro_agendamento)
            agendamento_para_incluir = Agendamento(dados_agendamento["horario"], 150, dados_agendamento["data"],
                                                   cliente_agendamento, tipoAgendamento_agendamento,
                                                   dados_agendamento["codigo"])
        try:
            if agendamento_para_incluir.cliente == '' or (enfermeiro_agendamento == '' and medico_agendamento == ''):
                raise ClienteOuMedicoEnfermeiroNaoExiste()
            for agendamento in self.__agendamento_DAO.get_all():
                if agendamento.codigo == agendamento_para_incluir.codigo or (tipoAgendamento_agendamento == 0) or (agendamento.data == agendamento_para_incluir.data and agendamento.horario == agendamento_para_incluir.horario):
                    raise Exception
        except ClienteOuMedicoEnfermeiroNaoExiste:
            self.__tela_agendamento.mostra_mesagem('Cliente ou Médico/Enfermeiros não cadastrados!')
        except Exception:
            self.__tela_agendamento.mostra_mesagem('Não foi possível cadastrar o agendamento pois o código ou horário já existe ou o tipo de agendamento não foi selecionado!')
        else:  
            self.__agendamento_DAO.add(agendamento_para_incluir)
            self.__tela_agendamento.mostra_mesagem('Agendamento cadastrado com sucesso!')

    def exclui_agendamento(self):
        self.listar_agendamentos()
        codigo_agendamento_excluido = self.__tela_agendamento.seleciona_agendamento()
        agendamento_excluido = self.pega_agendamento_por_codigo(codigo_agendamento_excluido)
        try:
            if agendamento_excluido is None:
                raise Exception
        except Exception:
            self.__tela_agendamento.mostra_mesagem('Não foi possível excluir o agendamento, pois o código informado não está na lista!')
        else:
            for agendamento in self.__agendamento_DAO.get_all():
                if agendamento.codigo == codigo_agendamento_excluido:
                    self.__agendamento_DAO.remove(agendamento_excluido.codigo)
                    self.__tela_agendamento.mostra_mesagem('Agendamento excluído com sucesso!')
                    self.listar_agendamentos()
                    break

    def altera_agendamento(self):
        self.listar_agendamentos()
        codigo_agendamento_alterado = self.__tela_agendamento.seleciona_agendamento()
        agendamento_alterado = self.pega_agendamento_por_codigo(codigo_agendamento_alterado)
        try:
            if agendamento_alterado is None:
                raise Exception
        except Exception:
            self.__tela_agendamento.mostra_mesagem('Não foi possível alterar o agendamento, pois o código informado não está na lista!')
        else:
            dados_agendamento = self.__tela_agendamento.pega_dados_para_alterar_agendamento()
            agendamento_alterado.horario = dados_agendamento["horario"]
            agendamento_alterado.data = dados_agendamento["data"]
            self.__tela_agendamento.mostra_mesagem('Agendamento alterado com sucesso!\n')

    def listar_agendamentos(self):
        dados_agendamentos = []
        try:
            if len(self.__agendamento_DAO.get_all()) == 0:
                raise Exception
        except Exception:
            self.__tela_agendamento.mostra_mesagem("No momento a lista de agendamentos está vazia.")
        else:
            for agendamento in self.__agendamento_DAO.get_all():
                dados_agendamentos.append({"horario": agendamento.horario, "data": agendamento.data,
                                          "valor": agendamento.valor, "codigo": agendamento.codigo,
                                          "cliente": agendamento.cliente.nome})
            self.__tela_agendamento.mostra_agendamento(dados_agendamentos)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela_agendamento(self):
        opcoes = {0: self.retornar, 1: self.inclui_agendamento, 2: self.altera_agendamento, 3: self.exclui_agendamento, 4: self.listar_agendamentos}
        while True:
            opcao = self.__tela_agendamento.tela_opcoes()
            funcao_escolhida = opcoes[opcao]
            funcao_escolhida()
