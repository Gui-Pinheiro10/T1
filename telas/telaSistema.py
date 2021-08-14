from telas.abstractTela import AbstractTela

class TelaSistema(AbstractTela):

    def tela_opcoes(self):
        print("-------- SISTEMA CADASTRO CLIENTES ---------")
        print("Escolha sua opcao: ")
        print("1 - CLIENTES")
        print("0 - Finalizar sistema")
        opcao = self.le_num_inteiro("Escolha a opcao: ", [1, 0])
        return opcao
