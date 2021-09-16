from entidade.atendente import Atendente
from telas.telaAtendente import TelaAtendente


class ControladorAtendente:
    def __init__(self, controlador_sistema):
        self.__tela_atendente = TelaAtendente()
        self.__atendentes = []
        self.__controlador_sistema = controlador_sistema

    def pega_atendente_por_matricula(self, matricula: int):
        for atendente in self.__atendentes:
            if (atendente.matricula == matricula):
                return atendente
        return None

    def inclui_atendente(self):
        dados_atendente = self.__tela_atendente.pega_dados_atendente()
        atendente = Atendente(dados_atendente["nome"], dados_atendente["cpf"], dados_atendente["idade"],
                              dados_atendente["rua"], dados_atendente["numero"], dados_atendente["complemento"],
                              dados_atendente["matricula"], dados_atendente["salario"])
        try:
            if self.pega_atendente_por_matricula(dados_atendente["matricula"]) is not None:
                raise Exception
        except Exception:
            self.__tela_atendente.mostra_mesagem("Não foi possível cadastrar o enfermeiro pois a matrícula já existe!")
        else:
            self.__atendentes.append(atendente)
            self.__tela_atendente.mostra_mesagem("Atendente adicionado com sucesso!")

    def altera_atendente(self):
        self.lista_atendentes()
        matricula_atendente = self.__tela_atendente.seleciona_atendente()
        atendente = self.pega_atendente_por_matricula(matricula_atendente)
        try:
            if atendente is None:
                raise Exception
        except Exception:
            self.__tela_atendente.mostra_mesagem("Não foi possível alterar o atendente, pois a matrícula informada não está na lista!")
        else:
            novos_dados_atendente = self.__tela_atendente.pega_dados_para_alterar_atendente()
            atendente.nome = novos_dados_atendente["nome"]
            atendente.idade = novos_dados_atendente["idade"]
            atendente.endereco.rua = novos_dados_atendente["rua"]
            atendente.endereco.numero = novos_dados_atendente["numero"]
            atendente.endereco.complemento = novos_dados_atendente["complemento"]
            atendente.salario = novos_dados_atendente["salario"]
            self.__tela_atendente.mostra_mesagem("Atendente alterado com sucesso!")
            self.lista_atendentes()

    def exclui_atendente(self):
        self.lista_atendentes()
        marticula_atendente = self.__tela_atendente.seleciona_atendente()
        atendente = self.pega_atendente_por_matricula(marticula_atendente)
        try:
            if atendente is None:
                raise Exception
        except Exception:
            self.__tela_atendente.mostra_mesagem("Não foi possível excluir o atendente, pois a matrícula informada não está na lista!")
        else:
            self.__atendentes.remove(atendente)
            self.__tela_atendente.mostra_mesagem("Atendente excluído com sucesso!")
            self.lista_atendentes()

    def lista_atendentes(self):
       # self.__tela_atendente.mostra_mesagem("LISTA DE ATENDENTES".center(30, '*'))
        dados_atendente = []
        try:
            if len(self.__atendentes) == 0:
                raise Exception
        except Exception:
            self.__tela_atendente.mostra_mesagem("No momento a lista de atendentes está vazia!")
        else:
            for atendente in self.__atendentes:
                dados_atendente.append({"nome": atendente.nome, "cpf": atendente.cpf, "idade": atendente.idade,
                                                        "rua": atendente.endereco.rua, "numero": atendente.endereco.numero,
                                                        "complemento": atendente.endereco.complemento, "matricula": atendente.matricula,
                                                        "salario": atendente.salario})
                self.__tela_atendente.mostra_atendente(dados_atendente)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.inclui_atendente, 2: self.altera_atendente, 3: self.exclui_atendente, 4: self.lista_atendentes,
                        0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_atendente.tela_opcoes()]()
