import PySimpleGUI as sg
from telas.abstractTela import AbstractTela


class TelaSistema(AbstractTela):
    def __init__(self):
        self.__window = None
        self.init_components()

    def tela_opcoes(self):
        self.init_components()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['5']:
            opcao = 5
        if values['6']:
            opcao = 6
        if values['7']:
            opcao = 7
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def close(self):
        self.__window.Close()

    def init_components(self):
        sg.ChangeLookAndFeel('LightBrown2')
        layout = [
            [sg.Text('Bem vindo ao sistema da clínica médica!', font=("Garamond", 30))],
            [sg.Text('Escolha sua opção:', font=("Garamond", 25))],
            [sg.Radio("CLIENTES", "RD1", key='1', font=("Garamond", 18))],
            [sg.Radio("MÉDICOS", "RD1", key='2', font=("Garamond", 18))],
            [sg.Radio("LIMPEZA", "RD1", key='3', font=("Garamond", 18))],
            [sg.Radio("ENFERMEIROS", "RD1", key='4', font=("Garamond", 18))],
            [sg.Radio("ATENDENTES", "RD1", key='5', font=("Garamond", 18))],
            [sg.Radio("AGENDAMENTO", "RD1", key='6', font=("Garamond", 18))],
            [sg.Radio("CLIENTES COM AGENDAMENTOS", "RD1", key='7', font=("Garamond", 18))],
            [sg.Radio("FINALIZAR SISTEMA", "RD1", key='0', font=("Garamond", 18))],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema Clínica Médica').Layout(layout)

    def mostra_cliente_com_agendamento(self, dados_clientes_com_agendamento):
        string_todos_clientes_com_agendamento = ""
        for dado in dados_clientes_com_agendamento:
            string_todos_clientes_com_agendamento = string_todos_clientes_com_agendamento + "NOME DO CLIENTE: " + dado["nome_cliente"] + '\n'
            string_todos_clientes_com_agendamento = string_todos_clientes_com_agendamento + "CPF DO CLIENTE: " + dado["cpf_cliente"] + '\n'
            string_todos_clientes_com_agendamento = string_todos_clientes_com_agendamento + "CÓDIGO DO AGENDAMENTO: " + str(dado["agendamento_codigo"]) + '\n'
            string_todos_clientes_com_agendamento = string_todos_clientes_com_agendamento + "HORÁRIO: " + str(dado["agendamento_horario"]) + '\n'
            string_todos_clientes_com_agendamento = string_todos_clientes_com_agendamento + "DATA : " + str(dado["agendamento_data"]) + '\n\n'

        sg.Popup('-------- LISTA DE CLIENTES COM AGENDAMENTO ----------', string_todos_clientes_com_agendamento)