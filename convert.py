from pytube import YouTube as yt


opcoes =["itag=140 mime_type=audio/mp4 abr=128kbps type=audio",
 "itag=249 mime_type=audio/webm abr=50kbps type=audio",
 "itag=250 mime_type=audio/webm abr=70kbps type=audio",
 "itag=251 mime_type=audio/webm abr=160kbps type=audio"]

def convert_link(link, diretorio):
    url_obtido = yt(link)
    global opcoes
    opcoes_dic = {}

    for linha in opcoes:
      itag, mime_type, abr, type = linha.split(" ")

      opcoes_dic[itag] = {
        "mime_type":mime_type,
        "abr": abr,
        "type":type
      }
    for itag, opcoes in opcoes_dic.items():#itag representa a chave do dic, enquanto opcoes os valores das chaves
      mime_type = opcoes["mime_type"]
      type = opcoes["type"]
      abr = opcoes["abr"]

      print(f"{itag} : : {mime_type} : {type} : {abr}\n")
  
    escolha_itag = input("escolha o itag, acima: ")
    try:
      stream = url_obtido.streams.get_by_itag(escolha_itag)

      audio = stream.download(output_path=diretorio)

      if not audio == "":
        print(f"Baixado o audio:\n\n {audio}")
         
    except Exception as e:
       print(f"Erro ao baixar o conteúdo em aúdio. {e}")
  