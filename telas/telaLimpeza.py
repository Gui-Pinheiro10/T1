from controladores.controladorLimpeza import ControladorLimpeza
from telas.abstractTela import AbstractTela


class TelaLimpeza(AbstractTela):
    def __init__(self, controlador: ControladorLimpeza):
        self.__controlador = controlador

    def mostra_tela_opcoes(self):
        print("---------- OPÇÕES DE FUNCIONÁRIOS DA LIMPEZA ----------")
        print('1 - Incluir Funcionário da Limpeza')
        print('2 - Alterar Funcionário da Limpeza')
        print('3 - Excluir Funcionário da Limpeza')
        print('4 - Listar os Funcionários da Limpeza')
        print('0 - Retornar')
        opcao = self.le_num_inteiro('Escolha a opção: ', [0, 1, 2, 3, 4])
        return opcao

    def pega_dados_limpeza(self):
        print('---------- DADOS DO FUNCIONÁRIO DA LIMPEZA ----------')
        nome = input('Nome: ')
        cpf = input('CPF: ')
        idade = input('Idade: ')
        print('Digite os dados do seu endereço abaixo:')
        rua = input('Rua: ')
        numero = input('Número: ')
        complemento = input('Complemento: ')
        matricula = input('Matrícula: ')
        salario = input('Salário:')
        return {"nome": nome, "cpf": cpf, "idade": idade, "rua": rua, "numero": numero, "complemento": complemento,
                "matricula": matricula, "salario": salario}

    def pega_dados_para_alterar_limpeza(self):
        print('---------- DADOS PARA ALTERAÇÃO DE FUNCIONÁRIO DA LIMPEZA ----------')
        print('ATENÇÃO! Não é permitido alterar CPF e matrícula de enfermeiro.')
        nome = input('Nome: ')
        idade = input('Idade: ')
        salario = input('Salário: ')
        print('Digite os novos dados do seu endereço abaixo:')
        rua = input('Rua: ')
        numero = input('Número: ')
        complemento = input('Complemento: ')
        return {"nome": nome, "idade": idade, "rua": rua, "numero": numero, "complemento": complemento, "salario": salario}
        
    def seleciona_limpeza(self):
        matricula = input('Digite a matrícula do funcionário da limpeza que deseja selecionar: ')
        return matricula
