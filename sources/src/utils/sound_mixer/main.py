#Projet : Bletchley's Adventure
#Auteurs : Diego GIMENEZ, Maël KEN, Alexis LAROSE, Dimitri NERRAND

import pygame

from src import DataHandler, LogHandler, Player, GameLoop


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
			pygame.mixer.set_num_channels(128)
			self.sound_tracks = []
			self.channels = []
			self.musics_historic = []
			self.music_coefficient = 0.25
			self.sound_coefficient = 1.0
			self.added_sfx = {}
			_, added_sfx_paths = DataHandler().get_sound_track_data('added_sfx')
			for name, path in added_sfx_paths.items():
				self.added_sfx[name] = pygame.mixer.Sound(path)
			self.sfx_channel = self.find_channel()

	def add_sound_track(self, sound_track):
		self.sound_tracks.append(sound_track)

	def remove_sound_track(self, sound_track):
		self.sound_tracks.remove(sound_track)

	def find_channel(self):
		# renvoyer une channel libérée
		channel = None
		for idx, c in enumerate(self.channels):
			if c is None:
				LogHandler().add(f'Assign channel {idx}')
				self.channels[idx] = pygame.mixer.Channel(idx)
				return self.channels[idx]

		LogHandler().add(f'Assign channel {len(self.channels)}')
		channel = pygame.mixer.Channel(len(self.channels))
		self.channels.append(channel)
		return channel

	def release_channel(self, channel):
		if pygame.mixer.get_init():
			channel.stop()
		self.channels = [c for c in self.channels if c == channel]

	def free_all_channels(self):
		[channel.stop() for channel in self.channels]
		self.channels = []

	def get_index_of_channel(self, channel):
		if channel in self.channels:
			return self.channels.index(channel)
		return -1

	def generate_debug_data(self):
		return ['==== Channels info ===='] + ([sound_track.get_debug_string() for sound_track in self.sound_tracks if sound_track.get_debug_string() is not None] if len(self.sound_tracks) > 0 else ['No channel'])

	def pause_music(self):
		pygame.mixer.music.pause()

	def unpause_music(self):
		if not pygame.mixer.music.get_busy():
			pygame.mixer.music.unpause()

	def get_musics_historic(self):
		return self.musics_historic

	def get_current_music(self):
		if len(self.musics_historic) == 0:
			return None
		return self.musics_historic[-1]

	def play_music(self, music_name):
		self.musics_historic.append(music_name)
		pygame.mixer.music.load(DataHandler().load_music(music_name)[1])
		pygame.mixer.music.set_volume(self.music_coefficient)
		pygame.mixer.music.play(-1)

	def play_music_prev(self):
		if len(self.musics_historic) >= 2:
			self.play_music(self.musics_historic[-2])

	def play_sfx(self, sfx_name, play_amount = 0):
		self.sfx_channel.set_volume(1)
		self.sfx_channel.play(self.added_sfx[sfx_name], play_amount)

	def set_music_coefficient(self, coefficient):
		self.music_coefficient = max(0.0, min(coefficient, 1.0))
		pygame.mixer.music.set_volume(self.music_coefficient)

	def set_sound_coefficient(self, coefficient):
		self.sound_coefficient = coefficient

	def update(self):
		if not pygame.mixer.get_init():
			pygame.mixer.init()
		player_position = Player().get_focus().get_position().copy()
		for sound_track in self.sound_tracks:
			if GameLoop().is_game_paused():
				sound_track.pause()
			elif sound_track.get_paused():
				sound_track.unpause()

			distance = sound_track.distance_to(player_position)
			if distance < 5:
				distance = 5
			volume = 1 / (4 * (distance * distance / 500))
			if volume > 1:
				volume = 1
			new_volume = volume * self.sound_coefficient * sound_track.get_sound_coef()
			sound_track.set_volume(new_volume)
