#https://github.com/deepankarvarma/MP4-to-MP3-converter-using-Python/blob/master/app.py
#https://dev.to/stokry/download-youtube-video-to-mp3-with-python-26p

#https://www.youtube.com/watch?v=SrnWp5O0DEs&pp=ygUMbm8gbW9yZSBqYWNr
import pytube
from moviepy.editor import VideoFileClip
import sys

def case1(linkYT):
    
    try:
        print("Convertendo...")
        converter_Audio = VideoFileClip(linkYT)# resolver o problema aqui e colocar direcionamento para a pasta que eu quero que baixe
        converter_Audio.audio.write_audiofile()
        print("\nBaixado!")

    except:
        print("error ao baixar...")
        sys.exit()
#def case2(linkYT):


def opcoesDeconversao(case, linkYT):
    
    match case:
        case 1:
            case1(linkYT)
        #case 2:
        case _:
            print("Inválido")
    
    


urlYT = input("Copie e cole a URL da música aqui:")

if urlYT and "youtube.com" in urlYT:
    try:
        linkYT = pytube.YouTube(urlYT)
        print("\n----------------------------")
        print("\ntitulo: ", linkYT.title, "\n\nduração: ", linkYT.length, " segundos")#fazer o calculo de conversão para minutos ou horas
        print("\n------Quer converter para: ------------------")

        case = int(input("Entre as opções: \n1- Converter para MP3 | \n2- Fazer download do vídeo |\n"))
        
        opcoesDeconversao(case, linkYT)
        
    except:
            print("Download Failed!")


    else:
        print("Não foi passado nada para o Sistema. Tente novamente...")

