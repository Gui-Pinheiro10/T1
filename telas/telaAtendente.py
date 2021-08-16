from telas.abstractTela import AbstractTela


class TelaAtendente(AbstractTela):

    def tela_opcoes(self):
        print("\n")
        print(" OPÇÕES DE ATENDENTES".center(30, '*'))
        print("1 - Adicionar Atendente")
        print('2 - Alterar Atendente')
        print('3 - Excluir Atendente')
        print('4 - Lista de Atendentes')
        print('0 - Retornar')
        opcao = self.le_num_inteiro("Escolha a opção: ", [1, 2, 3, 4, 0])
        print("\n")
        return opcao

    def pega_dados_atendente(self):
        print(' DADOS DO ATENDENTE '.center(30, "*"))
        nome = input("Nome: ")
        cpf = input("CPF: ")
        idade = int(input("Idade: "))
        print("Digite o seu Endereço abaixo.")
        rua = input("Rua: ")
        numero = int(input("Número: "))
        complemento = input("Complemento: ")
        matricula = int(input("Matrícula: "))
        salario = float(input("Salário: "))
        return {"nome": nome, "cpf": cpf, "idade": idade, "rua": rua, "numero": numero,
                "complemento": complemento, "matricula": matricula, "salario": salario}

    def pega_dados_para_alterar_atendente(self):
        print('ATENÇÃO! Não é permitido alterar CPF e matrícula de atendente.')
        print(" DADOS DE ATENDENTE ".center(30, '*'))
        nome = input('Nome: ')
        idade = int(input('Idade: '))
        print('Digite os novos dados do seu endereço abaixo:')
        rua = input('Rua: ')
        numero = int(input('Número: '))
        complemento = input('Complemento: ')
        salario = float(input("Salário: "))
        return {"nome": nome, "idade": idade, "rua": rua, "numero": numero,
                "complemento": complemento, "salario": salario}

    def mostra_atendente(self, dados_atendente):
        print("NOME: ", dados_atendente["nome"])
        print("CPF: ",dados_atendente["cpf"])
        print("IDADE: ", dados_atendente["idade"])
        print("SALÁRIO: ", dados_atendente["salario"])
        print("MATRÍCULA: ", dados_atendente["matricula"])
        print("ENDEREÇO: Rua: ",dados_atendente["rua"], "// Número: ",dados_atendente["numero"], "// Complemento: ", dados_atendente["complemento"])
        print('\n')

    def seleciona_atendente(self):
        matricula = int(input('Digite a matrícula do atendente que deseja selecionar: '))
        return matricula
