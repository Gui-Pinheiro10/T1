from telas.abstractTela import AbstractTela


class TelaAgendamento(AbstractTela):
    
    def tela_opcoes(self):
        print("---------- OPÇÕES DE AGENDAMENTOS ----------")
        print('1 - Incluir Agendamento')
        print('2 - Alterar Agendamento')
        print('3 - Excluir Agendamento')
        print('4 - Listar Agendamento')
        print('0 - Retornar')
        opcao = self.le_num_inteiro('Escolha a opção: ', [0, 1, 2, 3, 4])
        return opcao

    def pega_dados_agendamento(self):
        print('---------- DADOS DO AGENDAMENTO ----------')
        horario = input('Horário: ')
        valor = input('Valor: ')
        data = input('Data: ')
        cliente = input('Cliente: ')
        tipoAgendamento = input('Tipo de Agendamento: ')
        codigo = input('Código: ')
        return {"horario": horario, "valor": valor, "data": data, "codigo": codigo, "cliente": cliente, "tipoAgendamento": tipoAgendamento}

    def pega_dados_para_alterar_agendamento(self):
        print('---------- DADOS PARA ALTERAÇÃO DE AGENDAMENTO ----------')
        print('ATENÇÃO! Não é permitido alterar o código do agendamento.')
        horario = input('Horário: ')
        valor = input('Valor: ')
        data = input('Data: ')
        cliente = input('Cliente: ')
        tipoAgendamento = input('Tipo de Agendamento: ')
        return {"horario": horario, "valor": valor, "data": data, "cliente": cliente, "tipoAgendamento": tipoAgendamento}

    def seleciona_agendamento(self):
        codigo_agendamento = input('Digite o código do agendamento que deseja selecionar: ')
        return codigo_agendamento
