import pygame

from ...basics import Vector2


class SoundTrack:
    def __init__(self, sound_path: str,  position: Vector2, loop: bool = False, is_music: bool = False):
        self.position = position
        self.is_music = is_music
        self.loop = loop
        self.sound_path = sound_path
        self.sound_object = None
        self.channel_object = None
        if is_music:
            pygame.mixer.music.load(sound_path)
        else:
            self.init()

        if loop:
            self.play_amount = -1  # -1 = jouer indéfiniment
        else:
            self.play_amount = 1

    def init(self):
        self.sound_object = pygame.mixer.Sound(self.sound_path)
        self.channel_object = pygame.mixer.find_channel()

    def play(self):
        if self.is_music:
            pygame.mixer.music.play(self.play_amount)
        else:
            if self.channel_object is None:
                self.init()
            self.channel_object.play(self.sound_object, self.play_amount)

    def stop(self):
        if self.is_music:
            pygame.mixer.music.stop()
        else:
            if self.channel_object is not None:
                self.channel_object.stop()

    def pause(self):
        if self.is_music:
            pygame.mixer.music.pause()
        else:
            self.stop()

    def unpause(self):
        if self.is_music:
            pygame.mixer.music.unpause()
        else:
            self.play()

    def set_volume(self, volume: float):
        if self.is_music:
            pygame.mixer.music.set_volume(volume)
        self.channel_object.set_volume(volume)

    def get_busy(self):
        if not self.is_music:
            return self.channel_object.get_busy()
        else:
            return True

    def release_channel(self):
        if not self.is_music:
            del self.channel_object  # libérer une Channel