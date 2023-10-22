import pygame
from moviepy.editor import AudioFileClip

class MusicControl: 
    def __init__(self):
        self.musicPath = None

    def setUpMusic(self, musicPath):
        pygame.mixer.init()
        self.musicPath = musicPath
        pygame.mixer.music.load(self.musicPath)
        pygame.mixer.music.set_endevent(pygame.USEREVENT + 1)
        pygame.mixer.music.play(loops=-1)  # Establece loops=-1 para que se reproduzca en bucle

    def stopMusic(self):
        pygame.mixer.music.stop()

    def pauseMusic(self):
        pygame.mixer.music.pause()
    
    def setUpVideoMusic(self, videoPath):
        try: 
            audio = AudioFileClip(videoPath)
            audio.write_audiofile(videoPath.replace(".mp4", ".mp3"))
            self.setUpMusic(videoPath.replace(".mp4", ".mp3"))
        except Exception as e:
            print(f"Error: {e}")

    
