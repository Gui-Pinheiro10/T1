from telas.abstractTela import AbstractTela
import PySimpleGUI as sg


class TelaAtendente(AbstractTela):

    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
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

    def init_opcoes(self):
        sg.ChangeLookAndFeel('LightBrown2')
        layout = [
            [sg.Text('-------- CADASTRO DE ATENDENTES ----------', font=("Garamond", 25, 'bold'))],
            [sg.Text('Escolha sua opção:', font=("Garamond", 20, 'bold'))],
            [sg.Radio('Adicionar Atendente', "RD1", key='1', font=("Garamond", 18))],
            [sg.Radio('Alterar Atendente', "RD1", key='2', font=("Garamond", 18))],
            [sg.Radio('Excluir Atendente', "RD1", key='3', font=("Garamond", 18))],
            [sg.Radio('Lista de Atendentes', "RD1", key='4', font=("Garamond", 18))],
            [sg.Radio('Retornar', "RD1", key='0', font=("Garamond", 18))],
            [sg.Button('Confirmar', font=("Garamond", 15, 'bold')), sg.Cancel('Cancelar', font=("Garamond", 15, 'bold'))]
        ]
        self.__window = sg.Window('Sistema de Cadastro de Atendentes').Layout(layout)

    def pega_dados_atendente(self):
        sg.ChangeLookAndFeel('LightBrown2')
        layout = [
            [sg.Text('--------- DADOS ATENDENTE ----------', font=("Garamond", 25, 'bold'))],
            [sg.Text('Nome:', size=(15, 1), font=("Garamond", 18)), sg.InputText('', key='nome')],
            [sg.Text('CPF:', size=(15, 1), font=("Garamond", 18)), sg.InputText('', key='cpf')],
            [sg.Text('Idade:', size=(15, 1), font=("Garamond", 18)), sg.InputText('', key='idade')],
            [sg.Text('Rua:', size=(15, 1), font=("Garamond", 18)), sg.InputText('', key='rua')],
            [sg.Text('Número:',size=(15,1), font=("Garamond", 18)), sg.InputText('', key='numero')],
            [sg.Text('Complemento:',size=(15,1), font=("Garamond", 18)), sg.InputText('', key='complemento')],
            [sg.Text('Matrícula:', size=(15, 1), font=("Garamond", 18)), sg.InputText('', key='matricula')],
            [sg.Text('Salário:', size=(15, 1), font=("Garamond", 18)), sg.InputText('', key='salario')],
            [sg.Button('Confirmar', font=("Garamond", 15, 'bold')), sg.Cancel('Cancelar', font=("Garamond", 15, 'bold'))]
        ]
        self.__window = sg.Window('Sistema de Cadastro de Atendentes').Layout(layout)
     #   while True:
        button, values = self.open()
        #    try:
        nome = values['nome']
        cpf = values['cpf']
        idade = (values['idade'])
        rua = values['rua']
        numero = values['numero']
        complemento = (values['complemento'])
        matricula = values['matricula']
        salario = values['salario']
        self.close()
        return {"nome": nome, "cpf": cpf, "idade": idade, "rua": rua, "numero": numero, "complemento": complemento,
                "matricula": matricula, "salario": salario}
            #except ValueError as e: # no momento, só to fznd tratamento de "idade"
             #   self.mostra_mesagem(e)

    def pega_dados_para_alterar_atendente(self):
        sg.ChangeLookAndFeel('LightBrown2')
        layout = [
            [sg.Text('--------- DADOS PARA ALTERAR ATENDENTE ----------', font=("Garamond", 25, 'bold'))],
            [sg.Text('ATENÇÃO! Não é permitido alterar CPF e matrícula de atendente.')],
            [sg.Text('Nome:', size=(15, 1), font=("Garamond", 18)), sg.InputText('', key='nome')],
            [sg.Text('Idade:', size=(15, 1), font=("Garamond", 18)), sg.InputText('', key='idade')],
            [sg.Text('Rua:', size=(15, 1), font=("Garamond", 18)), sg.InputText('', key='rua')],
            [sg.Text('Número:',size=(15,1), font=("Garamond", 18)), sg.InputText('', key='numero')],
            [sg.Text('Complemento:',size=(15,1), font=("Garamond", 18)), sg.InputText('', key='complemento')],
            [sg.Text('Salário:', size=(15, 1), font=("Garamond", 18)), sg.InputText('', key='salario')],
            [sg.Button('Confirmar', font=("Garamond", 15, 'bold')), sg.Cancel('Cancelar', font=("Garamond", 15, 'bold'))]
        ]
        self.__window = sg.Window('Dados de Médico').Layout(layout)
        button, values = self.open()
        nome = (values['nome'])
        idade = (values(['idade']))
        rua = (values['rua'])
        numero = (values['numero'])
        complemento = (values['complemento'])
        salario = values['salario']
        self.close()
        return {"nome": nome, "idade": idade, "rua": rua, "numero": numero, "complemento": complemento, "salario": salario}

    def mostra_atendente(self, dados_atendente):
        string_todos_atendentes = ""
        for dado in dados_atendente:
            string_todos_atendentes = string_todos_atendentes + "NOME: "+ dado["nome"]+ '\n'
            string_todos_atendentes = string_todos_atendentes + "CPF: " + dado["cpf"] + '\n'
            string_todos_atendentes = string_todos_atendentes + "IDADE: " + dado["idade"] + '\n'
            string_todos_atendentes = string_todos_atendentes + "RUA: " + dado["rua"] + '\n'
            string_todos_atendentes = string_todos_atendentes + "NÚMERO: " + dado["numero"] + '\n'
            string_todos_atendentes = string_todos_atendentes + "COMPLEMENTO: " + dado["complemento"] + '\n'
            string_todos_atendentes = string_todos_atendentes + "MATRÍCULA: " + dado["matricula"] + '\n'
            string_todos_atendentes = string_todos_atendentes + "SALÁRIO: " + dado["salario"] + '\n\n'
        sg.Popup('----------- LISTA DE ATENDENTES -------------')

    def seleciona_atendente(self):
        sg.ChangeLookAndFeel('LightBrown2')
        layout = [
            [sg.Text('-------- SELECIONAR ATENDENTE ----------', font=("Garamond", 25))],
            [sg.Text("Digite a matrícula do atendente que deseja selecionar:", font=("Garamond", 15))],
            [sg.Text('MATRÍCULA:', size=(15, 1), font=("Garamond", 15)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona Atendente').Layout(layout)

        button, values = self.open()
        matricula = values["matricula"]
        self.close()
        return matricula

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values