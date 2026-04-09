from pytubefix import  YouTube
from uteis import leiaint,cabecalho,linha,confirmar,init,Fore,Style
from baixar import  baixar_audio
import validators
from interface import interface
import os
def main():
    cabecalho(Fore.CYAN +"yt-audio-extractor")
    while True:
        print('1 - Converter')
        print('2 - Historico de Download')
        print('3 - Sair')
        opcao = leiaint('escolha uma opção: ')
        if opcao == 1:
            url = input("URL: ").strip()
            if not validators.url(url) or ("youtube.com" not in url and "youtu.be" not in url):
                print(Fore.RED + f'erro: URL inválida! use um link do Youtube!')
                continue
            yt = YouTube(url)
            destino = input('DESTINO: ').strip()
            if not destino:
                destino = '.'
            else:
                os.makedirs(destino,exist_ok=True)
            interface(yt)
            resp = confirmar("Quer baixar o arquivo? [S/N]: ")
            if resp == "S":
                resposta = baixar_audio(url, destino)
                if resposta["status"] == 'sucesso':
                    print(Fore.GREEN +f'o Arquivo foi baixado com sucesso! Caminho: {resposta["caminho"]}')
                else:
                    print(Fore.RED+ f'não foi possível baixar: {resposta["mensagem"]}')
            else:
                print("Download cancelado")
        elif opcao ==2:
            print("Historico ainda não implementado")
        elif opcao == 3:
            cabecalho(Fore.LIGHTYELLOW_EX + 'Saindo do programa . . .')
            break
        else:
            print(Fore.RED + 'Opção inválida')

if __name__=='__main__':
    main()
