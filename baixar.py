from pytubefix import YouTube
from pytubefix.exceptions import VideoRemovedByYouTubeForViolatingTOS, VideoUnavailable

def baixar_audio(url,destino='.'):
    try:
        yt = YouTube(url)
        audio = yt.streams.get_audio_only()
        audio_final = audio.download(output_path=destino)
        return  audio_final

    except VideoRemovedByYouTubeForViolatingTOS:
        return "Video foi removido do youtube por violar os direitos autorais"
    except VideoUnavailable:
        return "O video está indisponivel!"
    except Exception as error:
        return f"Erro ao baixar o áudio {error}"



