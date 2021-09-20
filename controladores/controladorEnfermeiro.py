from entidade.enfermeiro import Enfermeiro
from telas.telaEnfermeiro import TelaEnfermeiro
from DAOs.enfermeiro_dao import EnfermeiroDAO


class ControladorEnfermeiro():
    def __init__(self, controlador_sistema):
        self.__enfermeiros_DAO = EnfermeiroDAO()
        self.__tela_enfermeiro = TelaEnfermeiro()
        self.__controlador_sistema = controlador_sistema

    def pega_enfermeiro_por_cpf(self, cpf: int):
        for enfermeiro in self.__enfermeiros_DAO.get_all():
            if enfermeiro.cpf == cpf:
                return enfermeiro
        return None

    def inclui_enfermeiro(self):
        dados_enfermeiro = self.__tela_enfermeiro.pega_dados_enfermeiro()
        if dados_enfermeiro == 'Cancelar':
            self.__tela_enfermeiro.close()
            self.__tela_enfermeiro.open()
        else:
            try:
                if self.pega_enfermeiro_por_cpf(dados_enfermeiro["cpf"]) is not None:
                    raise Exception
            except Exception:
                self.__tela_enfermeiro.mostra_mesagem('Não foi possível cadastrar o enfermeiro pois o CPF já está cadastrado!')
            else:
                enfermeiro = Enfermeiro(dados_enfermeiro["nome"], dados_enfermeiro["cpf"], dados_enfermeiro["idade"],
                                        dados_enfermeiro["rua"], dados_enfermeiro["numero"],
                                        dados_enfermeiro["complemento"], dados_enfermeiro["matricula"],
                                        dados_enfermeiro["salario"])
                self.__enfermeiros_DAO.add(enfermeiro)
                self.__tela_enfermeiro.mostra_mesagem('Enfermeiro adicionado com sucesso!')

    def exclui_enfermeiro(self):
        self.listar_enfermeiros()
        cpf_enfermeiro_excluido = self.__tela_enfermeiro.seleciona_enfermeiro()
        if cpf_enfermeiro_excluido == 'Cancelar':
            self.__tela_enfermeiro.close()
            self.__tela_enfermeiro.open()
        else:
            enfermeiro_excluido = self.pega_enfermeiro_por_cpf(cpf_enfermeiro_excluido)
            try:
                if enfermeiro_excluido is None:
                    raise Exception
            except Exception:
                self.__tela_enfermeiro.mostra_mesagem('Não foi possível excluir o enfermeiro, pois o CPF informado não está na lista!')
            else:
                self.__enfermeiros_DAO.remove(enfermeiro_excluido.cpf)
                self.__tela_enfermeiro.mostra_mesagem('Enfermeiro excluído com sucesso!')
                self.listar_enfermeiros()

    def altera_enfermeiro(self):
        self.listar_enfermeiros()
        cpf_enfermeiro_alterado = self.__tela_enfermeiro.seleciona_enfermeiro()
        if cpf_enfermeiro_alterado == 'Cancelar':
            self.__tela_enfermeiro.close()
            self.__tela_enfermeiro.open()
        else:
            enfermeiro_alterado = self.pega_enfermeiro_por_cpf(cpf_enfermeiro_alterado)
            try:
                if enfermeiro_alterado is None:
                    raise Exception
            except Exception:
                self.__tela_enfermeiro.mostra_mesagem('Não foi possível alterar o enfermeiro, pois a matrícula informada não está na lista!')
            else:
                novos_dados_enfermeiro = self.__tela_enfermeiro.pega_dados_para_alterar_enfermeiro()
                enfermeiro_alterado.nome = novos_dados_enfermeiro["nome"]
                enfermeiro_alterado.idade = novos_dados_enfermeiro["idade"]
                enfermeiro_alterado.endereco.rua = novos_dados_enfermeiro["rua"]
                enfermeiro_alterado.endereco.numero = novos_dados_enfermeiro["numero"]
                enfermeiro_alterado.endereco.complemento = novos_dados_enfermeiro["complemento"]
                enfermeiro_alterado.salario = novos_dados_enfermeiro["salario"]
                self.__tela_enfermeiro.mostra_mesagem('Enfermeiro alterado com sucesso!\n')
                self.listar_enfermeiros()

    def listar_enfermeiros(self):
        dados_enfermeiros = []
        try:
            if len(self.__enfermeiros_DAO.get_all()) == 0:
                raise Exception
        except Exception:
            self.__tela_enfermeiro.mostra_mesagem("No momento a lista de enfermeiros está vazia.")
        else:
            for enfermeiro in self.__enfermeiros_DAO.get_all():
                dados_enfermeiros.append({"nome": enfermeiro.nome, "idade": enfermeiro.idade,
                                          "cpf": enfermeiro.cpf, "salario": enfermeiro.salario,
                                          "matricula": enfermeiro.matricula, "rua": enfermeiro.endereco.rua,
                                          "numero": enfermeiro.endereco.numero, "complemento": enfermeiro.endereco.complemento})
            self.__tela_enfermeiro.mostra_enfermeiro(dados_enfermeiros)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela_enfermeiro(self):
        opcoes = {0: self.retornar, 1: self.inclui_enfermeiro, 2: self.altera_enfermeiro, 3: self.exclui_enfermeiro, 4: self.listar_enfermeiros}
        while True:
            opcao = self.__tela_enfermeiro.tela_opcoes()
            funcao_escolhida = opcoes[opcao]
            funcao_escolhida()

    def retorna_lista_enfermeiros(self):
        return self.__enfermeiros_DAO.get_all()
