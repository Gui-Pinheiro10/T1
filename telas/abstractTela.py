from abc import ABC, abstractmethod


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
        print(msg)

    def le_valor_inteiro(self, mensagem: str=""):
        lido = False
        while not lido:
            try:
                numero = int(input(mensagem))
                lido = True
                return numero
            except ValueError:
                print("VALOR INVÁLIDO. Digite um valor numérico inteiro válido.")

    def verifica_cpf(self):
        cpf_valido = False
        while not cpf_valido:
            try:
                cpf = input('CPF: ')
                if len(cpf) != 11:
                    raise Exception
                if len(cpf) == 11 and cpf.isnumeric():
                    cpf_valido = True
                    return cpf
            except Exception:
                print('CPF informado incorretamente. Favor fornecer CPF válido!')

    def verifica_idade(self, mensagem: str=""):
        lido = False
        while not lido:
            try:
                idade = int(input(mensagem))
                if 0 <= idade <= 150:
                    lido = True
                    return idade
                else:
                    raise Exception
            except ValueError:
                print("VALOR INVÁLIDO! Digite um valor numérido inteiro válido.")
            except Exception:
                print("VALOR INVÁLIDO! Digite um valor numérido inteiro entre 0 e 150.")

    def le_str(self, mensagem: str=""):
        lido = False
        while not lido:
            try:
                entrada = str(input(mensagem))
                if len(entrada.strip()) == 0:
                    raise Exception
                else:
                    lido = True
            except Exception:
                print("ENTRADA VAZIA. Digite um valor válido.")
