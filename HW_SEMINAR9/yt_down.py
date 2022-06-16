from pytube import YouTube

def yt_down(adres, path):
    yt = YouTube(adres)
    yt.streams.filter(progressive=True, file_extension='mp4')
    yt.streams.order_by('resolution')
    yt.streams.desc()
    yt.streams.first().download(path)