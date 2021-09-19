from abc import ABC, abstractmethod
import PySimpleGUI as sg


class AbstractTela(ABC):
    @abstractmethod
    def tela_opcoes(self):
        pass

    def le_num_inteiro(self, mensagem: str="", inteiros_validos: []=None):
        while True:
            valor_entrada = input(mensagem)
            try:
                inteiro = int(valor_entrada)
                if inteiros_validos and inteiro not in inteiros_validos:
                    raise ValueError
                return inteiro
            except ValueError:
                print("VALOR INVÁLIDO. Digite um valor numérico inteiro válido.")
                if inteiros_validos:
                    print("Os valores válidos são: ",inteiros_validos)

    def mostra_mesagem(self, msg):
        sg.popup("", msg)

    def le_valor_inteiro(self, valor: int):
        lido = False
        while not lido:
            try:
                if not valor.isnumeric():
                    raise ValueError
            except ValueError:
                sg.PopupOK("VALOR INVÁLIDO. Digite um valor numérico inteiro válido.")
                valor = sg.popup_get_text('Digite um valor inteiro válido: ')
            else:
                lido = True
        return int(valor)

    def verifica_matricula(self, matricula: int):
        lido = False
        while not lido:
            try:
                if not matricula.isnumeric():
                    raise ValueError
            except ValueError:
                sg.PopupOK("MATRÍCULA INVÁLIDA.")
                matricula = sg.popup_get_text('Digite uma matrícula válida: ')
            else:
                lido = True
        return int(matricula)

    def verifica_salario(self, salario: int):
        lido = False
        while not lido:
            try:
                if not salario.isnumeric():
                    raise ValueError
            except ValueError:
                sg.PopupOK("SALÁRIO INVÁLIDO.")
                salario = sg.popup_get_text('Digite um salário válido: ')
            else:
                lido = True
        return int(salario)

    def verifica_numero_rua(self, numero_rua: int):
        lido = False
        while not lido:
            try:
                if not numero_rua.isnumeric():
                    raise ValueError
            except ValueError:
                sg.PopupOK("NÚMERO DO ENDEREÇO INVÁLIDO.")
                numero_rua = sg.popup_get_text('Digite um número do endereço válido: ')
            else:
                lido = True
        return int(numero_rua)

    def verifica_cpf(self, cpf: int):
        cpf_valido = False
        while not cpf_valido:
            try:
                if len(cpf) != 11:
                    raise Exception
                if not cpf.isnumeric():
                    raise Exception
            except Exception:
                sg.PopupOK('CPF informado incorretamente. Favor fornecer CPF válido!')
                cpf = sg.popup_get_text("Digite o CPF novamente: ")
            else:
                cpf_valido = True
        return cpf

    def verifica_idade(self, idade: int):
        idade_valida = False
        while not idade_valida:
            try:
                if not idade.isnumeric():
                    raise Exception
                if int(idade) < 0 or int(idade) > 150:
                    raise Exception
            except Exception:
                sg.PopupOK("VALOR INVÁLIDO! Digite um valor numérico inteiro entre 0 e 150.")
                idade = sg.popup_get_text('Digite a idade novamente: ')
            else:
                idade_valida = True
        return int(idade)

    def le_nome(self, nome: str):
        lido = False
        while not lido:
            try:
                if len(nome.strip()) == 0:
                    raise Exception
            except Exception:
                sg.PopupOK("ENTRADA VAZIA PARA NOME.")
                nome = sg.popup_get_text('Digite um nome válido: ')
            else:
                lido = True
        return nome

    def le_rua(self, rua: str):
        lido = False
        while not lido:
            try:
                if len(rua.strip()) == 0:
                    raise Exception
            except Exception:
                sg.PopupOK("ENTRADA VAZIA PARA RUA.")
                rua = sg.popup_get_text('Digite uma rua válida: ')
            else:
                lido = True
        return rua

    def le_complemento(self, complemento: str):
        lido = False
        while not lido:
            try:
                if len(complemento.strip()) == 0:
                    raise Exception
            except Exception:
                sg.PopupOK("ENTRADA VAZIA PARA COMPLEMENTO.")
                complemento = sg.popup_get_text('Digite um complemento de endereço válido: ')
            else:
                lido = True
        return complemento
