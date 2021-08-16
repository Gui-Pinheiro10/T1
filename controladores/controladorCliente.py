from entidade.cliente import Cliente
from telas.telaCliente import TelaCliente

class ControladorCliente:
    def __init__(self, controlador_sistema):
        self.__tela_cliente = TelaCliente()
        self.__clientes = []
        self.__controlador_sistema = controlador_sistema

    def pega_cliente_por_codigo(self, codigo: int):
        for cliente in self.__clientes:
            if (cliente.codigo == codigo):
                return cliente
        return None

    def inclui_cliente(self):
        dados_cliente = self.__tela_cliente.pega_dados_cliente()
        cliente = Cliente(dados_cliente["nome"], dados_cliente["cpf"], dados_cliente["idade"], dados_cliente["rua"],
                          dados_cliente["numero"], dados_cliente["complemento"], dados_cliente["codigo"])
        try:
            if self.pega_cliente_por_codigo(dados_cliente["codigo"]) is not None:
                raise Exception
        except Exception:
            self.__tela_cliente.mostra_mesagem("Não foi possível adicionar o cliente, pois este código já está cadastrado.")
        else:
            self.__clientes.append(cliente)
            self.__tela_cliente.mostra_mesagem("Cliente adicionado com sucesso!")

    def altera_cliente(self):
        self.lista_clientes()
        codigo_pessoa = self.__tela_cliente.seleciona_cliente()
        pessoa = self.pega_cliente_por_codigo(codigo_pessoa)
        if (pessoa is not None):
            novos_dados_pessoa = self.__tela_cliente.pega_dados_para_alterar_cliente()
            pessoa.nome = novos_dados_pessoa["nome"]
            pessoa.idade = novos_dados_pessoa["idade"]
            pessoa.endereco.rua = novos_dados_pessoa["rua"]
            pessoa.endereco.numero = novos_dados_pessoa["numero"]
            pessoa.endereco.complemento = novos_dados_pessoa["complemento"]
            self.__tela_cliente.mostra_mesagem("Cliente alterado com sucesso!")
            self.lista_clientes()
        else:
            self.__tela_cliente.mostra_mesagem("Não foi possível alterar este cadastro, pois ele não existe.")


    def exclui_cliente(self):
        self.lista_clientes()
        codigo_cliente = self.__tela_cliente.seleciona_cliente()
        cliente = self.pega_cliente_por_codigo(codigo_cliente)
        if (cliente is not None):
            self.__clientes.remove(cliente)
            self.__tela_cliente.mostra_mesagem('Cliente excluído com sucesso!')
            self.lista_clientes()
        else:
            self.__tela_cliente.mostra_mesagem("Não foi possível excluir este cadastro, pois ele não existe.")

    def lista_clientes(self):
        self.__tela_cliente.mostra_mesagem("LISTA DE CLIENTES".center(30, '-'))
        for cliente in self.__clientes:
            self.__tela_cliente.mostra_cliente({"nome": cliente.nome, "cpf": cliente.cpf, "idade": cliente.idade, "rua": cliente.endereco.rua, "numero": cliente.endereco.numero, "complemento": cliente.endereco.complemento,
                                                "codigo": cliente.codigo})
        if len(self.__clientes) == 0:
            self.__tela_cliente.mostra_mesagem("No momento, a lista de clientes está vazia.")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.inclui_cliente, 2: self.altera_cliente, 3: self.exclui_cliente, 4: self.lista_clientes,
                        0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_cliente.tela_opcoes()]()

    def retorna_lista_clientes(self):
        return self.__clientes
