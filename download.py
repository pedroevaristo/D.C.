from pytube import YouTube as yt

opcoes = f"""
 itag=22 type=video/mp4 res=720p fps=30fps,
 itag=43 type=video/webm res=360p fps=30fps,
 itag=18 type=video/mp4 res=360p fps=30fps,
 itag=36 type=video/3gpp res=240p fps=30fps,
 itag=17 type=video/3gpp res=144p fps=30fps,
 itag=137 type=video/mp4 res=1080p fps=30fps,
 itag=136 type=video/mp4 res=720p fps=30fps,
 itag=135 type=video/mp4 res=480p fps=30fps,
 itag=134 type=video/mp4 res=360p fps=30fps,
 itag=133 type=video/mp4 res=240p fps=30fps,
 itag=160 type=video/mp4 res=144p fps=30fps,
"""

def download_link(pego_link):
    resolucao = input(f"Qual resolução quer usar? Entre as opções{opcoes}")
    for linha in opcoes.splitlines():
        #problemas em ler a string e fazer a busca pelo itag
        #link para poder buscar o tipo de qualidade: https://www.youtube.com/watch?v=Uf4rxCB4lys&pp=ygUOam9obnkgYmUgZ29vZGU%3D
        if linha.match(resolucao): 
            #fazer a busca dentro da string e ver se dá match com o valor digitado junto com itag
            print("Entrou")
            try:
                
                #comentario
                (
                    """Fazer alguma coisa que pega o itag e puxa da api do pytube
                    e baixe as configurações estabelecidas
                    """
                )
            
                print("Downloading")
            except Exception as e:
                print("erro ao baixar o vídeo")
                #comentário
                (
                    """toda vez que digito algo mas parece queue é por padrão 1
                        Qual resolução quer usar? 137
                        22"""
                )
            #finally:

        else:
            print("não apareceu a opção")

        
