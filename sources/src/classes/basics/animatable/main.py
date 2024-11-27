from src.classes import TimeHandler, SaveHandler


class Animatable:
	def __init__(self, image_path: str):
		self.running = True
		self.dt = 0
		self.frame_index = 0
		self.infinite = True
		data, _ = SaveHandler().load_image(image_path)
		self.animations = data['animations']
		self.animation_name = 'walking'  # --> cas particulier pour les tests, à rendre ça dynamique
		self.animation_sound_data = self.animation_sound_path = None
		if self.animation_name not in self.animations: return
		if "sound" in self.animations[self.animation_name]:
			self.animation_sound_data, self.animation_sound_path = SaveHandler().load_sound(image_path, self.animations[self.animation_name]["sound"])
			self.load_sound(self.animation_sound_path)


	def stop_animation(self):
		self.running = False

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


	def update_animation_sound(self):
		if self.animation_sound_data is None: return
		if not self.get_busy() and self.running: self.play_sound()
		if not self.running: self.stop_sound()
