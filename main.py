from pytubefix import YouTube
def leiaint(msg):
    while True:
        try:
            valor = int(input(msg))
            return valor
        except ValueError:
            print('Erro, digite um número inteiro!')

def main():
    while True:
        print('1 - Converter')
        print('2 - Sair')
        opcao = leiaint('escolha uma opção: ')
        if opcao == 1:
            url = input('URL: ').strip()
        elif opcao == 2:
            print("Saindo . . . ")
            break
        else:
            print('Opção inválida')

main()
