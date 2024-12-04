import pygame

from src.classes import Vector2, SoundMixer, LogHandler


class SoundTrack:
	def __init__(self, position: Vector2,  sound_paths: list[str]):
		self.position = position
		self.sounds = {}
		for sound_name, sound_path in sound_paths.items():
			self.sounds[sound_name] = pygame.mixer.Sound(sound_path)

		self.is_music = None
		self.loop = None
		self.sound_object = None
		self.channel_object = None
		self.paused = None
		SoundMixer().add_sound_track(self)


	def init(self):
		self.sound_object = pygame.mixer.Sound(self.sound_path)
		self.channel_object = SoundMixer().find_channel()

	def play(self, sound_name: str, loop: bool = False, is_music: bool = False):
		self.loop = loop
		self.is_music = is_music
		if self.is_music:
			pygame.mixer.music.play(self.play_amount)
		else:
			if self.channel_object is None:
				self.init()
			self.channel_object.play(self.sound_object, self.play_amount)

		if is_music:
			pygame.mixer.music.load(sound_path)
		else:
			self.init()
		if loop:
			self.play_amount = -1  # -1 = jouer indéfiniment
		else:
			self.play_amount = 1

	def stop(self):
		if self.is_music:
			pygame.mixer.music.stop()
		else:
			if self.channel_object is not None and self.get_busy():

				self.channel_object.stop()

	def pause(self):
		self.paused = True
		if self.is_music:
			pygame.mixer.music.pause()
		else:
			self.stop()

	def unpause(self):
		self.paused = False
		if self.is_music:
			pygame.mixer.music.unpause()
		else:
			self.play()

	def set_volume(self, volume: float):
		if self.is_music:
			return pygame.mixer.music.set_volume(volume)
		return self.channel_object.set_volume(volume)

	def get_busy(self):
		if not self.is_music:
			return self.channel_object.get_busy()
		else:
			return True

	def release_channel(self):
		if not self.is_music:
			SoundMixer().release_channel(self.channel_object)
			del self.channel_object  # libérer une Channel

	def get_debug_string(self):
		if self.is_music:
			return None
		return f'Channel {SoundMixer().get_index_of_channel(self.channel_object)}: {id(self.sound_object)} ({self.sound_path.split("/")[-1]}) {"playing" if self.get_busy() else "idling"}'

	def remove(self):
		self.release_channel()
		SoundMixer().remove_sound_track(self)

	def distance_to(self, vector2: Vector2):
		if self.position is None:
			return 0
		return self.position.distance_to(vector2)

	def get_position(self):
		return self.position

	def get_loop(self):
		return self.loop

	def get_is_music(self):
		return self.is_music

	def get_paused(self):
		return self.paused
