from controladores.controladorLimpeza import ControladorLimpeza


class TelaLimpeza(self):
    def __init__(self, controlador: ControladorLimpeza):
        self.__controlador = controlador

    def le_num_inteiro(self, mensagem: str = "", inteiros_validos: list = None):
        while True:
            valor_lido = input(mensagem)
            try:
                inteiro = int(valor_lido)
                if inteiros_validos and inteiro not in inteiros_validos:
                    raise ValueError
                return inteiro
            except ValueError:
                print('Valor incorreto. Digite um valor inteiro válido.')
                if inteiros_validos:
                    print('Valores válidos: ', inteiros_validos)
    
    def mostra_tela_opcoes(self):
        print("---------- OPÇÕES DE FUNCIONÁRIOS DA LIMPEZA ----------")
        print('1 - Incluir')
        print('2 - Alterar')
        print('3 - Excluir')
        print('4 - Listar')
        print('0 - Voltar')
        opcao = self.le_num_inteiro('Escolha a opção: ', [0, 1, 2, 3, 4])
        return opcao
