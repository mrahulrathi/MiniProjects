from pytube import YouTube

def DownloadYT(url):
    youtubeObject = YouTube(url)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
        print("Title:", youtubeObject.title)
        print("Download is successfull")
    except:
        print("An error occured")

url = input("Enter the Youtube url: ")
DownloadYT(url)


