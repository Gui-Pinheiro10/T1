from entidade.limpeza import Limpeza
from telas.telaLimpeza import TelaLimpeza
from DAOs.limpeza_dao import LimpezaDAO


class ControladorLimpeza:
    def __init__(self, controlador_sistema):
        self.__limpezas_DAO = LimpezaDAO()

        self.__tela_limpeza = TelaLimpeza()
        self.__controlador_sistema = controlador_sistema

    def pega_limpeza_por_cpf(self, cpf: int):
        for limpeza in self.__limpezas_DAO.get_all():
            if limpeza.cpf == cpf:
                return limpeza
        return None

    def inclui_limpeza(self):
        dados_limpeza = self.__tela_limpeza.pega_dados_limpeza()
        if dados_limpeza == 'Cancelar':
            self.__tela_limpeza.close()
            self.__tela_limpeza.open()
        else:
            try:
                if self.pega_limpeza_por_cpf(dados_limpeza["cpf"]) is not None:
                    raise Exception
            except Exception:
                self.__tela_limpeza.mostra_mesagem('Não foi possível cadastrar o funcionário pois o CPF já está cadastrado!')
            else:
                limpeza = Limpeza(dados_limpeza["nome"], dados_limpeza["cpf"], dados_limpeza["idade"], dados_limpeza["rua"],
                                  dados_limpeza["numero"],
                                  dados_limpeza["complemento"], dados_limpeza["matricula"], dados_limpeza["salario"])
                self.__limpezas_DAO.add(limpeza)
                self.__tela_limpeza.mostra_mesagem('Funcionário da Limpeza adicionado com sucesso!')

    def exclui_limpeza(self):
        self.listar_limpezas()
        cpf_funcionario_excluido =  self.__tela_limpeza.seleciona_limpeza()
        if cpf_funcionario_excluido == 'Cancelar':
            self.__tela_limpeza.close()
            self.__tela_limpeza.open()
        else:
            funcionario_excluido = self.pega_limpeza_por_cpf(cpf_funcionario_excluido)
            try:
                if funcionario_excluido is None:
                    raise Exception
            except Exception:
                self.__tela_limpeza.mostra_mesagem('Não foi possível excluir o funcionário, pois o CPF informado informada não está na lista!')
            else:
                self.__limpezas_DAO.remove(funcionario_excluido.cpf)
                self.__tela_limpeza.mostra_mesagem('Funcionário da Limpeza excluído com sucesso!')
                self.listar_limpezas()

    def altera_limpeza(self):
        self.listar_limpezas()
        cpf_funcionario_alterado = self.__tela_limpeza.seleciona_limpeza()
        if cpf_funcionario_alterado == 'Cancelar':
            self.__tela_limpeza.close()
            self.__tela_limpeza.open()
        else:
            funcionario_alterado = self.pega_limpeza_por_cpf(cpf_funcionario_alterado)
            try:
                if funcionario_alterado is None:
                    raise Exception
            except Exception:
                self.__tela_limpeza.mostra_mesagem('Não foi possível alterar o funcionário, pois o CPF informado não está na lista!')
            else:
                novos_dados_limpeza = self.__tela_limpeza.pega_dados_para_alterar_limpeza()
                funcionario_alterado.nome = novos_dados_limpeza["nome"]
                funcionario_alterado.idade = novos_dados_limpeza["idade"]
                funcionario_alterado.endereco.rua = novos_dados_limpeza["rua"]
                funcionario_alterado.endereco.numero = novos_dados_limpeza["numero"]
                funcionario_alterado.endereco.complemento = novos_dados_limpeza["complemento"]
                funcionario_alterado.salario = novos_dados_limpeza["salario"]
                self.__tela_limpeza.mostra_mesagem('Funcionário da limpeza alterado com sucesso!\n')
                self.listar_limpezas()

    def listar_limpezas(self):
        dados_limpezas = []
        try:
            if len(self.__limpezas_DAO.get_all()) == 0:
                raise Exception
        except Exception:
            self.__tela_limpeza.mostra_mesagem("No momento a lista de funcionários de limpeza está vazia.")
        else:
            for limpeza in self.__limpezas_DAO.get_all():
                dados_limpezas.append({"nome": limpeza.nome, "idade": limpeza.idade, "cpf": limpeza.cpf,
                                       "salario": limpeza.salario, "matricula": limpeza.matricula,
                                       "rua": limpeza.endereco.rua, "numero": limpeza.endereco.numero,
                                       "complemento": limpeza.endereco.complemento})
            self.__tela_limpeza.mostra_limpeza(dados_limpezas)

    def retornar(self):
        self.__controlador_sistema.abre_tela()
    
    def abre_tela(self):
        opcoes = {0: self.retornar, 1: self.inclui_limpeza, 2: self.altera_limpeza, 3: self.exclui_limpeza, 4: self.listar_limpezas}
        continua = True
        while continua:
            opcoes[self.__tela_limpeza.tela_opcoes()]()
