from src.classes import SoundTrack


class SoundMaker:
    def __init__(self, position):
        self.position = position  # défini dans les classes enfant
        self.sound_tracks = {}

    def load_sound(self, sound_path: str, loop: bool = False, is_music: bool = False):
        if self.position is None:
            raise AttributeError
        self.sound_tracks[sound_path] = SoundTrack(sound_path, self.position, loop, is_music)

    def play_sound(self, sound_path: str):
        self.sound_tracks[sound_path].play()

    def stop_sound(self, sound_path: str):
        if self.sound_tracks[sound_path].get_busy():
            print("BUSY")
            self.sound_tracks[sound_path].stop()

    def pause(self, sound_path: str):
        self.sound_tracks[sound_path].pause()

    def unpause(self, sound_path: str):
        self.sound_tracks[sound_path].unpause()

    def get_busy(self, sound_path: str):
        return self.sound_tracks[sound_path].get_busy()

    def is_sound_loaded(self, sound_path: str):
        return sound_path in self.sound_tracks