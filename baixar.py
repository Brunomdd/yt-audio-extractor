from  pytubefix import YouTube
from pytubefix.exceptions import VideoRemovedByYouTubeForViolatingTOS, VideoUnavailable

def baixar_audio(yt,destino='.'):
    try:
        audio = yt.streams.get_audio_only()
        audio_final = audio.download(output_path=destino)
        return {"status":"sucesso","caminho":audio_final}


    except VideoRemovedByYouTubeForViolatingTOS:
        return {"status":"erro","mensagem":"o áudio foi removido do youtube por violar os direitos autorais"}
    except VideoUnavailable:
        return {"status":"erro","mensagem":"o áudio esta indisponível"}
    except Exception as error:
        return {"status":"erro","mensagem":f"Erro ao baixar o áudio {error}"}



