from uteis import leiaint,cabecalho,linha,confirmar
from baixar import  baixar_audio
import validators
from interface import interface

def main():
    cabecalho("yt-audio-extractor")
    while True:
        print('1 - Converter')
        print('2 - Sair')
        opcao = leiaint('escolha uma opção: ')
        if opcao == 1:
            url = input("URL: ").strip()
            if not validators.url(url) or ('youtube.com' not in url and "youtu.be" not in url):
                print(f'erro: URL inválida! use um link do Youtube!')
                continue

            destino = input('DESTINO: ').strip()
            interface(url)
            resp = confirmar("Quer baixar o arquivo? [S/N]: ")
            if resp == "S":
                resposta = baixar_audio(url, destino)
                if resposta['status'] == 'sucesso':
                    print(f'Arquivo baixado com sucesso! Caminho: {resposta['caminho']}')
                else:
                    if resposta['status'] == 'erro':
                        print(f'não foi possível baixar: {resposta['mensagem']}')
            else:
                print("Download cancelado")

        elif opcao == 2:
            cabecalho('Saindo do programa . . .')
            break
        else:
            print('Opção inválida')

if __name__=='__main__':
    main()
