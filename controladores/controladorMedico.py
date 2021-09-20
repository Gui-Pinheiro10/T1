from entidade.medico import Medico
from telas.telaMedico import TelaMedico
from DAOs.medico_dao import MedicoDAO


class ControladorMedico:

    def __init__(self, controlador_sistema):
        self.__medico_DAO = MedicoDAO()
        self.__tela_medico = TelaMedico()
        self.__controlador_sistema = controlador_sistema

    def pega_medico_por_cpf(self, cpf: str):
        for medico in self.__medico_DAO.get_all():
            if medico.cpf == cpf:
                return medico
        return None

    def inclui_medico(self):
        dados_medico = self.__tela_medico.pega_dados_medico()
        if dados_medico is not None:
            try:
                if self.pega_medico_por_cpf(dados_medico["cpf"]) is not None:
                    raise Exception
            except Exception:
                self.__tela_medico.mostra_mesagem("Não foi possível adicionar o médico, pois este CPF já está cadastrado.")
            else:
                medico = Medico(dados_medico["nome"], dados_medico["cpf"], dados_medico["idade"],
                                      dados_medico["rua"], dados_medico["numero"],
                                      dados_medico["complemento"], dados_medico["matricula"],
                                      dados_medico["salario"], dados_medico["crm"])
                self.__medico_DAO.add(medico)
                self.__tela_medico.mostra_mesagem("Médico adicionado com sucesso!")


    def altera_medico(self):
        self.lista_medicos()
        cpf_pessoa = self.__tela_medico.seleciona_medico()
        medico_alterado = self.pega_medico_por_cpf(cpf_pessoa)
        try:
            if medico_alterado is None:
                raise Exception
        except Exception:
            self.__tela_medico.mostra_mesagem("Não foi possível alterar este cadastro, pois este CPF não está cadastrado.")
        else:
            novos_dados_pessoa = self.__tela_medico.pega_dados_para_alterar_medico()
            if novos_dados_pessoa is not None:
                medico_alterado.nome = novos_dados_pessoa["nome"]
                medico_alterado.idade = novos_dados_pessoa["idade"]
                medico_alterado.endereco.rua = novos_dados_pessoa["rua"]
                medico_alterado.endereco.numero = novos_dados_pessoa["numero"]
                medico_alterado.endereco.complemento = novos_dados_pessoa["complemento"]
                medico_alterado.salario = novos_dados_pessoa["salario"]
                self.__tela_medico.mostra_mesagem("Médico alterado com sucesso!")
                self.lista_medicos()

    def exclui_medico(self):
        self.lista_medicos()
        codigo_med = self.__tela_medico.seleciona_medico()
        medico_excluido = self.pega_medico_por_cpf(codigo_med)
        try:
            if medico_excluido is None:
                raise Exception
        except Exception:
            self.__tela_medico.mostra_mesagem("Não foi possível excluir este cadastro, pois este CPF não está cadastrado.")
        else:
            self.__medico_DAO.remove(medico_excluido.cpf)
            self.__tela_medico.mostra_mesagem('Médico excluído com sucesso!')
            self.lista_medicos()

    def lista_medicos(self):
        dados_medicos = []
        try:
            if len(self.__medico_DAO.get_all()) == 0:
                raise Exception
        except Exception:
            self.__tela_medico.mostra_mesagem('No momento, a lista de médicos está vazia.')
        else:
            for med in self.__medico_DAO.get_all():
                dados_medicos.append({"nome": med.nome, "cpf": med.cpf, "idade": med.idade,
                                         "rua": med.endereco.rua, "numero": med.endereco.numero,
                                         "complemento": med.endereco.complemento, "matricula": med.matricula,
                                         "salario": med.salario, "crm": med.crm})
            self.__tela_medico.mostra_medico(dados_medicos)

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
