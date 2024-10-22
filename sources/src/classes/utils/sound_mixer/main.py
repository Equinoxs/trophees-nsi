from ...basics import Vector2
from math import pi


class SoundMixer(object):
    _instance = None

    # singleton
    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.sound_tracks = []

    def add_sound_track(self, sound_track):
        self.sound_tracks.append(sound_track)
        # à implémenter une fois Player écrit : update_volumes

    def remove_sound_track(self, sound_track):
        self.sound_tracks.remove(sound_track)

    def update_volumes(self, player_position: Vector2):
        for sound_track in self.sound_tracks:
            # à implémenter une fois le jeu un peu plus avancé
            """if not sound_track.get_busy():
                sound_track.release_channel()
            else:"""
            sound_track.set_volume(1/(4*pi*(sound_track.distance_to(player_position)**2)))  # à vérifier...
