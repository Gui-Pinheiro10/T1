from controladores.controladorEnfermeiro import ControladorEnfermeiro
from telas.abstractTela import AbstractTela


class TelaEnfermeiro(AbstractTela):
    def __init__(self, controlador: ControladorEnfermeiro):
        self.__controlador = controlador
 
    def mostra_tela_opcoes(self):
        print("---------- OPÇÕES DE ENFERMEIROS ----------")
        print('1 - Incluir Enfermeiro')
        print('2 - Alterar Enfermeiro')
        print('3 - Excluir Enfermeiro')
        print('4 - Listar os Enfermeiros')
        print('0 - Voltar')
        opcao = self.le_num_inteiro('Escolha a opção: ', [0, 1, 2, 3, 4])
        return opcao

    def pega_dados_enfermeiro(self):
        print('---------- DADOS DO ENFERMEIRO ----------')
        nome = input('Nome: ')
        cpf = input('CPF: ')
        idade = input('Idade: ')
        print('Digite os dados do seu endereço abaixo:')
        rua = input('Rua: ')
        numero = input('Número: ')
        complemento = input('Complemento: ')
        matricula = input('Matrícula: ')
        return {"nome": nome, "cpf": cpf, "idade": idade, "rua": rua, "numero": numero, "complemento": complemento,
                "matricula": matricula}
            
    def pega_dados_para_alterar_enfermeiro(self):
        print('---------- DADOS PARA ALTERAÇÃO DE ENFERMEIRO ----------')
        print('ATENÇÃO! Não é permitido alterar CPF e matrícula de enfermeiro.')
        nome = input('Nome: ')
        idade = input('Idade: ')
        print('Digite os novos dados do seu endereço abaixo:')
        rua = input('Rua: ')
        numero = input('Número: ')
        complemento = input('Complemento: ')
        return {"nome": nome, "idade": idade, "rua": rua, "numero": numero, "complemento": complemento}

    def seleciona_enfermeiro(self):
        matricula = input('Digite a matrícula do enfermeiro que deseja selecionar: ')
        return matricula
