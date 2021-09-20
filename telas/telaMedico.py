from telas.abstractTela import AbstractTela
import PySimpleGUI as sg


class TelaMedico(AbstractTela):
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
            [sg.Text('-------- CADASTRO DE MÉDICOS ----------', font=("Garamond", 25, 'bold'))],
            [sg.Text('Escolha sua opção:', font=("Garamond", 20, 'bold'))],
            [sg.Radio('Adicionar Médico', "RD1", key='1', font=("Garamond", 18))],
            [sg.Radio('Alterar Médico', "RD1", key='2', font=("Garamond", 18))],
            [sg.Radio('Excluir Médico', "RD1", key='3', font=("Garamond", 18))],
            [sg.Radio('Lista de Médicos', "RD1", key='4', font=("Garamond", 18))],
            [sg.Radio('Retornar', "RD1", key='0', font=("Garamond", 18))],
            [sg.Button('Confirmar', font=("Garamond", 15, 'bold')), sg.Cancel('Cancelar', font=("Garamond", 15, 'bold'))]
        ]
        self.__window = sg.Window('Sistema de Cadastro de Médicos').Layout(layout)

    def pega_dados_medico(self):
        sg.ChangeLookAndFeel('LightBrown2')
        layout = [
            [sg.Text('--------- DADOS MÉDICO ----------', font=("Garamond", 25, 'bold'))],
            [sg.Text('Nome:', size=(15, 1), font=("Garamond", 18)), sg.InputText('', key='nome')],
            [sg.Text('CPF:', size=(15, 1), font=("Garamond", 18)), sg.InputText('', key='cpf')],
            [sg.Text('Idade:', size=(15, 1), font=("Garamond", 18)), sg.InputText('', key='idade')],
            [sg.Text('Rua:', size=(15, 1), font=("Garamond", 18)), sg.InputText('', key='rua')],
            [sg.Text('Número:',size=(15,1), font=("Garamond", 18)), sg.InputText('', key='numero')],
            [sg.Text('Complemento:',size=(15,1), font=("Garamond", 18)), sg.InputText('', key='complemento')],
            [sg.Text('Matrícula:', size=(15,1), font=("Garamond",18)), sg.InputText('', key='matricula')],
            [sg.Text('Salário:', size=(15, 1), font=("Garamond", 18)), sg.InputText('', key='salario')],
            [sg.Text('CRM:', size=(15, 1), font=("Garamond", 18)), sg.InputText('', key='crm')],
            [sg.Button('Confirmar', font=("Garamond", 15, 'bold')), sg.Cancel('Cancelar', font=("Garamond", 15, 'bold'))]
        ]
        self.__window = sg.Window('Sistema de Cadastro de Médicos').Layout(layout)
     #   while True:
        button, values = self.open()
        try:
            nome = values['nome']
            cpf = values['cpf']
            idade = int(values['idade'])
            rua = values['rua']
            numero = int(values['numero'])
            complemento = (values['complemento'])
            matricula = int(values['matricula'])
            salario = int(values['salario'])
            crm = values['crm']
        except ValueError as e:
            self.mostra_mesagem('Valor deve ser inteiro')
        else:
            return {"nome": nome, "cpf": cpf, "idade": idade, "rua": rua, "numero": numero, "complemento": complemento,
                    "matricula": matricula, "salario": salario, "crm": crm}
        finally:
            self.close()

        # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
        # opção de tratamento: adicionar um if e só coletar nome e telefone se o button é 'Confirmar'

    def pega_dados_para_alterar_medico(self):
        sg.ChangeLookAndFeel('LightBrown2')
        layout = [
            [sg.Text('--------- DADOS PARA ALTERAR MÉDICO ----------', font=("Garamond", 25, 'bold'))],
            [sg.Text('Nome:', size=(15, 1), font=("Garamond", 18)), sg.InputText('', key='nome')],
            [sg.Text('Idade:', size=(15, 1), font=("Garamond", 18)), sg.InputText('', key='idade')],
            [sg.Text('Rua:', size=(15, 1), font=("Garamond", 18)), sg.InputText('', key='rua')],
            [sg.Text('Número:',size=(15,1), font=("Garamond", 18)), sg.InputText('', key='numero')],
            [sg.Text('Complemento:',size=(15,1), font=("Garamond", 18)), sg.InputText('', key='complemento')],
            [sg.Text('Salário:', size=(15,1), font=("Garamond", 18)), sg.InputText('', key='salario')],
            [sg.Button('Confirmar', font=("Garamond", 15, 'bold')), sg.Cancel('Cancelar', font=("Garamond", 15, 'bold'))]
        ]
        self.__window = sg.Window('Sistema de Cadastro de Médicos').Layout(layout)

        button, values = self.open()
        try:
            nome = (values['nome'])
            idade = int(values['idade'])
            rua = (values['rua'])
            numero = int(values['numero'])
            complemento = (values['complemento'])
            salario = int(values['salario'])
        except ValueError:
            self.mostra_mesagem('Idade, Número e Salário devem ser inteiros!')
        else:
            return {"nome": nome, "idade": idade, "rua": rua, "numero": numero, "complemento": complemento, "salario": salario}
        finally:
            self.close()

    def mostra_medico(self, dados_medico):
        string_todos_medicos = ""
        for dado in dados_medico:
            string_todos_medicos = string_todos_medicos + "NOME: " + dado["nome"] + '\n'
            string_todos_medicos = string_todos_medicos + "CPF: " + dado["cpf"] + '\n'
            string_todos_medicos = string_todos_medicos + "IDADE: " + str(dado["idade"]) + '\n'
            string_todos_medicos = string_todos_medicos + "ENDEREÇO: Rua " + dado["rua"] + " // Número: " + str(dado["numero"])\
            + " // Complemento: " + dado["complemento"] + '\n'
            string_todos_medicos = string_todos_medicos + "MATRÍCULA: " + str(dado["matricula"]) + '\n'
            string_todos_medicos = string_todos_medicos + "SALÁRIO: " + str(dado["salario"]) + '\n'
            string_todos_medicos = string_todos_medicos + "CRM: " + str(dado["crm"]) + '\n\n'

        sg.Popup('-------- LISTA DE MÉDICOS ----------', string_todos_medicos)

    def seleciona_medico(self):
        sg.ChangeLookAndFeel('LightBrown2')
        layout = [
            [sg.Text('-------- SELECIONAR MÉDICO ----------', font=("Garamond", 25))],
            [sg.Text("Digite o CPF do médico que deseja selecionar:", font=("Garamond", 15))],
            [sg.Text('CPF:', size=(15, 1), font=("Garamond", 15)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona Médico').Layout(layout)

        button, values = self.open()
        cpf = (values['cpf'])
        self.close()
        return cpf

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values