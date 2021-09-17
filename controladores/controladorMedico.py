from entidade.medico import Medico
from telas.telaMedico import TelaMedico
from DAOs.medico_dao import MedicoDAO


class ControladorMedico:
    def __init__(self, controlador_sistema):
        self.__medico_DAO = MedicoDAO()
        self.__tela_medico = TelaMedico()
        self.__controlador_sistema = controlador_sistema

    def pega_medico_por_cpf(self, cpf: str):
        for med in self.__medico_DAO.get_all():
            if med.cpf == cpf:
                return med
        return None

    def inclui_medico(self):
        dados_medico = self.__tela_medico.pega_dados_medico()
        medico = Medico(dados_medico["nome"],  dados_medico["cpf"], dados_medico["idade"],
                        dados_medico["rua"], dados_medico["numero"], dados_medico["complemento"],
                        dados_medico["matricula"], dados_medico["salario"], dados_medico["crm"])
        try:
            if self.pega_medico_por_cpf(dados_medico["cpf"]) is not None:
                raise Exception
        except Exception:
            self.__tela_medico.mostra_mesagem("Não foi possível adicionar o médico, pois este CPF já está cadastrado.")
        else:
            self.__medico_DAO.add(medico)
            self.__tela_medico.mostra_mesagem("Médico adicionado com sucesso!")

    def altera_medico(self):
        self.lista_medicos()
        cpf_medico = self.__tela_medico.seleciona_medico()
        medico = self.pega_medico_por_cpf(cpf_medico)
        try:
            if medico is None:
                raise Exception
        except Exception:
            self.__tela_medico.mostra_mesagem('Não foi possível alterar o médico, pois este CPF não está cadastrado.')
        else:
            novos_dados_medico = self.__tela_medico.pega_dados_para_alterar_medico()
            medico.nome = novos_dados_medico["nome"]
            medico.idade = novos_dados_medico["idade"]
            medico.endereco.rua = novos_dados_medico["rua"]
            medico.endereco.numero = novos_dados_medico["numero"]
            medico.endereco.complemento = novos_dados_medico["complemento"]
            medico.salario = novos_dados_medico["salario"]
            self.__tela_medico.mostra_mesagem("Médico alterado com sucesso!")
            self.lista_medicos()

    def exclui_medico(self):
        self.lista_medicos()
        cpf_medico = self.__tela_medico.seleciona_medico()
        medico_exluido = self.pega_medico_por_cpf(cpf_medico)
        try:
            if medico_exluido is None:
                raise Exception
        except Exception:
            self.__tela_medico.mostra_mesagem('Não foi possível excluir o médico, pois o CPF informado não está na lista!')
        else:
            self.__medico_DAO.remove(medico_exluido.cpf)
            self.__tela_medico.mostra_mesagem("Médico excluído com sucesso!")
            self.lista_medicos()

    def lista_medicos(self):
       # self.__tela_medico.mostra_mesagem("LISTA DE MÉDICOS".center(30, '-'))
        dados_medico = []
        try:
            if len(self.__medico_DAO.get_all()) == 0:
                raise Exception
        except Exception:
            self.__tela_medico.mostra_mesagem("No momento a lista de médicos está vazia!")
        else:
            for medico in self.__medico_DAO.get_all():
                dados_medico.append({"nome": medico.nome, "cpf": medico.cpf, "idade": medico.idade, "rua": medico.endereco.rua,
                                                  "numero": medico.endereco.numero, "complemento": medico.endereco.complemento,
                                                  "matricula": medico.matricula, "salario": medico.salario, "crm": medico.crm})
                self.__tela_medico.mostra_medico(dados_medico)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.inclui_medico, 2: self.altera_medico, 3: self.exclui_medico, 4: self.lista_medicos,
                        0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_medico.tela_opcoes()]()

    def retorna_lista_medicos(self):
        return self.__medico_DAO.get_all()
