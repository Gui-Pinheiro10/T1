from telas.abstractTela import AbstractTela

class TelaSistema(AbstractTela):

    def tela_opcoes(self):
        print("-------- SISTEMA CADASTRO CLIENTES ---------")
        print("Escolha sua opcao: ")
        print("1 - MENU CLIENTES")
        print("2 - MENU MÉDICOS")
        print("3 - MENU LIMPEZA")
        print("4 - MENU ENFERMEIROS")
        print("5 - MENU ATENDENTE")
        print("6 - MENU AGENDAMENTO")
        print("0 - Finalizar sistema")
        opcao = self.le_num_inteiro("Escolha a opcao: ", [1, 2, 3, 4, 5, 6, 0])
        return opcao
