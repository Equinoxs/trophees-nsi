from src.classes import SoundTrack, DataHandler


class SoundMaker:
	def __init__(self, position, authorized_sound_tracks):
		self.position = position  # défini dans les classes enfant
		self.sound_tracks = {}
		for sound_track_name in authorized_sound_tracks:
			self.sound_tracks[sound_track_name] = SoundTrack(position, DataHandler().get_sound_track_data(sound_track_name)[1])

	def load_sound(self, sound_type: str, sound_name: str, loop: bool = False, is_music: bool = False, needs_playing: bool = False, default_volume: float = 1):
		_, sound_path = DataHandler().load_sound(sound_type, sound_name)
		self.sound_tracks[sound_type] = SoundTrack(sound_path, self.position, loop, is_music)
		if needs_playing:
			self.sound_tracks[sound_type].play()
		if default_volume != 1:
			self.sound_tracks[sound_type].set_volume(default_volume)

	def play_sound(self, sound_name: str = None):
		if sound_name is None:
			raise AttributeError
		for name, sound_track in self.sound_tracks.items():
			if sound_track.contains(sound_name):
				self.sound_tracks[name].play(sound_name)

	def stop_sound(self, sound_type: str):
		if sound_type in self.sound_tracks and self.sound_tracks[sound_type].get_busy():
			self.sound_tracks[sound_type].stop()

	def pause(self, sound_type: str):
		self.sound_tracks[sound_type].pause()

	def unpause(self, sound_type: str):
		self.sound_tracks[sound_type].unpause()

	def get_busy(self, sound_type: str):
		if sound_type in self.sound_tracks:
			return self.sound_tracks[sound_type].get_busy()
		return False

	def is_sound_loaded(self, sound_type: str):
		return sound_type in self.sound_tracks

	def remove_sound(self, sound_type: str):
		if sound_type in self.sound_tracks:
			self.sound_tracks[sound_type].remove()
			del self.sound_tracks[sound_type]
		
	def change_sound(self, sound_type: str, sound_name: str, needs_playing: bool = None):
		if sound_type in self.sound_tracks:
			loop, is_music, busy = self.sound_tracks[sound_type].get_loop(), self.sound_tracks[sound_type].get_is_music(), self.sound_tracks[sound_type].get_busy()
			self.stop_sound(sound_type)
			self.remove_sound(sound_type)
			return self.load_sound(sound_type, sound_name, loop, is_music, busy if needs_playing is None else needs_playing)
		return self.load_sound(sound_type, sound_name, needs_playing=needs_playing)


		