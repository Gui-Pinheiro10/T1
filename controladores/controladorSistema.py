from telas.telaSistema import TelaSistema
from controladores.controladorCliente import ControladorCliente

class ControladorSistema:
    def __init__(self):
        self.__controlador_cliente = ControladorCliente(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_cliente(self):
        return self.__controlador_cliente

    def cadastro_cliente(self):
        self.__controlador_cliente.abre_tela() # chama o controlador de Clientes

    def inicializa_sistema(self):
        self.abre_tela()

    def encarra_sistema(self):
        print("Sistema encerrado!")
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastro_cliente, 0: self.encarra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
            
