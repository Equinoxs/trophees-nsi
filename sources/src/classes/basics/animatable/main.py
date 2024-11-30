from src.classes import TimeHandler, SaveHandler


class Animatable:
	def __init__(self, image_path: str):
		self.running = True
		self.dt = 0
		self.frame_index = 0
		self.infinite = True
		data, _ = SaveHandler().load_image(image_path)
		self.animations = data['animations']
		self.animation_name = 'inactive'
		self.animation_sound_data = self.animation_sound_path = None
		if self.animation_name not in self.animations: return
		if "sound" in self.animations[self.animation_name]:
			self.animation_sound_data, self.animation_sound_path = SaveHandler().load_sound(image_path, self.animations[self.animation_name]["sound"])
			self.load_sound(self.animation_sound_path, loop=self.infinite)

	def change_animation(self, animation_name):
		self.animation_name = animation_name

	def stop_animation(self):
		self.running = False
		if self.animation_sound_data is not None:
			self.stop_sound(self.animation_sound_path)

	def resume_animation(self):
		self.running = True
		if self.animation_sound_data is not None and not self.get_busy(self.animation_sound_path):
			self.play_sound(self.animation_sound_path)

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
