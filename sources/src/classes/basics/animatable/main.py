from src.classes import TimeHandler, DataHandler, LogHandler


class Animatable:
	def __init__(self, image_path: str):
		self.running = True  # indique si l'animation tourne
		self.frame_index = 0
		self.infinite = True
		self.image_path = image_path
		data, _ = DataHandler().load_image(image_path)
		self.animations = data['animations']
		self.animation_name = 'inactive'
		self.dt = 0

	def change_animation(self, animation_name):
		if self.animation_name == animation_name:
			return
		LogHandler().add(f'{self.name} * Changing animation: {self.animation_name} -> {animation_name}')

		previous_sound = self.animations[self.animation_name]['sound'] if 'sound' in self.animations[self.animation_name] else None
		self.animation_name = animation_name
		if 'sound' in self.animations[self.animation_name]:  # besoin de changer le son
			LogHandler().add(f'{self.name} * Changing sound: {self.animations[self.animation_name]['sound']}')
			self.play_sound(self.animations[self.animation_name]['sound'])
		else:  # pas de son dans la nouvelle animation
			self.stop_sound(previous_sound)

	def stop_animation(self):
		self.running = False
		if 'sound' in self.animations[self.animation_name]:
			self.stop_sound(self.animations[self.animation_name]['sound'])

	def resume_animation(self):
		self.running = True

	def reset_animation_state(self):
		self.frame_index = 0
		self.dt = 0

	def update_index_animation(self):
		self.dt += TimeHandler().get_delta_time()
		if not self.animations or not self.running:
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
