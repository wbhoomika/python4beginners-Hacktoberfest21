from pytube import YouTube

def run(Videos):
    for vidLink in Videos:
        try:
            youtube = YouTube(vidLink)  # Searches for the video
            print("Downloading \"" + youtube.streams[0].title + "\"")
        except:
            print("\""+vidLink + "\" returned a connection issue")
        vidStream = youtube.streams.filter(res="720p").first()   # Gets the video
        vidStream.download("Videos/")  # Downloads the video to Downloads folder
    print("Completed!")


if __name__ == "__main__":
    print("YouTube video downloader - To stop entering URLs, Just click Enter on an empty line. ")
    Videos = []
    link = input("YouTube Video Link: ")  # Gets the amount of Dice
    while not link.__eq__(""):
        Videos.append(link)
        link = input("YouTube Video Link: ")
    run(Videos)
