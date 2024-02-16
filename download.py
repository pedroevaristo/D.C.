from pytube import YouTube as yt

opcoes = """
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
 itag=140 type=audio/mp4 abr=128kbps 
 itag=171 type=audio/webm abr=128kbps

"""

def download_link(pego_link):
    resolucao = input("Qual resolução quer usar? Entre as opções{opcoes}")
    for linha in opcoes.splitlines():
        if linha.startswith(f"itag={resolucao}"):
            try:
                
            
                print("Downloading")
            except Exception as e:
                print("erro ao baixar o vídeo")

                (
                    """toda vez que digito algo mas parece queue é por padrão 1
                        Qual resolução quer usar? 137
                        22"""
                )
        else:
            print("não apareceu a opção")
        
