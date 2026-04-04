from pytubefix import YouTube

def baixar_audio(url,destino='.'):
    try:
        yt = YouTube(url)
        print(f"Título: {yt.title}")
        print(f"Quantidade de views {yt.views}")
        print(f"Quantidade de likes: {yt.likes}")
        print(f"Autor: {yt.author}")
        audio = yt.streams.get_audio_only()
        audio_final = audio.download(output_path=destino)
        return  audio_final
    except Exception as error:
        print(f"Erro ao baixar o áudio {error}")
        

