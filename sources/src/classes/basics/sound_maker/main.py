from src.classes import SoundTrack, DataHandler


class SoundMaker:
	def __init__(self, position = None, authorized_sound_tracks = []):
		self.position = position  # défini dans les classes enfant
		self.all_sound_tracks = {}
		self.sound_tracks = {}
		for sound_track_name in authorized_sound_tracks:
			self.sound_tracks[sound_track_name] = SoundTrack(position, DataHandler().get_sound_track_data(sound_track_name)[1])

	def play_sound(self, sound_name: str = None):
		if sound_name is None:
			raise AttributeError
		for name, sound_track in self.sound_tracks.items():
			if sound_track.contains(sound_name):
				self.sound_tracks[name].play(sound_name)
				return
		for name, sound_track in self.all_sound_tracks.items():
			if sound_track.contains(sound_name):
				sound_track.play(sound_name)
				return

	def stop_sound_track(self, sound_track_name: str):
		if sound_track_name in self.sound_tracks and self.sound_tracks[sound_track_name].get_busy():
			self.sound_tracks[sound_track_name].stop()

	def stop_sound(self, sound_name: str):
		for name, sound_track in self.sound_tracks.items():
			if sound_track.contains(sound_name):
				self.sound_tracks[name].stop()

	def remove_sound_track(self, sound_track_name: str):
		if sound_track_name in self.sound_tracks:
			self.sound_tracks[sound_track_name].remove()
			del self.sound_tracks[sound_track_name]

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

	def gimme_all_sound_tracks(self):
		data = DataHandler().get_all_sound_tracks_data()
		for name, sounds in data.items():
			self.all_sound_tracks[name] = SoundTrack(self.position, sounds)

	def dont_gimme_all_sound_tracks(self):
		for sound_track in self.all_sound_tracks:
			self.all_sound_tracks[sound_track].stop()
			self.all_sound_tracks[sound_track].release_channel()
			del self.all_sound_tracks[sound_track]
