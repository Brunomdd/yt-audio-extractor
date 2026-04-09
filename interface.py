
from uteis import linha
def interface(yt):
    
        print(linha())
        print(f"Nome: {yt.title}")
        minutos = yt.length // 60
        segundos = yt.length % 60
        print(f"Quantidade de likes: {yt.likes}")
        print(f"f Duração: {minutos} e {segundos}")
        print(linha())







