from telas.abstractTela import AbstractTela
import PySimpleGUI as sg


class TelaLimpeza(AbstractTela):
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

    def close(self):
        self.__window.Close()

    def init_components(self):
        # sg.theme_previewer()
        sg.ChangeLookAndFeel('LightBrown2')
        layout = [
            [sg.Text('SISTEMA DE CONTROLE DO FUNCIONÁRIO DA LIMPEZA', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Adicionar Funcionário da Limpeza', "RD1", key='1')],
            [sg.Radio('Alterar Funcionário da Limpeza', "RD1", key='2')],
            [sg.Radio('Excluir Funcionário da Limpeza', "RD1", key='3')],
            [sg.Radio('Listar Funcionário da Limpeza', "RD1", key='4')],
            [sg.Radio('Finalizar sistema', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de controle do Funcionário da Limpeza').Layout(layout)

    def pega_dados_limpeza(self):
        sg.ChangeLookAndFeel('LightBrown2')
        layout = [
            [sg.Text('---------- DADOS DO FUNCIONÁRIO DA LIMPEZA ----------', font=("Helvica", 15))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Text('Idade:', size=(15, 1)), sg.InputText('', key='idade')],
            [sg.Text('Matrícula:', size=(15, 1)), sg.InputText('', key='matricula')],
            [sg.Text('Salário:', size=(15, 1)), sg.InputText('', key='salario')],
            [sg.Text('Digite os dados do endereço abaixo:', font=("Helvica", 25))],
            [sg.Text('Rua:', size=(15, 1)), sg.InputText('', key='rua')],
            [sg.Text('Número:', size=(15, 1)), sg.InputText('', key='numero')],
            [sg.Text('Complemento:', size=(15, 1)), sg.InputText('', key='complemento')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Dados do Enfermeiro').Layout(layout)
        button, values = self.open()
        nome = values['nome']
        cpf = values['cpf']
        idade = values['idade']
        matricula = values['matricula']
        salario = values['salario']
        rua = values['rua']
        numero = values['numero']
        complemento = values['complemento']

        self.close()

        return {"nome": nome, "cpf": cpf, "idade": idade, "rua": rua, "numero": numero, "complemento": complemento,
                "matricula": matricula, "salario": salario}

    def pega_dados_para_alterar_limpeza(self):
        sg.ChangeLookAndFeel('LightBrown2')
        layout = [
            [sg.Text('---------- DADOS PARA ALTERAÇÃO DO FUNCIONÁRIO DA LIMPEZA ----------', font=("Helvica", 15))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Idade:', size=(15, 1)), sg.InputText('', key='idade')],
            [sg.Text('Salário:', size=(15, 1)), sg.InputText('', key='salario')],
            [sg.Text('Digite os dados do endereço abaixo:', font=("Helvica", 25))],
            [sg.Text('Rua:', size=(15, 1)), sg.InputText('', key='rua')],
            [sg.Text('Número:', size=(15, 1)), sg.InputText('', key='numero')],
            [sg.Text('Complemento:', size=(15, 1)), sg.InputText('', key='complemento')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Dados do Funcionário da Limpeza').Layout(layout)
        button, values = self.open()
        nome = values['nome']
        idade = values['idade']
        salario = values['salario']
        rua = values['rua']
        numero = values['numero']
        complemento = values['complemento']

        self.close()

        return {"nome": nome, "idade": idade, "rua": rua, "numero": numero,
                "complemento": complemento, "salario": salario}

    def seleciona_limpeza(self):
        sg.ChangeLookAndFeel('LightBrown2')
        layout = [
            [sg.Text('-------- SELECIONAR FUNCIONÁRIO DA LIMPEZA ----------', font=("Helvica", 25))],
            [sg.Text('Digite o CPF do funcionário da limpeza que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona Funcionário da Limpeza').Layout(layout)

        button, values = self.open()
        cpf = values['cpf']
        self.close()
        return cpf

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def mostra_limpeza(self, dados_limpeza):
        string_todos_limpeza = ""
        for dado in dados_limpeza:
            string_todos_limpeza = string_todos_limpeza + "NOME DO FUNCIONÁRIO DA LIMPEZA: " + dado["nome"] + '\n'
            string_todos_limpeza = string_todos_limpeza + "FONE DO FUNCIONÁRIO DA LIMPEZA: " + str(dado["telefone"]) + '\n'
            string_todos_limpeza = string_todos_limpeza + "CPF DO FUNCIONÁRIO DA LIMPEZA: " + str(dado["cpf"]) + '\n\n'

        sg.Popup('-------- LISTA DE FUNCIONÁRIOS DA LIMPEZA ----------', string_todos_limpeza)