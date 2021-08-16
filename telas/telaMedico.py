from telas.abstractTela import AbstractTela


class TelaMedico(AbstractTela):

    def tela_opcoes(self):
        print('\n')
        print("OPÇÕES DE MÉDICOS".center(30, '*'))
        print("1 - Adicionar Médico")
        print("2 - Alterar Médico")
        print("3 - Excluir Médico")
        print("4 - Lista de Médicos")
        print("0 - Retornar")
        opcao = self.le_num_inteiro("Escolha a opção: ", [1, 2, 3, 4, 0])
        print("\n")
        return opcao

    def pega_dados_medico(self):
        print(" DADOS MÉDICO ".center(30,"*"))
        nome = input("Nome: ")
        cpf = self.verifica_cpf()
        idade = self.verifica_idade("Idade: ")
        print("Digite o seu Endereço abaixo.")
        rua = input("Rua: ")
        numero = self.le_valor_inteiro("Número: ")
        complemento = input("Complemento: ")
        matricula = self.le_valor_inteiro("Matrícula: ")
        salario = self.le_valor_inteiro("Salário: ")
        crm = input("CRM: ")
        return {"nome": nome, "cpf": cpf, "idade": idade, "rua": rua, "numero": numero,
                 "complemento": complemento, "matricula": matricula, "salario": salario, "crm": crm}

    def pega_dados_para_alterar_medico(self):
        print("ATENÇÃO! Não é possível alterar CPF, matrícula e CRM do médico.")
        print(" DADOS DO MÉDICO ".center(30, "*"))
        nome = input("Nome: ")
        idade = self.verifica_idade("Idade: ")
        print("Digite o seu Endereço abaixo.")
        rua = input("Rua: ")
        numero = self.le_valor_inteiro("Número: ")
        complemento = input("Complemento: ")
        salario = self.le_valor_inteiro("Salário: ")
        return {"nome": nome, "idade": idade, "rua": rua, "numero": numero,
                "complemento": complemento, "salario": salario}

    def mostra_medico(self, dados_medico):
        print("NOME: ",dados_medico["nome"])
        print("CPF: ",dados_medico["cpf"])
        print("IDADE: ",dados_medico["idade"])
        print("ENDEREÇO: Rua: ",dados_medico["rua"],
              "// Número: ",dados_medico["numero"], "// Complemento: ",
              dados_medico["complemento"])
        print("MATRÍCULA: ", dados_medico["matricula"])
        print("SALÁRIO: ",dados_medico["salario"])
        print("CRM: ", dados_medico["crm"])
        print("\n")

    def seleciona_medico(self):
        matricula = self.le_valor_inteiro('Digite a matrícula do Médico que deseja selecionar: ')
        return matricula
