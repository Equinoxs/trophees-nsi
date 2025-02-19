import pygame

from src.classes import Vector2, SoundMixer

class SoundTrack:
	def __init__(self, position: Vector2, sound_paths: list[str]):
		self.sounds = {}
		self.current_sound_name = None
		for sound_name, sound_path in sound_paths.items():
			self.sounds[sound_name] = pygame.mixer.Sound(sound_path)
		self.position = position
		self.channel = SoundMixer().find_channel()
		self.paused = None
		self.play_amount = None
		SoundMixer().add_sound_track(self)

	def contains(self, sound_name: str):
		return sound_name in set(self.sounds)

	def play(self, sound_name: str, loop: bool = False):
		self.current_sound_name = sound_name
		if loop:
			self.play_amount = -1
		else:
			self.play_amount = 0
		if self.channel is None:
			self.channel = SoundMixer().find_channel()
		self.channel.play(self.sounds[sound_name], self.play_amount)

	def stop(self):
		if self.channel is not None and self.get_busy():
			self.channel.stop()

	def pause(self):
		self.paused = True
		if self.channel is not None and self.get_busy():
			self.channel.pause()

	def unpause(self):
		self.paused = False
		if self.channel is not None and self.get_busy():
			self.channel.unpause()

	def set_volume(self, volume: float):
		return self.channel.set_volume(volume)

	def get_busy(self):
		return self.channel.get_busy()

	def release_channel(self):
		SoundMixer().release_channel(self.channel)
		del self.channel  # libérer une Channel

	def get_debug_string(self):
		if self.current_sound_name is not None:
			return f'Channel {SoundMixer().get_index_of_channel(self.channel)}: {id(self.sounds[self.current_sound_name])} ({self.current_sound_name}) {"play" if self.get_busy() else "idle"}'
		return ''

	def remove(self):
		self.release_channel()
		SoundMixer().remove_sound_track(self)

	def distance_to(self, vector2: Vector2):
		if self.position is None:
			return 0
		return self.position.distance_to(vector2)

	def get_position(self):
		return self.position

	def get_play_amount(self):
		return self.play_amount

	def get_loop(self):
		return self.play_amount == -1

	def get_paused(self):
		return self.paused
