import os
from pydub import AudioSegment
from pydub.playback import play
from youtubesearchpython import VideosSearch
from pytube import YouTube
import pyglet


class musicLogic:
    def __init__(self):
        self.player = pyglet.media.Player()
        self.nameSongListForUser = []
        self.nameSongListForDev = []
        self.urlSongList = []

    def searchYoutubeSongs(self, query):
        videosSearch = VideosSearch(query, limit=2)  # Limita la búsqueda a 5 resultados (ajusta según sea necesario)
        results = videosSearch.result()
        self.nameSongListForUser = []
        self.nameSongListForDev = []
        self.urlSongList = []

        # Imprimir la lista de URLs de los videos y sus títulos
        for idx, video in enumerate(results['result'], start=1):
            videoUrl = "https://www.youtube.com/watch?v=" + video['id']
            videoTitle = video['title']
            print(f"{idx}. Título: {videoTitle}")
            print(f"   URL: {videoUrl}")
            self.nameSongListForDev.append(self.getName(videoUrl))
            self.nameSongListForUser.append(videoTitle)
            self.urlSongList.append(videoUrl)

    def getName(self, videoUrl):
        yt = YouTube(videoUrl)
        audioStream = yt.streams.filter(only_audio=True).first()
        return audioStream.default_filename

    def downloadYoutubeAudio(self, videoUrl):
        yt = YouTube(videoUrl)
        audioStream = yt.streams.filter(only_audio=True).first()

        # Limpia el título para que sea válido como nombre de archi
        outputFolder = "canciones"

        # Crea la carpeta "canciones" si no existe
        audioStream.download(outputFolder)

    def playAudio(self, videoFilePath):
        try:
            source = pyglet.media.load(videoFilePath)
            self.player.queue(source)
            self.player.play()
            pyglet.app.run()
        except Exception as e:
            print("Error:", str(e))

    def stop(self):
        self.player.pause()
        pyglet.app.exit()
