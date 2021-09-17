from telas.abstractTela import AbstractTela
import PySimpleGUI as sg


class TelaCliente(AbstractTela):
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
            [sg.Text('-------- CADASTRO DE CLIENTES ----------', font=("Garamond", 25, 'bold'))],
            [sg.Text('Escolha sua opção:', font=("Garamond", 20, 'bold'))],
            [sg.Radio('Adicionar Cliente', "RD1", key='1', font=("Garamond", 18))],
            [sg.Radio('Alterar Cliente', "RD1", key='2', font=("Garamond", 18))],
            [sg.Radio('Excluir Cliente', "RD1", key='3', font=("Garamond", 18))],
            [sg.Radio('Lista de Clientes', "RD1", key='4', font=("Garamond", 18))],
            [sg.Radio('Retornar', "RD1", key='0', font=("Garamond", 18))],
            [sg.Button('Confirmar', font=("Garamond", 15, 'bold')), sg.Cancel('Cancelar', font=("Garamond", 15, 'bold'))]
        ]
        self.__window = sg.Window('Sistema de Cadastro de Clientes').Layout(layout)

    def pega_dados_cliente(self):
        sg.ChangeLookAndFeel('LightBrown2')
        layout = [
            [sg.Text('--------- DADOS CLIENTE ----------', font=("Garamond", 25, 'bold'))],
            [sg.Text('Nome:', size=(15, 1), font=("Garamond", 18)), sg.InputText('', key='nome')],
            [sg.Text('CPF:', size=(15, 1), font=("Garamond", 18)), sg.InputText('', key='cpf')],
            [sg.Text('Idade:', size=(15, 1), font=("Garamond", 18)), sg.InputText('', key='idade')],
            [sg.Text('Rua:', size=(15, 1), font=("Garamond", 18)), sg.InputText('', key='rua')],
            [sg.Text('Número:',size=(15,1), font=("Garamond", 18)), sg.InputText('', key='numero')],
            [sg.Text('Complemento:',size=(15,1), font=("Garamond", 18)), sg.InputText('', key='complemento')],
            [sg.Button('Confirmar', font=("Garamond", 15, 'bold')), sg.Cancel('Cancelar', font=("Garamond", 15, 'bold'))]
        ]
        self.__window = sg.Window('Sistema de Cadastro de Clientes').Layout(layout)
     #   while True:
        button, values = self.open()
        try:
            nome = values['nome']
            cpf = values['cpf']
            idade = int(values['idade'])
            rua = values['rua']
            numero = int(values['numero'])
            complemento = (values['complemento'])
        except ValueError as e: # no momento, só to fznd tratamento de "idade"
            self.mostra_mesagem('Valor deve ser inteiro')
        else:
            return {"nome": nome, "cpf": cpf, "idade": idade, "rua": rua, "numero": numero, "complemento": complemento}
        finally:
            self.close()

        # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
        # opção de tratamento: adicionar um if e só coletar nome e telefone se o button é 'Confirmar'

    def pega_dados_para_alterar_cliente(self):
        sg.ChangeLookAndFeel('LightBrown2')
        layout = [
            [sg.Text('--------- DADOS PARA ALTERAR CLIENTE ----------', font=("Garamond", 25, 'bold'))],
            [sg.Text('Nome:', size=(15, 1), font=("Garamond", 18)), sg.InputText('', key='nome')],
            [sg.Text('Idade:', size=(15, 1), font=("Garamond", 18)), sg.InputText('', key='idade')],
            [sg.Text('Rua:', size=(15, 1), font=("Garamond", 18)), sg.InputText('', key='rua')],
            [sg.Text('Número:',size=(15,1), font=("Garamond", 18)), sg.InputText('', key='numero')],
            [sg.Text('Complemento:',size=(15,1), font=("Garamond", 18)), sg.InputText('', key='complemento')],
            [sg.Button('Confirmar', font=("Garamond", 15, 'bold')), sg.Cancel('Cancelar', font=("Garamond", 15, 'bold'))]
        ]
        self.__window = sg.Window('Sistema de Cadastro de Clientes').Layout(layout)

        button, values = self.open()
        nome = (values['nome'])
        idade = (values(['idade']))
        rua = (values['rua'])
        numero = (values['numero'])
        complemento = (values['complemento'])
        self.close()
        return {"nome": nome, "idade": idade, "rua": rua, "numero": numero, "complemento": complemento}


    # nao entendi pq esse método não funciona
    def mostra_cliente(self, dados_cliente):
        string_todos_clientes = ""
        for dado in dados_cliente:
            string_todos_clientes = string_todos_clientes + "NOME DO CLIENTE: " + dado["nome"] + '\n'
            string_todos_clientes = string_todos_clientes + "CPF DO CLIENTE: " + dado["cpf"] + '\n'
            string_todos_clientes = string_todos_clientes + "IDADE DO CLIENTE: " + str(dado["idade"]) + '\n'
            string_todos_clientes = string_todos_clientes + "ENDEREÇO DO CLIENTE: Rua " + dado["rua"] + " // Número: " + str(dado["numero"])\
            + " // Complemento: " + dado["complemento"] + '\n\n'


        sg.Popup('-------- LISTA DE CLIENTES ----------', string_todos_clientes)

    def seleciona_cliente(self): # criar um listbox com os cpfs existentes?
        sg.ChangeLookAndFeel('LightBrown2')
        layout = [
            [sg.Text('-------- SELECIONAR CLIENTE ----------', font=("Garamond", 25))],
            [sg.Text("Digite o CPF do cliente que deseja selecionar:", font=("Garamond", 15))],
            [sg.Text('CPF:', size=(15, 1), font=("Garamond", 15)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona Cliente').Layout(layout)

        button, values = self.open()
        cpf = (values['cpf'])
        self.close()
        return cpf

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values