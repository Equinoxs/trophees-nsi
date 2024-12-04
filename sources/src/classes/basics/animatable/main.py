from src.classes import TimeHandler, DataHandler, LogHandler


class Animatable:
	def __init__(self, image_path: str):
		self.running = True
		self.dt = 0
		self.frame_index = 0
		self.infinite = True
		self.image_path = image_path
		data, _ = DataHandler().load_image(image_path)
		self.animations = data['animations']
		self.animation_name = 'inactive'
		self.animation_sound_data = self.animation_sound_path = None
		if self.animation_name not in self.animations: return
		if 'sound_type' in self.animations[self.animation_name]:
			LogHandler().add(f'{self.name} * Loading sound: {self.animations[self.animation_name]["sound"]}')
			self.load_sound(self.animations[self.animation_name]['sound_type'], self.animations[self.animation_name]['sound_file'], loop=self.infinite, needs_playing=True)

	def change_animation(self, animation_name):
		if self.animation_name == animation_name: return

		LogHandler().add(f'{self.name} * Changing animation: {self.animation_name} -> {animation_name}')

		previous_sound_type = self.animations[self.animation_name]['sound_type'] if 'sound_type' in self.animations[self.animation_name] else None
		self.animation_name = animation_name
		if 'sound_type' in self.animations[self.animation_name]: # besoin de changer le son
			LogHandler().add(f'{self.name} * Changing sound: {self.animations[self.animation_name]["sound_file"]}')
			self.change_sound(self.animations[self.animation_name]['sound_type'], self.animations[self.animation_name]['sound_file'], needs_playing=True)
		else: # pas de son dans la nouvelle animation
			self.stop_sound(previous_sound_type)
			self.remove_sound(previous_sound_type)

	def stop_animation(self):
		self.running = False
		if 'sound_type' in self.animations[self.animation_name]:
			self.stop_sound(self.animations[self.animation_name]['sound_type'])

	def resume_animation(self):
		self.running = True

	def reset_animation_state(self):
		self.frame_index = 0
		self.dt = 0

	def update_index_animation(self):  # Renvoie vrai si le MapElement doit être animé
		self.dt += TimeHandler().get_delta_time()
		if self.animations == {} or not self.running:
			return

		scheme = self.animations[self.animation_name]['widths']

		# Calcul du nombre de frames à sauter
		while self.dt >= scheme[self.frame_index]["time"]:
			self.dt -= scheme[self.frame_index]["time"]
			self.frame_index += 1

			# Si on dépasse la dernière frame
			if self.frame_index >= len(scheme):
				if self.infinite:
					self.frame_index = 0  # Boucle au début
				else:
					self.frame_index = len(scheme) - 1  # Reste sur la dernière frame
					self.running = False
