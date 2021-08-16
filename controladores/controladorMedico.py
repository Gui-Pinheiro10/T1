from entidade.medico import Medico
from telas.telaMedico import TelaMedico


class ControladorMedico:
    def __init__(self, controlador_sistema):
       self.__tela_medico = TelaMedico()
       self.__medicos = []
       self.__controlador_sistema = controlador_sistema

    def pega_medico_por_matricula(self, matricula: int):
        for med in self.__medicos:
            if (med.matricula == matricula):
                return med
        return None

    def inclui_medico(self):
        dados_medico = self.__tela_medico.pega_dados_medico()
        medico = Medico(dados_medico["nome"],  dados_medico["cpf"], dados_medico["idade"],
                        dados_medico["rua"], dados_medico["numero"], dados_medico["complemento"],
                        dados_medico["matricula"], dados_medico["salario"], dados_medico["crm"])
        if self.pega_medico_por_matricula(dados_medico["matricula"]) is None:
            self.__medicos.append(medico)
            self.__tela_medico.mostra_mesagem("Médico adicionado com sucesso!")
        else:
            self.__tela_medico.mostra_mesagem("Não foi possível adicionar o médico, pois esta matrícula já está cadastrada.")

    def altera_medico(self):
        self.lista_medicos()
        matricula_medico = self.__tela_medico.seleciona_medico()
        medico = self.pega_medico_por_matricula(matricula_medico)
        if (medico is not None):
            novos_dados_medico = self.__tela_medico.pega_dados_para_alterar_medico()
            medico.nome = novos_dados_medico["nome"]
            medico.idade = novos_dados_medico["idade"]
            medico.endereco.rua = novos_dados_medico["rua"]
            medico.endereco.numero = novos_dados_medico["numero"]
            medico.endereco.complemento = novos_dados_medico["complemento"]
            medico.salario = novos_dados_medico["salario"]
            self.__tela_medico.mostra_mesagem("Médico alterado com sucesso!")
            self.lista_medicos()
        else:
            self.__tela_medico.mostra_mesagem("Não foi possível alterar o médico, pois a matrícula informada não está na lista!")

    def exclui_medico(self):
        self.lista_medicos()
        matricula_medico = self.__tela_medico.seleciona_medico()
        medico = self.pega_medico_por_matricula(matricula_medico)
        if (medico is not None):
            self.__medicos.remove(medico)
            self.__tela_medico.mostra_mesagem("Médico excluído com sucesso!")
            self.lista_medicos()
        else:
            self.__tela_medico.mostra_mesagem('Não foi possível excluir o médico, pois a matrícula informada não está na lista!')

    def lista_medicos(self):
        self.__tela_medico.mostra_mesagem("LISTA DE MÉDICOS".center(30, '-'))
        for medico in self.__medicos:
            self.__tela_medico.mostra_medico({"nome": medico.nome, "cpf": medico.cpf, "idade": medico.idade, "rua": medico.endereco.rua,
                                              "numero": medico.endereco.numero, "complemento": medico.endereco.complemento,
                                              "matricula": medico.matricula, "salario": medico.salario, "crm": medico.crm})
        if len(self.__medicos) == 0:
            self.__tela_medico.mostra_mesagem("No momento a lista de médicos está vazia!")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.inclui_medico, 2: self.altera_medico, 3: self.exclui_medico, 4: self.lista_medicos,
                        0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_medico.tela_opcoes()]()

    def retorna_lista_medicos(self):
        return self.__medicos
