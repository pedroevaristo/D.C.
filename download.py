from pytube import YouTube as yt
print ("Downloading")
def download_link(pego_link):
    
    resolucao = input("Qual resolução quer usar? ")
    try:
        highest_resolution_stream = pego_link.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
        print(highest_resolution_stream.itag)
    except Exception as e:
        print("erro ao baixar o vídeo")