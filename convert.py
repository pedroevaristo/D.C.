from pytube import YouTube as yt


opcoes =["itag=140 mime_type=audio/mp4 abr=128kbps acodec=mp4a.40.2 progressive=False type=audio",
 "itag=249 mime_type=audio/webm abr=50kbps acodec=opus progressive=False type=audio",
 "itag=250 mime_type=audio/webm abr=70kbps acodec=opus progressive=False type=audio",
 "itag=251 mime_type=audio/webm abr=160kbps acodec=opus progressive=False type=audio"]

def convert_link(link, diretorio):
    url_obtido = yt(link)
    
    escolha_itag = input(f"Escolha entre as opcoes:\n{opcoes}")
    #está saindo com tudo dentro do opcoes
    try:
      stream = url_obtido.streams.get_by_itag(escolha_itag)
      audio = stream.download(output_path=diretorio)
        if audio
    except Exception as e:
       print(f"Erro ao baixar o conteúdo em aúdio. {e}")
    
    



(  """
  itag=140 type=audio/mp4 abr=128kbps 
 itag=171 type=audio/webm abr=128kbps 

 para converter e baixar nessa qualidade de audio
 """ 
)
