from telas.abstractTela import AbstractTela


class TelaEnfermeiro(AbstractTela):
 
    def tela_opcoes(self):
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
        idade = int(input('Idade: '))
        print('Digite os dados do seu endereço abaixo:')
        rua = input('Rua: ')
        numero = int(input('Número: '))
        complemento = input('Complemento: ')
        matricula = int(input('Matrícula: '))
        salario = float(input('Salário: '))
        return {"nome": nome, "cpf": cpf, "idade": idade, "rua": rua, "numero": numero, "complemento": complemento,
                "matricula": matricula, "salario": salario}

    def pega_dados_para_alterar_enfermeiro(self):
        print('---------- DADOS PARA ALTERAÇÃO DE ENFERMEIRO ----------')
        print('ATENÇÃO! Não é permitido alterar CPF e matrícula de enfermeiro.')
        nome = input('Nome: ')
        idade = int(input('Idade: '))
        salario = float(input('Salário: '))
        print('Digite os novos dados do seu endereço abaixo:')
        rua = input('Rua: ')
        numero = int(input('Número: '))
        complemento = input('Complemento: ')
        return {"nome": nome, "idade": idade, "rua": rua, "numero": numero, "complemento": complemento, "salario": salario}

    def seleciona_enfermeiro(self):
        matricula = int(input('Digite a matrícula do enfermeiro que deseja selecionar: '))
        return matricula
