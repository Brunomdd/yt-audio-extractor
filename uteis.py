def leiaint(msg):
    while True:
        try:
            valor = int(input(msg))
            return valor
        except ValueError:
            print('Erro, digite um número inteiro!')