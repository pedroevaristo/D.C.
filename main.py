import pytube
import convert
from download import download_link
#https://www.youtube.com/watch?v=SrnWp5O0DEs&pp=ygUMbm8gbW9yZSBqYWNr

def consulta(link):
    pego_link = pytube.YouTube(link)

    if link and "youtube.com" in link:
        
        opcao = input(f"\n-----------------------\nTitulo:  {pego_link.title} Duração :  {round(pego_link.length / 60)}\n\n---------escolha entre as opções--------\n 1- Baixar vídeo \n 2- Converter vídeo para música \n--------------\n")
            
        match opcao:
            case 1:
                download_link(pego_link)
            #case 2:

    else:
        print("Esse link não direciona ao youtube")

if __name__ == "__main__":
    link = input("Copie e cole a URL da música aqui:")
    consulta(link)