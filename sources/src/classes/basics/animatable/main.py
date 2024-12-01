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
		self.update_sound()

	def change_animation(self, animation_name):
		if self.animation_name == animation_name: return
		LogHandler().add(f'{self.name} * Changing animation: {self.animation_name} -> {animation_name}')
		self.animation_name = animation_name
		if self.animation_sound_data is not None:
			LogHandler().add(f'{self.name} * Stopping sound: {self.animation_sound_path.split("/")[-1]}')
			self.stop_sound(self.animation_sound_path)
			self.remove_sound(self.animation_sound_path)
		self.update_sound()
		if self.animation_sound_data is not None and not self.get_busy(self.animation_sound_path):
			LogHandler().add(f'{self.name} * Playing sound: {self.animation_sound_path.split("/")[-1]}')
			self.play_sound(self.animation_sound_path)

	def update_sound(self):
		self.animation_sound_data, self.animation_sound_path = None, None
		if "sound" in self.animations[self.animation_name]:
			self.animation_sound_data, self.animation_sound_path = DataHandler().load_sound(self.image_path, self.animations[self.animation_name]["sound"])
			LogHandler().add(f'{self.name} * Loading sound: {self.animation_sound_path.split("/")[-1]}')
			self.load_sound(self.animation_sound_path, loop=self.infinite)

	def stop_animation(self):
		self.running = False
		if self.animation_sound_data is not None:
			self.stop_sound(self.animation_sound_path)

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
