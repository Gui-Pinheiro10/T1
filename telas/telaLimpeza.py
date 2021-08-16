from telas.abstractTela import AbstractTela


class TelaLimpeza(AbstractTela):

    def tela_opcoes(self):
        print("---------- OPÇÕES DE FUNCIONÁRIOS DA LIMPEZA ----------")
        print('1 - Incluir Funcionário da Limpeza')
        print('2 - Alterar Funcionário da Limpeza')
        print('3 - Excluir Funcionário da Limpeza')
        print('4 - Listar os Funcionários da Limpeza')
        print('0 - Retornar')
        opcao = self.le_num_inteiro('Escolha a opção: ', [0, 1, 2, 3, 4])
        print('\n')
        return opcao

    def pega_dados_limpeza(self):
        print('---------- DADOS DO FUNCIONÁRIO DA LIMPEZA ----------')
        nome = self.le_str('Nome: ')
        cpf = self.verifica_cpf()
        idade = self.verifica_idade('Idade: ')
        print('Digite os dados do seu endereço abaixo:')
        rua = self.le_str('Rua: ')
        numero = self.le_valor_inteiro('Número: ')
        complemento = self.le_str('Complemento: ')
        matricula = self.le_valor_inteiro('Matrícula: ')
        salario = self.le_valor_inteiro('Salário: ')
        return {"nome": nome, "cpf": cpf, "idade": idade, "rua": rua, "numero": numero, "complemento": complemento,
                "matricula": matricula, "salario": salario}

    def pega_dados_para_alterar_limpeza(self):
        print('---------- DADOS PARA ALTERAÇÃO DE FUNCIONÁRIO DA LIMPEZA ----------')
        print('ATENÇÃO! Não é permitido alterar CPF e matrícula de funcionário de limpeza.')
        nome = self.le_str('Nome: ')
        idade = self.le_valor_inteiro('Idade: ')
        salario = self.le_valor_inteiro('Salário: ')
        print('Digite os novos dados do seu endereço abaixo:')
        rua = self.le_str('Rua: ')
        numero = self.le_valor_inteiro('Número: ')
        complemento = self.le_str('Complemento: ')
        return {"nome": nome, "idade": idade, "rua": rua, "numero": numero, "complemento": complemento, "salario": salario}

    def mostra_funcionario_limpeza(self, dados_funcionario):
        print("NOME: ", dados_funcionario["nome"])
        print("CPF: ",dados_funcionario["cpf"])
        print("IDADE: ", dados_funcionario["idade"])
        print("SALÁRIO: ", dados_funcionario["salario"])
        print("MATRÍCULA: ", dados_funcionario["matricula"])
        print("ENDEREÇO: Rua: ",dados_funcionario["rua"], "// Número: ",dados_funcionario["numero"], "// Complemento: ", dados_funcionario["complemento"])

    def seleciona_limpeza(self):
        matricula = self.le_valor_inteiro('Digite a matrícula do funcionário da limpeza que deseja selecionar: ')
        return matricula
