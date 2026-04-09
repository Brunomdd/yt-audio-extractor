from colorama import init,Fore,Style
init(autoreset=True)
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
            print(Fore.RED + 'Erro, digite um número inteiro!' )

def confirmar(msg):
    while True:
        resp = str(input(msg)).strip().upper()
        if resp in ('S','N'):
            return resp
        print(Fore.RED+ "Resposta inválida! Digite [S/N]!" )

