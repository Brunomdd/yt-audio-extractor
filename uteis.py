def linha(txt=32):
    return '-'*txt

def cabecalho(txt):
    print(linha())
    print(f'{txt}'.center(32))
    print(linha())

def leiaint(msg):
    while True:
        try:
            valor = int(input(msg))
            return valor
        except ValueError:
            print('Erro, digite um número inteiro!')