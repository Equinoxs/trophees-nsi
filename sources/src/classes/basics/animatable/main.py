from src.classes import TimeHandler, DataHandler, LogHandler


class Animatable:
	def __init__(self, image_path: str):
		self.animation_running = True  # indique si l'animation tourne
		self.frame_index = 0
		self.infinite = True
		self.animation_name = 'inactive'
		self.dt = 0
		self.animation_sound_name = None
		self.image_path = image_path
		self.animations = self.image_data['animations']

	def set_animation_sound_name(self, sound_name: str = None):
		if sound_name:
			if sound_name != self.animation_sound_name:
				LogHandler().add(f'{self.name} * Manually set and play sound: {sound_name}')
				self.stop_sound(self.animation_sound_name)
				self.play_sound(sound_name)
		else:
			LogHandler().add(f'{self.name} * Stop sound: {self.animation_sound_name}')
			self.stop_sound(self.animation_sound_name)
		self.animation_sound_name = sound_name

	def change_animation(self, animation_name: str, force: bool = False):
		if self.animation_name == animation_name and not force:
			return

		previous_animation = self.animation_name
		self.animation_name = animation_name

		previous_sound = self.animations.get(previous_animation, {}).get('sound')
		animation_sound = self.animations.get(animation_name, {}).get('sound')
		current_sound = self.animation_sound_name if self.animation_sound_name else animation_sound

		if previous_sound and previous_sound != current_sound:
			LogHandler().add(f'{self.name} * Stop previous sound: {previous_sound}')
			self.stop_sound(previous_sound)

		if current_sound and current_sound != previous_sound:
			LogHandler().add(f'{self.name} * Play new sound: {current_sound}')
			self.play_sound(current_sound, loop=True)

		if not self.animation_sound_name:
			self.animation_sound_name = animation_sound


	def stop_animation(self):
		self.animation_running = False
		if 'sound' in self.animations[self.animation_name]:
			self.stop_sound(self.animations[self.animation_name]['sound'])

	def resume_animation(self):
		self.animation_running = True

	def reset_animation_state(self):
		self.frame_index = 0
		self.dt = 0

	def update_index_animation(self):
		self.dt += TimeHandler().get_delta_time()
		if not self.animations or not self.animation_running:
			return

		scheme = self.animations[self.animation_name]['widths']

		while self.dt >= scheme[self.frame_index]['time']:
			self.dt -= scheme[self.frame_index]['time']
			self.frame_index += 1

			if self.frame_index >= len(scheme):
				if self.infinite:
					self.frame_index = 0
				else:
					self.frame_index = len(scheme) - 1
					self.running = False
					break
