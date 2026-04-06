from pytubefix import YouTube
from uteis import linha
from colorama import init,Fore,Style

def interface(url):
        init()
        yt = YouTube(url)
        print(linha())
        print(f"Nome: {yt.title}")
        print(f"Quantidade de likes: {yt.likes}")
        print(f"f Duração: {yt.length/60}")
        print(linha())




