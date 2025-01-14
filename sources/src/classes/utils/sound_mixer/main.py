from math import pi
from pygame import mixer


from src.classes import DataHandler, LogHandler, Player, GameLoop


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
			mixer.set_num_channels(16)
			self.sound_tracks = []
			self.channels = []
			self.musics_historic = []
			self.added_sfx = {}
			added_sfx_paths = DataHandler().get_sound_track_data('added_sfx')[1]
			for name, path in added_sfx_paths.items():
				self.added_sfx[name] = mixer.Sound(path)
			self.sfx_channel = self.find_channel()

	def add_sound_track(self, sound_track):
		self.sound_tracks.append(sound_track)

	def remove_sound_track(self, sound_track):
		self.sound_tracks.remove(sound_track)

	def update(self):
		player_position = Player().get_focus().get_position()
		for sound_track in self.sound_tracks:
			if GameLoop().is_game_paused():
				sound_track.pause()
			elif sound_track.get_paused():
				sound_track.unpause()
			if sound_track.get_position() == player_position or sound_track.distance_to(player_position) == 0:
				continue
			sound_track.set_volume(1/(4*pi*((sound_track.distance_to(player_position)/500)**2)))  # à vérifier...

	def find_channel(self):
		# renvoyer une channel libérée
		channel = None
		for idx, c in enumerate(self.channels):
			if c is None:
				LogHandler().add(f'Assign channel {idx}')
				self.channels[idx] = mixer.Channel(idx)
				return self.channels[idx]

		LogHandler().add(f'Assign channel {len(self.channels)}')
		channel = mixer.Channel(len(self.channels))
		self.channels.append(channel)
		return channel

	def release_channel(self, channel):
		self.channels = [c if c is not channel else None for c in self.channels]

	def get_index_of_channel(self, channel):
		return self.channels.index(channel)

	def generate_debug_data(self):
		return ['==== Channels info ===='] + ([sound_track.get_debug_string() for sound_track in self.sound_tracks if sound_track.get_debug_string() is not None] if len(self.sound_tracks) > 0 else ['No channel'])

	def pause_music(self):
		mixer.music.pause()

	def unpause_music(self):
		if not mixer.music.get_busy():
			mixer.music.unpause()

	def play_music(self, music_name):
		self.musics_historic.append(music_name)
		mixer.music.load(DataHandler().load_music(music_name)[1])
		mixer.music.set_volume(0.25)
		mixer.music.play()

	def play_music_prev(self):
		if len(self.musics_historic) >= 2:
			self.play_music(self.musics_historic[-2])

	def play_sfx(self, sfx_name, play_amount = 0):
		self.sfx_channel.play(self.added_sfx[sfx_name], play_amount)
