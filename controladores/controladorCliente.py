from entidade.cliente import Cliente
from telas.telaCliente import TelaCliente
from DAOs.cliente_dao import ClienteDAO


class ControladorCliente:

    def __init__(self, controlador_sistema):
        self.__cliente_DAO = ClienteDAO()
        self.__tela_cliente = TelaCliente()
        self.__controlador_sistema = controlador_sistema

    def pega_cliente_por_cpf(self, cpf: str):
        for cliente in self.__cliente_DAO.get_all():
            if cliente.cpf == cpf:
                return cliente
        return None

    def inclui_cliente(self):
        dados_cliente = self.__tela_cliente.pega_dados_cliente()
        if dados_cliente == 'Cancelar':
            self.__tela_cliente.close()
            self.__tela_cliente.open()
       # if dados_cliente is not None:
        else:
            try:
                if self.pega_cliente_por_cpf(dados_cliente["cpf"]) is not None:
                    raise Exception
            except Exception:
                self.__tela_cliente.mostra_mesagem("Não foi possível adicionar o cliente, pois este CPF já está cadastrado.")
            else:
                cliente = Cliente(dados_cliente["nome"], dados_cliente["cpf"], dados_cliente["idade"],
                                  dados_cliente["rua"],
                                  dados_cliente["numero"], dados_cliente["complemento"])
                self.__cliente_DAO.add(cliente)
                self.__tela_cliente.mostra_mesagem("Cliente adicionado com sucesso!")


    def altera_cliente(self):
        self.lista_clientes()
        cpf_pessoa = self.__tela_cliente.seleciona_cliente()
        if cpf_pessoa == 'Cancelar':
            self.__tela_cliente.close()
            self.__tela_cliente.open()
        else:
            pessoa = self.pega_cliente_por_cpf(cpf_pessoa)
            try:
                if pessoa is None:
                    raise Exception
            except Exception:
                self.__tela_cliente.mostra_mesagem("Não foi possível alterar este cadastro, pois este CPF não está cadastrado.")
            else:
                novos_dados_pessoa = self.__tela_cliente.pega_dados_para_alterar_cliente()
              #  if novos_dados_pessoa is not None:
                pessoa.nome = novos_dados_pessoa["nome"]
                pessoa.idade = novos_dados_pessoa["idade"]
                pessoa.endereco.rua = novos_dados_pessoa["rua"]
                pessoa.endereco.numero = novos_dados_pessoa["numero"]
                pessoa.endereco.complemento = novos_dados_pessoa["complemento"]
                self.__tela_cliente.mostra_mesagem("Cliente alterado com sucesso!")
                self.lista_clientes()

    def exclui_cliente(self):
        self.lista_clientes()
        codigo_cliente = self.__tela_cliente.seleciona_cliente()
        if codigo_cliente == 'Cancelar':
            self.__tela_cliente.close()
            self.__tela_cliente.open()
        else:
            cliente_excluido = self.pega_cliente_por_cpf(codigo_cliente)
            try:
                if cliente_excluido is None:
                    raise Exception
            except Exception:
                self.__tela_cliente.mostra_mesagem("Não foi possível excluir este cadastro, pois este CPF não está cadastrado.")
            else:
                self.__cliente_DAO.remove(cliente_excluido.cpf)
                self.__tela_cliente.mostra_mesagem('Cliente excluído com sucesso!')
                self.lista_clientes()

    def lista_clientes(self):
        dados_clientes = []
       # self.__tela_cliente.mostra_mesagem("LISTA DE CLIENTES".center(30, '-'))
        try:
            if len(self.__cliente_DAO.get_all()) == 0:
                raise Exception
        except Exception:
            self.__tela_cliente.mostra_mesagem('No momento, a lista de clientes está vazia.')
        else:
            for cliente in self.__cliente_DAO.get_all():
                dados_clientes.append({"nome": cliente.nome, "cpf": cliente.cpf, "idade": cliente.idade,
                                       "rua": cliente.endereco.rua, "numero": cliente.endereco.numero,
                                       "complemento": cliente.endereco.complemento})
            self.__tela_cliente.mostra_cliente(dados_clientes)


    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.inclui_cliente, 2: self.altera_cliente, 3: self.exclui_cliente, 4: self.lista_clientes,
                        0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_cliente.tela_opcoes()]()

    def retorna_lista_clientes(self):
        return self.__cliente_DAO.get_all()
