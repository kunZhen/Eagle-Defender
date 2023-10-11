import os
from pydub import AudioSegment
from pydub.playback import play

from pytube import YouTube
import pyglet
import youtube_dl


class musicLogic:
    def __init__(self):
        self.player = pyglet.media.Player()
        self.nameSongListForUser = []
        self.urlSongList = []

    def searchYoutubeSongs(self, query):
        ydl_opts = {
            'quiet': True,  # Evita que youtube-dl imprima mensajes en la consola
            'extract_flat': True,  # Extrae solo la información básica del video
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            search_results = ydl.extract_info(f"ytsearch3:{query}", download=False)

        self.nameSongListForUser = []  # Lista de nombres de canciones para el usuario
        self.urlSongList = []  # Lista de URL de videos
        seen_videos = set()  # Conjunto para evitar duplicados

        # Recorre los resultados y extrae información hasta obtener 2 resultados únicos
        for idx, video_info in enumerate(search_results.get('entries', []), start=1):
            video_url = video_info.get('url')
            video_title = video_info.get('title')

            if video_url and video_title and video_url not in seen_videos:
                print(f"{idx}. Título: {video_title}")
                print(f"   URL: {video_url}")

                self.nameSongListForUser.append(video_title)
                self.urlSongList.append(f"https://www.youtube.com/watch?v={video_url}")

                seen_videos.add(video_url)  # Agrega el URL al conjunto para evitar duplicados

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
