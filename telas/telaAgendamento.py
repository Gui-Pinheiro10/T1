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
        data = input('Data: ')
        codigo_cliente = int(input('Código do Cliente: '))
        matricula_medico_ou_enfermeiro = int(input('Matrícula do Médico ou Enfemeiro: '))
        numero_tipoAgendamento = int(input('Digite apenas 1 ou 2 - [1] Vacina [2] Consulta: '))
        nome_tipoAgendamento = input('Digite a especialidade ou tipo de vacina: ')
        codigo = int(input('Código: '))
        return {"horario": horario, "data": data, "codigo": codigo, "codigo_cliente": codigo_cliente, "numero_tipoAgendamento": numero_tipoAgendamento, "nome_tipoAgendamento": nome_tipoAgendamento, "matricula_medico_ou_enfermeiro": matricula_medico_ou_enfermeiro}

    def pega_dados_para_alterar_agendamento(self):
        print('---------- DADOS PARA ALTERAÇÃO DE AGENDAMENTO ----------')
        print('ATENÇÃO! Só é permitido alterar o horário, data e valor do agendamento.')
        horario = input('Horário: ')
        data = input('Data: ')
        return {"horario": horario, "data": data}

    def seleciona_agendamento(self):
        codigo_agendamento = int(input('Digite o código do agendamento que deseja selecionar: '))
        return codigo_agendamento
