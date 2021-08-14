from telas.abstractTela import AbstractTela


class TelaCliente(AbstractTela):

    def tela_opcoes(self):
        print('\n')
        print(" CADASTRO CLIENTES ".center(30, '*'))
        print('1 - Adicionar Cliente')
        print('2 - Alterar Cliente')
        print('3 - Excluir Cliente')
        print('4 - Lista de Clientes')
        print('0 - Retornar')
        opcao = self.le_num_inteiro("Escolha a opção: ", [1, 2, 3, 4, 0])
        print("\n")
        return opcao

    def pega_dados_cliente(self):
        print(' DADOS DO CLIENTE '.center(30, '*'))
        nome = input("Nome: ")
        cpf = input("CPF: ")
        idade = int(input("Idade: "))
        print("Digite o seu Endereço abaixo.")
        rua = input("Rua: ")
        numero = int(input("Número: "))
        complemento = input("Complemento: ")
        codigo = int(input("Código: "))
        return {"nome": nome, "cpf": cpf, "idade": idade, "rua": rua, "numero": numero, "complemento": complemento,
                "codigo": codigo}

    def pega_dados_para_alterar_cliente(self):
        print('ATENÇÃO. Não é possível alterar CPF ou Código do cliente.')
        print(' DADOS DO CLIENTES '.center(30, '*')) 
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        print("Digite o seu Endereço abaixo.")
        rua = input("Rua: ")
        numero = int(input("Número: "))
        complemento = input("Complemento: ")
        return {"nome": nome, "idade": idade, "rua": rua, "numero": numero, "complemento": complemento}

    def mostra_cliente(self, dados_cliente):
        print("NOME: ", dados_cliente["nome"])
        print("CPF: ",dados_cliente["cpf"])
        print("IDADE: ",dados_cliente["idade"])
        print("ENDEREÇO: Rua: ",dados_cliente["rua"], "// Número: ",dados_cliente["numero"], "// Complemento: ", dados_cliente["complemento"])
        print("CÓDIGO: ",dados_cliente["codigo"])
        print("\n")

    def seleciona_cliente(self):
        codigo = int(input("Código do cliente que deseja selecionar: "))
        return codigo
        
