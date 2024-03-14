import youtube_dl as yt
from pytube

opcoes = ["itag=22 type=video/mp4 res=720p fps=30fps",
"itag=43 type=video/webm res=360p fps=30fps", 
"itag=18 type=video/mp4 res=360p fps=30fps", 
"iitag=36 type=video/3gpp res=240p fps=30fps", 
"iitag=17 type=video/3gpp res=144p fps=30fps", 
"itag=137 type=video/mp4 res=1080p fps=30fps", 
"itag=136 type=video/mp4 res=720p fps=30fps",
"itag=135 type=video/mp4 res=480p fps=30fps", 
"itag=134 type=video/mp4 res=360p fps=30fps", 
"itag=133 type=video/mp4 res=240p fps=30fps", 
"itag=160 type=video/mp4 res=144p fps=30fps"]

def download_link(pego_link):
    global opcoes
    opcoes_dic = {}
    for linha in opcoes:
        #tendo problemas em pegar as informações mas só pega uma possívemente o itag
        itag, type, res, fps = linha.split(" ")

        opcoes_dic[itag] = {
            "type": type,
            "res": res,
            "fps": fps
        }
        
    for itag, opcoes in opcoes_dic.items():
        print(f"{itag} - {res} - {type}")
        
    escolha_itag = input("Digite o itag:")

    try:
        url_video = yt.(escolha_itag)#problema em pegar o itag não se se sabe se é devido a versão do python ou da api ou outro motivo

        video = yt.download_video(url_video)
            
        print(f"baixado com sucesso: {video}")
    except Exception as e:
        print(f"erro ao baixar o vídeo {e}")
                
            #finally:

   # print("não apareceu a opção")

        
