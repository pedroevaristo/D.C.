from pytube import YouTube as ytp

opcoes = f"""
 itag=22 type=video/mp4 res=720p fps=30fps 
 itag=43 type=video/webm res=360p fps=30fps 
 itag=18 type=video/mp4 res=360p fps=30fps 
 itag=36 type=video/3gpp res=240p fps=30fps 
 itag=17 type=video/3gpp res=144p fps=30fps 
 itag=137 type=video/mp4 res=1080p fps=30fps 
 itag=136 type=video/mp4 res=720p fps=30fps 
 itag=135 type=video/mp4 res=480p fps=30fps 
 itag=134 type=video/mp4 res=360p fps=30fps 
 itag=133 type=video/mp4 res=240p fps=30fps 
 itag=160 type=video/mp4 res=144p fps=30fps 
"""

def download_link(pego_link):
    global opcoes
    opcoes_dic = {}
    for linha in opcoes.splitlines():
        itag, type, res, fps = linha.split(" ")#tendo problemas em pegar as informações mas só pega uma possívemente o itag

        opcoes_dic[itag] = {
            "type": type,
            "res": res,
            "fps": fps
        }
        for itag, opcoes in opcoes_dic.items():
            print(f"{itag} - {opcoes[res]} - {opcoes[type]}")
        
        escolha_itag = input("Digite o itag:")

        #problemas em ler a string e fazer a busca pelo itag
        #link para poder buscar o tipo de qualidade: 
        
            #fazer a busca dentro da string e ver se dá match com o valor digitado junto com itag
          #comentario
        """Fazer alguma coisa que pega o itag e puxa da api do pytube
                    e baixe as configurações estabelecidas
                    """
        try:
            url_video = ytp.streams.get_by_itag(escolha_itag)

            video = ytp.download_video(url_video)
            
            print(f"baixado com sucesso: {video}")
        except Exception as e:
            print(f"erro ao baixar o vídeo {e}")
                #comentário
            (
              """toda vez que digito algo mas parece queue é por padrão 1
                  Qual resolução quer usar? 137
                   22"""
            )
            #finally:

        else:
            print("não apareceu a opção")

        
