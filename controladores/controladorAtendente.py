from entidade.atendente import Atendente
from telas.telaAtendente import TelaAtendente
from DAOs.atendente_dao import AtendenteDAO


class ControladorAtendente:

    def __init__(self, controlador_sistema):
        self.__atendente_DAO = AtendenteDAO()
        self.__tela_atendente = TelaAtendente()
        self.__controlador_sistema = controlador_sistema

    def pega_atendente_por_cpf(self, cpf: str):
        for atendente in self.__atendente_DAO.get_all():
            if atendente.cpf == cpf:
                return atendente
        return None

    def inclui_atendente(self):
        dados_atendente = self.__tela_atendente.pega_dados_atendente()
        if dados_atendente == 'Cancelar':
            self.__tela_atendente.close()
            self.__tela_atendente.open()
        else:
       # if dados_atendente is not None:
            try:
                if self.pega_atendente_por_cpf(dados_atendente["cpf"]) is not None:
                    raise Exception
            except Exception:
                self.__tela_atendente.mostra_mesagem("Não foi possível adicionar o atendente, pois este CPF já está cadastrado.")
            else:
                atendente = Atendente(dados_atendente["nome"], dados_atendente["cpf"], dados_atendente["idade"],
                                      dados_atendente["rua"], dados_atendente["numero"],
                                      dados_atendente["complemento"], dados_atendente["matricula"],
                                      dados_atendente["salario"])
                self.__atendente_DAO.add(atendente)
                self.__tela_atendente.mostra_mesagem("Atendente adicionado com sucesso!")


    def altera_atendente(self):
        self.lista_atendentes()
        cpf_pessoa = self.__tela_atendente.seleciona_atendente()
        if cpf_pessoa == 'Cancelar':
            self.__tela_atendente.close()
            self.__tela_atendente.open()
        else:
            atendente_alterado = self.pega_atendente_por_cpf(cpf_pessoa)
            try:
                if atendente_alterado is None:
                    raise Exception
            except Exception:
                self.__tela_atendente.mostra_mesagem("Não foi possível alterar este cadastro, pois este CPF não está cadastrado.")
            else:
                novos_dados_pessoa = self.__tela_atendente.pega_dados_para_alterar_atendente()
                if novos_dados_pessoa is not None:
                    atendente_alterado.nome = novos_dados_pessoa["nome"]
                    atendente_alterado.idade = novos_dados_pessoa["idade"]
                    atendente_alterado.endereco.rua = novos_dados_pessoa["rua"]
                    atendente_alterado.endereco.numero = novos_dados_pessoa["numero"]
                    atendente_alterado.endereco.complemento = novos_dados_pessoa["complemento"]
                    atendente_alterado.salario = novos_dados_pessoa["salario"]
                    self.__tela_atendente.mostra_mesagem("Atendente alterado com sucesso!")
                    self.lista_atendentes()

    def exclui_atendente(self):
        self.lista_atendentes()
        codigo_atendente = self.__tela_atendente.seleciona_atendente()
        if codigo_atendente == 'Cancelar':
            self.__tela_atendente.close()
            self.__tela_atendente.open()
        else:
            atendente_excluido = self.pega_atendente_por_cpf(codigo_atendente)
            try:
                if atendente_excluido is None:
                    raise Exception
            except Exception:
                self.__tela_atendente.mostra_mesagem("Não foi possível excluir este cadastro, pois este CPF não está cadastrado.")
            else:
                self.__atendente_DAO.remove(atendente_excluido.cpf)
                self.__tela_atendente.mostra_mesagem('Atendente excluído com sucesso!')
                self.lista_atendentes()

    def lista_atendentes(self):
        dados_atendentes = []
        try:
            if len(self.__atendente_DAO.get_all()) == 0:
                raise Exception
        except Exception:
            self.__tela_atendente.mostra_mesagem('No momento, a lista de atendentes está vazia.')
        else:
            for atendente in self.__atendente_DAO.get_all():
                dados_atendentes.append({"nome": atendente.nome, "cpf": atendente.cpf, "idade": atendente.idade,
                                         "rua": atendente.endereco.rua, "numero": atendente.endereco.numero,
                                         "complemento": atendente.endereco.complemento, "matricula": atendente.matricula,
                                         "salario": atendente.salario})
            self.__tela_atendente.mostra_atendente(dados_atendentes)


    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.inclui_atendente, 2: self.altera_atendente, 3: self.exclui_atendente, 4: self.lista_atendentes,
                        0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_atendente.tela_opcoes()]()

    def retorna_lista_atendentes(self):
        return self.__atendente_DAO.get_all()

