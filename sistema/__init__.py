def linha(tam=20):
    if tam <= 20:
        tam = 20
    return '-' * tam

def LeiaInt(n):
    while True:
        try:
            n = int(input(n))
        except (ValueError, TypeError):
            print(f'ERRO! Por favor, dígite um número válido!')
        except KeyboardInterrupt:
            return 0
        else:
            return n

def cabecalho(txt):
    if len(txt) <= 20:
        a = len(txt)
        print(linha(a))
        print(f'{txt:^20}')
        print(linha(a))
    else:
        a = len(txt) + 4
        print(linha(a))
        print(f'{txt:^{a}}')
        print(linha(a))

def cabecalho2(txt):
    if len(txt) <= 20:
        a = len(txt)
        print(f'{txt:^20}')
        print(linha(a))
    else:
        a = len(txt) + 4
        print(f'{txt:^{a}}')
        print(linha(a))

def menu(txt, lista):
    cabecalho(txt)
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = LeiaInt('Sua opção: ')
    return opc

def menu2(txt, lista):
    cabecalho2(txt)
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = LeiaInt('Sua opção: ')
    return opc

def qualMes(mes, dia):
    meses = ['January', 'February', 'March', 'April', 'May', 'June',
             'July', 'August', 'September', 'October', 'November', 'December']

