from uteis import leiaint,cabecalho,linha
from baixar import  baixar_audio

def main():

    cabecalho("yt-audio-extractor")
    while True:

        print('1 - Converter')
        print('2 - Sair')
        opcao = leiaint('escolha uma opção: ')
        if opcao == 1:
            url = input('URL: ').strip()
            destino = input('DESTINO: ').strip()
            if not destino:
                resposta = baixar_audio(url)
                if resposta:
                    print('Àudio baixado com sucesso!')
                else:
                    print('Não foi possivel baixar o video')
            else:
                resposta = baixar_audio(url, destino)
                print(f"Àudio baixado com sucesso ao destino {destino}")

        elif opcao == 2:
            cabecalho('Saindo do programa . . .')
            break
        else:
            print('Opção inválida')

main()
