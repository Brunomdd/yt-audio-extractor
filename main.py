from pytubefix import YouTube

def main():
    while True:
        print('1 - Converter')
        print('2 - Sair')
        opcao = int(input('escolha uma opção: '))
        if opcao == 1:
            url = input('URL: ').strip()
        elif opcao == 2:
            print("Saindo . . . ")
            break
        else:
            print('Opção inválida')

main()
