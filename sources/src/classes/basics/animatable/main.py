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
