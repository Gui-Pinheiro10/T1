from entidade.limpeza import Limpeza
from telas.telaLimpeza import TelaLimpeza
from DAOs.limpeza_dao import LimpezaDAO


class ControladorLimpeza:
    def __init__(self, controlador_sistema):
        #self.__limpezas = []
        self.__limpezas_DAO = LimpezaDAO()

        self.__tela_limpeza = TelaLimpeza()
        self.__controlador_sistema = controlador_sistema

    def inclui_limpeza(self): # VISTO
        dados_limpeza = self.__tela_limpeza.pega_dados_limpeza()
        limpeza = Limpeza(dados_limpeza["nome"], dados_limpeza["cpf"], dados_limpeza["idade"], dados_limpeza["rua"], dados_limpeza["numero"],
                          dados_limpeza["complemento"], dados_limpeza["matricula"], dados_limpeza["salario"])
        try:
            if self.pega_limpeza_por_matricula(dados_limpeza["matricula"]) is not None:
                raise Exception
        except Exception:
            self.__tela_limpeza.mostra_mesagem('Não foi possível cadastrar o funcionário pois a matrícula já existe!')
        else:
            self.__limpezas_DAO.add(limpeza)
            self.__tela_limpeza.mostra_mesagem('Funcionário da Limpeza adicionado com sucesso!')

    def exclui_limpeza(self): # VISTO
        self.listar_limpezas()
        cpf_funcionario_excluido =  self.__tela_limpeza.seleciona_limpeza()
        funcionario_excluido = self.pega_limpeza_por_cpf(cpf_funcionario_excluido)
        try:
            if funcionario_excluido is None:
                raise Exception
        except Exception:
            self.__tela_limpeza.mostra_mesagem('Não foi possível excluir o funcionário, pois a matrícula informada não está na lista!')
        else:
            self.__limpezas_DAO.remove(funcionario_excluido.cpf)
            self.__tela_limpeza.mostra_mesagem('Funcionário da Limpeza excluído com sucesso!')
            self.listar_limpezas()

    def altera_limpeza(self):
        self.listar_limpezas()
        cpf_funcionario_alterado = self.__tela_limpeza.seleciona_limpeza()
        funcionario_alterado = self.pega_limpeza_por_cpf(cpf_funcionario_alterado)
        try:
            if funcionario_alterado is None:
                raise Exception
        except Exception:
            self.__tela_limpeza.mostra_mesagem('Não foi possível alterar o funcionário, pois a matrícula informada não está na lista!')
        else:
            for funcionario_limpeza in self.__limpezas_DAO:
                if funcionario_limpeza.cpf == cpf_funcionario_alterado:
                    novos_dados = self.__tela_limpeza.pega_dados_para_alterar_limpeza()
                    funcionario_limpeza.nome = novos_dados["nome"]
                    funcionario_limpeza.idade = novos_dados["idade"]
                    funcionario_limpeza.endereco.rua = novos_dados["rua"]
                    funcionario_limpeza.endereco.numero = novos_dados["numero"]
                    funcionario_limpeza.endereco.complemento = novos_dados["complemento"]
                    funcionario_limpeza.salario = novos_dados["salario"]
                    self.__tela_limpeza.mostra_mesagem('Funcionário da limpeza alterado com sucesso!\n')
                    self.listar_limpezas()

    def listar_limpezas(self):
        dados_limpezas = []
        self.__tela_limpeza.mostra_mesagem("LISTA DE FUNCIONÁRIO".center(30, '-'))
        try:
            if len(self.__limpezas_DAO) == 0:
                raise Exception
        except Exception:
            self.__tela_limpeza.mostra_mesagem("No momento a lista de funcionários de limpeza está vazia.")
        else:
            for limpeza in self.__limpezas_DAO:
                dados_limpezas.append({"nome": limpeza.nome, "idade": limpeza.idade, "cpf": limpeza.cpf, "salario": limpeza.salario, "matricula": limpeza.matricula, "rua": limpeza.rua, "numero": limpeza.numero, "complemento": limpeza.complemento})
                self.__tela_limpeza.mostra_limpeza(dados_limpezas)

    def pega_limpeza_por_cpf(self, cpf: int):
        for limpeza in self.__limpezas_DAO.get_all():
            print(limpeza.cpf)
            if limpeza.cpf == cpf:
                return limpeza
        return None

    def retornar(self):
        self.__controlador_sistema.abre_tela()
    
    def abre_tela(self):
        opcoes = {0: self.retornar, 1: self.inclui_limpeza, 2: self.altera_limpeza, 3: self.exclui_limpeza, 4: self.listar_limpezas}
        continua = True
        while continua:
            opcoes[self.__tela_limpeza.tela_opcoes()]()
