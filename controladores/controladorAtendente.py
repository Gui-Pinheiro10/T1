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
        if self.pega_atendente_por_matricula(dados_atendente["matricula"]) is None:
            self.__atendentes.append(atendente)
            self.__tela_atendente.mostra_mesagem("Atendente adicionado com sucesso!")
        else:
            self.__tela_atendente.mostra_mesagem("Não foi possível cadastrar o enfermeiro pois a matrícula já existe!")

    def altera_atendente(self):
        self.lista_atendentes()
        matricula_atendente = self.__tela_atendente.seleciona_atendente()
        atendente = self.pega_atendente_por_matricula(matricula_atendente)
        if (atendente is not None):
            novos_dados_atendente = self.__tela_atendente.pega_dados_para_alterar_atendente()
            atendente.nome = novos_dados_atendente["nome"]
            atendente.idade = novos_dados_atendente["idade"]
            atendente.endereco.rua = novos_dados_atendente["rua"]
            atendente.endereco.numero = novos_dados_atendente["numero"]
            atendente.endereco.complemento = novos_dados_atendente["complemento"]
            atendente.salario = novos_dados_atendente["salario"]
            self.__tela_atendente.mostra_mesagem("Atendente alterado com sucesso!")
            self.lista_atendentes()
        else:
            self.__tela_atendente.mostra_mesagem("Não foi possível alterar o atendente, pois a matrícula informada não está na lista!")

    def exclui_atendente(self):
        self.lista_atendentes()
        marticula_atendente = self.__tela_atendente.seleciona_atendente()
        atendente = self.pega_atendente_por_matricula(marticula_atendente)
        if (atendente is not None):
            self.__atendentes.remove(atendente)
            self.__tela_atendente.mostra_mesagem("Atendente excluído com sucesso!")
            self.lista_atendentes()
        else:
            self.__tela_atendente.mostra_mesagem("Não foi possível excluir o atendente, pois a matrícula informada não está na lista!")

    def lista_atendentes(self):
        self.__tela_atendente.mostra_mesagem("LISTA DE ATENDENTES".center(30, '*'))
        for atendente in self.__atendentes:
            self.__tela_atendente.mostra_atendente(f'Nome: {atendente.nome} | CPF: {atendente.cpf} | Idade: {atendente.idade}\nRua: {atendente.endereco.rua} | Número: {atendente.endereco.numero} | Complemento: {atendente.endereco.complemento}\nMatrícula: {atendente.matricula} |Salário: {atendente.salario}')
        if len(self.__atendentes) == 0:
            self.__tela_atendente.mostra_mesagem("No momento a lista de atendentes está vazia!")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.inclui_atendente, 2: self.altera_atendente, 3: self.exclui_atendente, 4: self.lista_atendentes,
                        0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_atendente.tela_opcoes()]()
