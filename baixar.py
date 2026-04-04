from pytubefix import YouTube

def baixar_audio(url,destino='.'):
    try:
        yt = YouTube(url)
        audio = yt.streams.get_audio_only()
        audio_final = audio.download(output_path=destino)
        return  audio_final
    except Exception as error:
        print(f"Erro {error}")

