from uteis import leiaint
from pytubefix import YouTube

def baixar_audio(url):
    try:
        yt = YouTube(url)
        audio = yt.streams.get_audio_only()
        audio_final = audio.download()
        return  audio_final
    except Exception as error:
        print(f"Erro {error}")

def main():
    while True:
        print('1 - Converter')
        print('2 - Sair')
        opcao = leiaint('escolha uma opção: ')
        if opcao == 1:
            url = input('URL: ').strip()
            arquivo = baixar_audio(url)
            print(arquivo)
        elif opcao == 2:
            print("Saindo . . . ")
            break
        else:
            print('Opção inválida')

main()
