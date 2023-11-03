import pygame
from pytube import YouTube
import youtube_dl 
from moviepy.editor import AudioFileClip
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import librosa

import time
import threading

class musicLogic:
    def __init__(self): 
        """Creates an instance of a musicLogic controller"""
        self.nameSongListForUser=[]
        self.urlSongList=[]
        self.fileName=""

        # >>> Spotify module initiation <<<
        self.credentials = SpotifyClientCredentials(client_id="455c4c1a988c4de28aec7afbe6b25798", client_secret="1e2791559d1d4adea1e13f67328958d8")
        self.spotify = spotipy.Spotify(client_credentials_manager=self.credentials)

    def searchSong(self, query):
        """
        This method looks for a song both in Spotify and the on Youtube

        Parameters
            - query(str): name of the song requested
        """
        # >>> Look for the song on Spotify and set a name <<<
        results = self.spotify.search(q=f"track:{query}", type='track') #-> Looks for a spotify track similar to the request
        track = results['tracks']['items'][0]
        songname = track['name']

        # >>> Look for the songname found from Spotify on Youtube <<<
        ydl_opts = {
        'quiet': True,        # Evita que youtube-dl imprima mensajes en la consola
        'extract_flat': True,  # Extrae solo la información básica del video
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            search_results = ydl.extract_info(f"ytsearch3:{songname}", download=False)

        self.nameSongListForUser = []  # Lista de nombres de canciones para el usuario
        self.urlSongList = []          # Lista de URL de videos
        seen_videos = set()            # Conjunto para evitar duplicados

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

    def getName(self,videoUrl):
        yt = YouTube(videoUrl)
        audioStream = yt.streams.filter(only_audio=True).first()
        return audioStream.default_filename
    
    def downloadSongs(self, url:str, username:str):
        """
        Downloads a youtube song from a given URL and names it after an username

        Parameters:
            -url(str): link to youtube video
            -username(str): name of the user that will user to name the file
        """
        thread = threading.Thread(target=self.aux_download(url, username), daemon=True)
        thread.start()

    def aux_download(self, url:str, username:str):
        yt = YouTube(url)
        audioStream = yt.streams.filter(only_audio=True).first()

        # Limpia el título para que sea válido como nombre de archivo
        outputFolder = "Code/GraphicalUserInterface/songs"

        # Crea la carpeta "canciones" si no existe
        audioStream.download(outputFolder, filename=username)
        self.setUpVideoMusic(f'{outputFolder}/{username}')
    
    def downloadYoutubeAudio(self,videoUrl):
        yt = YouTube(videoUrl)
        audioStream = yt.streams.filter(only_audio=True).first()

        # Limpia el título para que sea válido como nombre de archivo
        outputFolder = "Code/GraphicalUserInterface/songs"
    

        # Crea la carpeta "canciones" si no existe
        audioStream.download(outputFolder, filename=self.fileName)

    def duration(self, video_url):
        try:
            yt = YouTube(video_url)
            duracion = yt.length
            return duracion
        except Exception as e:
            print(f"Error al obtener la duración del video: {str(e)}")
            return None

    def setUpMusic(self, musicPath):
        pygame.mixer.init()
        self.musicPath = musicPath
        pygame.mixer.music.load(self.musicPath)
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.set_endevent(pygame.USEREVENT + 1)
        pygame.mixer.music.play(loops=-1)  # Establece loops=-1 para que se reproduzca en bucle

    def stopMusic(self):
        pygame.mixer.music.stop()
    def pauseMusic(self):
        pygame.mixer.music.pause()
    def unpauseMusic(self): 
        pygame.mixer.music.unpause()
    
    @classmethod
    def playSFX(cls, name:str):
        pygame.mixer.init()
        soundpath = "Code/GraphicalUserInterface/sfx/"+name+".wav"
        sound_effect = pygame.mixer.Sound(soundpath)
        sound_effect.set_volume(0.9)
        sound_effect.play()
    
    def setUpVideoMusic(self, videoPath):
        try: 
            audio = AudioFileClip(videoPath)
            audio.write_audiofile(videoPath.replace(".mp4", ".mp3"))
        except Exception as e:
            print(f"Error: {e}")
