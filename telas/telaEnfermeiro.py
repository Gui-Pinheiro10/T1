from telas.abstractTela import AbstractTela
import PySimpleGUI as sg


class TelaEnfermeiro(AbstractTela):
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
            [sg.Text('SISTEMA DE CONTROLE DO ENFERMEIRO', font=("Garamond", 25, 'bold'))],
            [sg.Text('Escolha sua opção', font=("Garamond", 20, 'bold'))],
            [sg.Radio('Adicionar Enfermeiro', "RD1", key='1', font=("Garamond", 20))],
            [sg.Radio('Alterar Enfermeiro', "RD1", key='2', font=("Garamond", 20))],
            [sg.Radio('Excluir Enfermeiro', "RD1", key='3', font=("Garamond", 20))],
            [sg.Radio('Listar Enfermeiros', "RD1", key='4', font=("Garamond", 20))],
            [sg.Radio('Retornar', "RD1", key='0', font=("Garamond", 20))],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de controle do Enfermeiro').Layout(layout)

    def pega_dados_enfermeiro(self):
        sg.ChangeLookAndFeel('LightBrown2')
        layout = [
            [sg.Text('---------- DADOS DO ENFERMEIRO ----------', font=("Garamond", 25, 'bold'))],
            [sg.Text('Nome:', size=(15, 1), font=("Garamond", 18)), sg.InputText('', key='nome')],
            [sg.Text('CPF:', size=(15, 1), font=("Garamond", 18)), sg.InputText('', key='cpf')],
            [sg.Text('Idade:', size=(15, 1), font=("Garamond", 18)), sg.InputText('', key='idade')],
            [sg.Text('Matrícula:', size=(15, 1), font=("Garamond", 18)), sg.InputText('', key='matricula')],
            [sg.Text('Salário:', size=(15, 1), font=("Garamond", 18)), sg.InputText('', key='salario')],
            [sg.Text('Digite os dados do endereço abaixo:', font=("Garamond", 20, 'bold'))],
            [sg.Text('Rua:', size=(15, 1), font=("Garamond", 18)), sg.InputText('', key='rua')],
            [sg.Text('Número:', size=(15, 1), font=("Garamond", 18)), sg.InputText('', key='numero')],
            [sg.Text('Complemento:', size=(15, 1), font=("Garamond", 18)), sg.InputText('', key='complemento')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Dados do Enfermeiro').Layout(layout)
        button, values = self.open()
        if button in (None, 'Cancelar'):
            return 'Cancelar'
        nome = self.le_nome(values['nome'])
        cpf = self.verifica_cpf(values['cpf'])
        idade = self.verifica_idade(values['idade'])
        matricula = self.verifica_matricula(values['matricula'])
        salario = self.verifica_salario(values['salario'])
        rua = self.le_rua(values['rua'])
        numero = self.verifica_numero_rua(values['numero'])
        complemento = self.le_complemento(values['complemento'])

        self.close()

        return {"nome": nome, "cpf": cpf, "idade": idade, "rua": rua, "numero": numero, "complemento": complemento,
                "matricula": matricula, "salario": salario}

    def pega_dados_para_alterar_enfermeiro(self):
        sg.ChangeLookAndFeel('LightBrown2')
        layout = [
            [sg.Text('---------- DADOS PARA ALTERAÇÃO DO ENFERMEIRO ----------', font=("Garamond", 25, 'bold'))],
            [sg.Text('Nome:', size=(15, 1), font=("Garamond", 18)), sg.InputText('', key='nome')],
            [sg.Text('Idade:', size=(15, 1), font=("Garamond", 18)), sg.InputText('', key='idade')],
            [sg.Text('Salário:', size=(15, 1), font=("Garamond", 18)), sg.InputText('', key='salario')],
            [sg.Text('Digite os dados do endereço abaixo:', font=("Garamond", 20, 'bold'))],
            [sg.Text('Rua:', size=(15, 1), font=("Garamond", 18)), sg.InputText('', key='rua')],
            [sg.Text('Número:', size=(15, 1), font=("Garamond", 18)), sg.InputText('', key='numero')],
            [sg.Text('Complemento:', size=(15, 1), font=("Garamond", 18)), sg.InputText('', key='complemento')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Dados do Enfermeiro').Layout(layout)
        button, values = self.open()
        nome = self.le_nome(values['nome'])
        idade = self.verifica_idade(values['idade'])
        salario = self.verifica_salario(values['salario'])
        rua = self.le_rua(values['rua'])
        numero = self.verifica_numero_rua(values['numero'])
        complemento = self.le_complemento(values['complemento'])

        self.close()

        return {"nome": nome, "idade": idade, "rua": rua, "numero": numero,
                "complemento": complemento, "salario": salario}

    def seleciona_enfermeiro(self):
        sg.ChangeLookAndFeel('LightBrown2')
        layout = [
            [sg.Text('-------- SELECIONAR ENFERMEIRO ----------', font=("Garamond", 25, 'bold'))],
            [sg.Text('Digite o CPF do enfermeiro que deseja selecionar:', font=("Garamond", 20))],
            [sg.Text('CPF:', size=(15, 1), font=("Garamond", 18)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona Enfermeiro').Layout(layout)

        button, values = self.open()
        if button in (None, 'Cancelar'):
            return 'Cancelar'
        cpf = values['cpf']
        self.close()
        return cpf

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def mostra_enfermeiro(self, dados_enfermeiro):
        string_todos_enfermeiros = ""
        for dado in dados_enfermeiro:
            string_todos_enfermeiros = string_todos_enfermeiros + "NOME DO ENFERMEIRO: " + dado["nome"] + '\n'
            string_todos_enfermeiros = string_todos_enfermeiros + "CPF DO ENFERMEIRO: " + dado["cpf"] + '\n'
            string_todos_enfermeiros = string_todos_enfermeiros + "IDADE DO ENFERMEIRO: " + str(dado["idade"]) + '\n'
            string_todos_enfermeiros = string_todos_enfermeiros + "ENDEREÇO DO ENFERMEIRO: Rua " + dado[
                                                                   "rua"] + " // Número: " + str(dado["numero"]) \
                                                                   + " // Complemento: " + dado["complemento"] + '\n\n'

        sg.Popup('-------- LISTA DE ENFERMEIROS ----------', string_todos_enfermeiros)