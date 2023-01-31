import calendar, datetime
import sistema as st
import arquivos as aq

ano = datetime.datetime.today().year
mes = datetime.datetime.today().month
dia = datetime.datetime.today().day
horas = datetime.datetime.today().time().hour
minutos = datetime.datetime.today().time().minute
segundos = datetime.datetime.today().time().second

hoje = f'Data: {dia:^3}/{mes:^4}/{ano:^6}'
horario = f'{horas:^5}:{minutos:^6}:{segundos:^6}'
calendario = calendar.month(ano, mes)
print('-=' * 10)
print(calendario.replace(str(f' {dia} '), f'[{str(dia)}]'))
print('-=' * 10)
while True:
    print('-' * 20)
    print(f'{hoje}')
    print(f'{horario}')
    resp = st.menu('Calendário', ['Ver calendário', 'Ver Agenda', 'Saindo do Sistema'])
    if resp == 1:
        while True:
            resp1 = st.menu('Calendário', ['Deste ano', 'Escolher ano', 'Voltar'])
            if resp1 == 1:
                print(calendar.calendar(ano))
                break
            elif resp1 == 2:
                qualAno = st.LeiaInt('Qual ano:')
                print(calendar.calendar(qualAno))
                break
            elif resp1 == 3:
                st.cabecalho2('Voltando ao menu anterior!')
                break
            else:
                print('ERRO! Comando inváido!')

    elif resp == 2:
        while True:
            resp2 = st.menu('Agenda', ['Deste ano', 'Escolher ano', 'Voltar'])
            if resp2 == 1:
                if not aq.arquivoExiste(str(ano)):
                    resp2_1 = st.menu2(f'Não há tarefas para o ano de {ano}', ['add tarefa', 'voltar'])
                    if resp2_1 == 1:
                        aq.criarArquivo(str(ano))
                        aq.lerArquivo(str(ano))

                    elif resp2_1== 2:
                        print('Voltando ao menu anterior!')
                        break
                    else:
                        aq.lerArquivo(str(ano))

            elif resp2 == 2:
                qualAno = st.LeiaInt('Qual ano:')
                if not aq.arquivoExiste(str(qualAno)):
                    aq.criarArquivo(str(qualAno))
                    aq.lerArquivo(str(qualAno))
                else:
                    aq.lerArquivo(str(qualAno))

            elif resp2 == 3:
                st.cabecalho2('Voltando ao menu anterior!')
                break

            else:
                print('ERRO! Comando inválido!')

    elif resp == 3:
        st.cabecalho(' ~ FECHANDO SISTEMA ~ ')
        break
    else:
        st.cabecalho('ERRO! Comando inválido!')

