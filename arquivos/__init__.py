import calendario.Calendario.sistema as st
import calendar

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt', encoding='UTF = 8')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+', encoding='UTF = 8')
        a.close()
    except:
        print('Houve um ERRO ao criar o arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt', encoding='UTF = 8')
    except:
        print('ERRO! Arquivo não encontrado.')
    else:
        print('-' * 10)
        print(f'{"agenda":^10}')
        print('-' * 10)
        for linha in a:
            print(f'{linha}', end='')
        print()
    finally:
        a.close()

def cadastrar(nome, txt=''):
    meses = {'January': '', 'February': '', 'March': '', 'April': '', 'May': '', 'June': '',
             'July': '', 'August': '', 'September': '', 'October': '', 'November': '', 'December': ''}
    try:
        a = open(nome, 'at')
    except:
        print('Houve um ERRO na abertura de arquivo!')
    else:
        try:
            a.write(str(meses))
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro foi adicionado.')
            a.close()

def nomeArquivo(nome):
    while True:
        print(nome)
        qual_ano = st.LeiaInt('Qual Ano? ')
        qual_mes = st.LeiaInt('Qual mês? ')
        print(f'    ANO: {qual_ano}\n    MÊS: {qual_mes}')
        confirma = st.menu2('Mês e ano estão corretos?', ['Sim', 'Não'])
        if confirma == 1:
            nome_arquivo = f'{qual_ano}.{qual_mes}'
            return nome_arquivo, qual_mes, qual_ano

def anotar(nome, txt):
    try:
        a = open(nome, 'at')
    except:
        print('Houve um ERRO na abertura de arquivo!')
    else:
        try:
            a.write(calendar.calendar(txt))
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro foi adicionado.')
            a.close()
