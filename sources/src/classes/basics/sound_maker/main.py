from ...utils import SoundTrack


class SoundMaker:
    def __init__(self, position):
        self.position = position  # défini dans les classes enfant
        self.sound_track = None

    def load_sound(self, sound_path: str, loop: bool = False, is_music: bool = False):
        if self.position is None:
            raise AttributeError
        self.sound_track = SoundTrack(sound_path, self.position, loop, is_music)

    def play_sound(self):
        self.sound_track.play()

    def stop_sound(self):
        self.sound_track.stop()

    def pause(self):
        self.sound_track.pause()

    def unpause(self):
        self.sound_track.pause()
