from math import pi
from pygame import mixer
from src.classes import Vector2, LogHandler, Player, TimeHandler


class SoundMixer(object):
	_instance = None

	# singleton
	def __new__(cls, *args, **kwargs):
		if not isinstance(cls._instance, cls):
			cls._instance = object.__new__(cls, *args, **kwargs)
		return cls._instance

	def __init__(self):
		if not hasattr(self, "_initialized"):
			self._initialized = True
			mixer.init()
			self.sound_tracks = []
			self.channels = []

	def add_sound_track(self, sound_track):
		self.sound_tracks.append(sound_track)

	def remove_sound_track(self, sound_track):
		self.sound_tracks.remove(sound_track)

	def update(self):
		player_position = Player().get_focus().get_position()
		for sound_track in self.sound_tracks:
			if not TimeHandler().is_running():
				sound_track.pause()
			elif sound_track.get_paused():
				sound_track.unpause()
			if sound_track.get_position() == player_position or sound_track.distance_to(player_position) is 0: continue
			sound_track.set_volume(1/(4*pi*((sound_track.distance_to(player_position)/500)**2)))  # à vérifier...

	def find_channel(self):
		# renvoyer une channel libérée
		channel = None
		for idx, c in enumerate(self.channels):
			if c is None:
				LogHandler().add(f'Assigning channel {idx}')
				self.channels[idx] = mixer.Channel(idx)
				return self.channels[idx]

		LogHandler().add(f'Assigning channel {len(self.channels)}')
		channel = mixer.Channel(len(self.channels))
		self.channels.append(channel)
		return channel

	def release_channel(self, channel):
		self.channels = [c if c is not channel else None for c in self.channels]

	def get_index_of_channel(self, channel):
		return self.channels.index(channel)

	def generate_debug_data(self):
		return ['==== Channels info ===='] + ([sound_track.get_debug_string() for sound_track in self.sound_tracks if sound_track.get_debug_string() is not None] if len(self.sound_tracks) > 0 else ['No channel'])