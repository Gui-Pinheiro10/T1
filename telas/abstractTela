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
