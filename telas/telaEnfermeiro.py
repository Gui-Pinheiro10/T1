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

    def pega_dados_para_alterar_enfermeiro(self):
        print('---------- DADOS PARA ALTERAÇÃO DE ENFERMEIRO ----------')
        print('ATENÇÃO! Não é permitido alterar CPF e matrícula de enfermeiro.')
        nome = self.le_str('Nome: ')
        idade = self.verifica_idade('Idade: ')
        salario = self.le_valor_inteiro('Salário: ')
        print('Digite os novos dados do seu endereço abaixo:')
        rua = self.le_str('Rua: ')
        numero = self.le_valor_inteiro('Número: ')
        complemento = self.le_str('Complemento: ')
        return {"nome": nome, "idade": idade, "rua": rua, "numero": numero, "complemento": complemento, "salario": salario}

    def seleciona_enfermeiro(self):
        matricula = self.le_valor_inteiro('Digite a matrícula do enfermeiro que deseja selecionar: ')
        return matricula
