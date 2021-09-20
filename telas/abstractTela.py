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
                sg.PopupOK("MATRÍCULA INVÁLIDA.", title='ERRO NA MATRÍCULA')
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
                sg.PopupOK("SALÁRIO INVÁLIDO.", title='ERRO NO SALÁRIO')
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
                sg.PopupOK("NÚMERO DO ENDEREÇO INVÁLIDO.", title='ERRO NO ENDEREÇO')
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
                sg.PopupOK('CPF informado incorretamente. Favor fornecer CPF válido!', title='ERRO NO CPF')
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
                sg.PopupOK("VALOR INVÁLIDO! Digite um valor numérico inteiro entre 0 e 150.", title='ERRO NA IDADE')
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
                sg.PopupOK("ENTRADA VAZIA PARA NOME.", title='ERRO NO NOME')
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
                sg.PopupOK("ENTRADA VAZIA PARA RUA.", title='ERRO NA RUA')
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
                sg.PopupOK("ENTRADA VAZIA PARA COMPLEMENTO.", title='ERRO NA COMPLEMENTO')
                complemento = sg.popup_get_text('Digite um complemento de endereço válido: ')
            else:
                lido = True
        return complemento

    def le_horario(self, horario: str):
        lido = False
        while not lido:
            try:
                if len(horario) != 5:
                    raise Exception
                if not horario[0].isnumeric() or not horario[1].isnumeric() or not horario[3].isnumeric() or not horario[4].isnumeric():
                    raise Exception
                if horario[2] != ":":
                    raise Exception
            except Exception:
                sg.PopupOK("ENTRADA INVÁLIDA PARA HORÁRIO.", title='ERRO NO HORÁRIO')
                horario = sg.popup_get_text('Digite um horário no formato XX:XX: ')
            else:
                lido = True
        return horario

    def le_data(self, data: str):
        lido = False
        while not lido:
            try:
                if len(data) != 8:
                    raise Exception
                if not data[0].isnumeric() or not data[1].isnumeric() or not data[3].isnumeric() or not data[4].isnumeric or not data[6].isnumeric() or not data[7].isnumeric():
                    raise Exception
                if (data[2] != "/") or (data[5] != "/"):
                    raise Exception
            except Exception:
                sg.PopupOK("ENTRADA INVÁLIDA PARA DATA.", title='ERRO NA DATA')
                data = sg.popup_get_text('Digite uma data no formato DD/MM/AA: ')
            else:
                lido = True
        return data

    def le_especialidade_ou_tipo_de_vacina(self, especialidade_ou_tipo_de_vacina: str):
        lido = False
        while not lido:
            try:
                if len(especialidade_ou_tipo_de_vacina.strip()) == 0:
                    raise Exception
            except Exception:
                sg.PopupOK("ENTRADA VAZIA PARA ESPECIALIDADE DE CONSULTA OU TIPO DE VACINA.", title='ERRO NO TIPO DE AGENDAMENTO')
                especialidade_ou_tipo_de_vacina = sg.popup_get_text('Digite uma especialidade ou tipo de vacina: ')
            else:
                lido = True
        return especialidade_ou_tipo_de_vacina

    def verifica_codigo(self, codigo: int):
        codigo_valido = False
        while not codigo_valido:
            try:
                if not codigo.isnumeric():
                    raise Exception
            except Exception:
                sg.PopupOK("CÓDIGO DE AGENDAMENTO INVÁLIDO!.", title='ERRO NO CÓDIGO DO AGENDAMENTO')
                codigo = sg.popup_get_text('Digite o código do agendamento novamente: ')
            else:
                codigo_valido = True
        return int(codigo)
