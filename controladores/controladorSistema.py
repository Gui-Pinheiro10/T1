from telas.telaSistema import TelaSistema
from controladores.controladorCliente import ControladorCliente
from controladores.controladorMedico import ControladorMedico
from controladores.controladorLimpeza import ControladorLimpeza
from controladores.controladorEnfermeiro import ControladorEnfermeiro
from controladores.controladorAtendente import ControladorAtendente
from controladores.controladorAgendamento import ControladorAgendamento


class ControladorSistema:
    def __init__(self):
        self.__controlador_cliente = ControladorCliente(self)
        self.__controlador_medico = ControladorMedico(self)
        self.__controlador_limpeza = ControladorLimpeza(self)
        self.__controlador_enfermeiro = ControladorEnfermeiro(self)
        self.__controlador_atendente = ControladorAtendente(self)
        self.__controlador_agendamento = ControladorAgendamento(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_cliente(self):
        return self.__controlador_cliente

    def cadastro_cliente(self):
        self.__controlador_cliente.abre_tela() # chama o controlador de Clientes

    def cadastro_medico(self):
        self.__controlador_medico.abre_tela() # chama o controlador de Médicos

    def cadastro_limpeza(self):
        self.__controlador_limpeza.abre_tela() # chama o controlador de Limpeza

    def cadastro_enfermeiro(self):
        self.__controlador_enfermeiro.abre_tela_enfermeiro() # chama o controlador de Enfermeiros

    def cadastro_atendente(self):
        self.__controlador_atendente.abre_tela() # chama o controlador de Atendente

    def cadastro_agendamento(self):
        self.__controlador_agendamento.abre_tela_agendamento() # chama o controlador de Agendamentos

    def inicializa_sistema(self):
        self.abre_tela()

    def encerra_sistema(self):
        self.__tela_sistema.mostra_mesagem('SISTEMA ENCERRADO!')
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastro_cliente, 2: self.cadastro_medico, 3: self.cadastro_limpeza, 4: self.cadastro_enfermeiro, 5: self.cadastro_atendente, 6: self.cadastro_agendamento, 7: self.clientes_com_agendamentos, 0: self.encerra_sistema}
        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def retorna_lista_clientes_sistema(self):
        return self.__controlador_cliente.retorna_lista_clientes()

    def retorna_lista_medicos_sistema(self):
        return self.__controlador_medico.retorna_lista_medicos()

    def retorna_lista_enfermeiros_sistema(self):
        return self.__controlador_enfermeiro.retorna_lista_enfermeiros()

    def clientes_com_agendamentos(self):
        dados_clientes_com_agendamento = []
        try:
            if len(self.__controlador_agendamento.retorna_lista_agendamentos()) == 0:
                raise Exception
        except Exception:
            self.__tela_enfermeiro.mostra_mesagem("No momento não existem agendamentos marcados.")
        else:
            for cliente in self.__controlador_cliente.retorna_lista_clientes():
                for agendamento in self.__controlador_agendamento.retorna_lista_agendamentos():
                    if cliente.cpf == agendamento.cliente.cpf:
                        dados_clientes_com_agendamento.append({"nome_cliente": cliente.nome, "cpf_cliente": cliente.cpf,
                                                               "agendamento_codigo": agendamento.codigo, "agendamento_horario": agendamento.horario,
                                                               "agendamento_data": agendamento.data})
            self.__tela_sistema.mostra_cliente_com_agendamento(dados_clientes_com_agendamento)
