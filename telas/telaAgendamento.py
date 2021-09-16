from telas.abstractTela import AbstractTela
import PySimpleGUI as sg


class TelaAgendamento(AbstractTela):
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
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_components(self):
        # sg.theme_previewer()
        sg.ChangeLookAndFeel('LightBrown2')
        layout = [
            [sg.Text('SISTEMA DE CONTROLE DE AGENDAMENTOS', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Inserir Agendamento', "RD1", key='1')],
            [sg.Radio('Alterar Agendamento', "RD1", key='2')],
            [sg.Radio('Excluir Agendamento', "RD1", key='3')],
            [sg.Radio('Listar Agendamentos', "RD1", key='4')],
            [sg.Radio('Finalizar sistema', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de controle dos Agendamentos').Layout(layout)

    def pega_dados_agendamento(self):
        sg.ChangeLookAndFeel('LightBrown2')
        layout = [
            [sg.Text('---------- DADOS DO AGENDAMENTO ----------', font=("Helvica", 15))],
            [sg.Text('Horário:', size=(15, 1)), sg.InputText('', key='horario')],
            [sg.Text('Data:', size=(15, 1)), sg.InputText('', key='data')],
            [sg.Text('Código do Cliente:', size=(15, 1)), sg.InputText('', key='codigo_cliente')],
            [sg.Text('Matrícula do Médico ou Enfermeiro:', size=(15, 1)), sg.InputText('', key='matricula_medico_ou_enfermeiro')],
            [sg.Text('Digite apenas 1 ou 2 - [1] Vacina [2] Consulta:', size=(15, 1)), sg.InputText('', key='numero_tipoAgendamento')],
            [sg.Text('Digite a especialidade ou tipo de vacina:', size=(15, 1)), sg.InputText('', key='nome_tipoAgendamento')],
            [sg.Text('Código:', size=(15, 1)), sg.InputText('', key='codigo')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Dados do Agendamento').Layout(layout)

        button, values = self.open()

        horario = values['horario']
        data = values['data']
        codigo_cliente = values['codigo_cliente']
        matricula_medico_ou_enfermeiro = values['matricula_medico_ou_enfermeiro']
        numero_tipoAgendamento = values['numero_tipoAgendamento']
        nome_tipoAgendamento = values['nome_tipoAgendamento']
        codigo = values['codigo']

        self.close()

        return {"horario": horario, "data": data, "codigo": codigo, "codigo_cliente": codigo_cliente, "numero_tipoAgendamento": numero_tipoAgendamento, "nome_tipoAgendamento": nome_tipoAgendamento, "matricula_medico_ou_enfermeiro": matricula_medico_ou_enfermeiro}

    def pega_dados_para_alterar_agendamento(self):
        sg.ChangeLookAndFeel('LightBrown2')
        layout = [
            [sg.Text('---------- DADOS DO AGENDAMENTO ----------', font=("Helvica", 15))],
            [sg.Text('Horário:', size=(15, 1)), sg.InputText('', key='horario')],
            [sg.Text('Data:', size=(15, 1)), sg.InputText('', key='data')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Dados para alterar o agendamento').Layout(layout)

        button, values = self.open()

        horario = values['horario']
        data = values['data']
        return {"horario": horario, "data": data}

    def seleciona_agendamento(self):
        sg.ChangeLookAndFeel('LightBrown2')
        layout = [
            [sg.Text('-------- SELECIONAR AGENDAMENTO ----------', font=("Helvica", 25))],
            [sg.Text('Digite o código do agendamento que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('Código:', size=(15, 1)), sg.InputText('', key='codigo_agendamento')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona Agendamento').Layout(layout)

        button, values = self.open()
        codigo_agendamento = values['codigo_agendamento']
        self.close()
        return codigo_agendamento

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()
