from uteis import leiaint,cabecalho,linha,confirmar
from baixar import  baixar_audio
import validators
from interface import interface,init,Fore,Style
import os


def main():
    cabecalho(Fore.CYAN +"yt-audio-extractor" + Style.RESET_ALL)
    while True:
        print('1 - Converter')
        print('2 - Sair')
        opcao = leiaint('escolha uma opção: ')
        if opcao == 1:
            url = input("URL: ").strip()
            if not validators.url(url) or ("youtube.com" not in url and "youtu.be" not in url):
                print(Fore.RED + f'erro: URL inválida! use um link do Youtube!'+ Style.RESET_ALL)
                continue
            destino = input('DESTINO: ').strip()
            os.makedirs(destino,exist_ok=True)
            interface(url)
            resp = confirmar("Quer baixar o arquivo? [S/N]: ")
            if resp == "S":
                resposta = baixar_audio(url, destino)
                if resposta["status"] == 'sucesso':
                    print(Fore.GREEN +f'o Arquivo foi baixado com sucesso! Caminho: {resposta["caminho"]}' + Style.RESET_ALL)
                else:
                    print(Fore.RED+ f'não foi possível baixar: {resposta["mensagem"]}')
            else:
                print("Download cancelado")
        elif opcao == 2:
            cabecalho(Fore.LIGHTYELLOW_EX + 'Saindo do programa . . .'+ Style.RESET_ALL)
            break
        else:
            print(Fore.RED + 'Opção inválida'+Style.RESET_ALL)

if __name__=='__main__':
    main()
