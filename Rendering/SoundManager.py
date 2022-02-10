import pygame

class Sound:
    def __init__(self, song):
        self.songLoaded = pygame.mixer.music.load(song)
        pygame.mixer.music.set_volume(0.1)
    
    def replace(self, newSong):
        self.mixer.music.load(newSong)
    
    def play(self, is_looping):
        if is_looping == True:
            self.mixer.music.play(-1, 0.0)
        self.mixer.music.play(0, 0.0)
    
    def pause(self):
        self.mixer.music.pause()

    def unpause(self):
        self.mixer.music.unpause()
    
    def volume(self, vol):
        self.mixer.music.set_volume(vol)
    
    def get_volume(self):
        return self.mixer.music.get_volume()
    