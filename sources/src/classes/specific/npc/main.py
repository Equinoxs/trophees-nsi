from src.classes import Vector2, TimeHandler, ControlHandler, MapObject, Camera

class NPC(MapObject):
	def __init__(self, name: str, pattern_timeline: list, position: Vector2, image_path: str, z_index: int, interaction: str = None, side_effects: list = []):
		MapObject.__init__(self, name, position, image_path, z_index, interaction, side_effects)
		self.initial_position = Vector2(position.get_x(), position.get_y())

		self.sprint = False
		self.speed = 1.38  # m/s = 5 km/h
		self.speed_vector = Vector2(0, 0)
  
		self.pattern_timeline = pattern_timeline
		self.pattern = list(filter(lambda val: isinstance(val, Vector2), self.pattern_timeline))
		self.following_pattern = True
		self.pattern_index = 0

		self.objective = self.pattern[self.pattern_index] if len(self.pattern) > 0 else None

		self.delta_time_event = None
		self.is_moving = False  # permet de SAVOIR si le NPC se dirige vers un objectif
		self.must_move = True  # permet de CONTRÔLER si le NPC doit se diriger vers son objectif

	def go_initial(self):
		self.set_objective(self.initial_position)

	def turn_right(self):
		if self.horizontal_flip:
			self.switch_horizontal_flip()

	def turn_left(self):
		if not self.horizontal_flip:
			self.switch_horizontal_flip()

	def update_player(self):
		if ControlHandler().is_activated('go_forward'):
			self.speed_vector.set_y(-1)
		elif ControlHandler().is_activated('go_backward'):
			self.speed_vector.set_y(1)
		else:
			self.speed_vector.set_y(0)

		if ControlHandler().is_activated('go_left'):
			self.speed_vector.set_x(-1)
		elif ControlHandler().is_activated('go_right'):
			self.speed_vector.set_x(1)
		else:
			self.speed_vector.set_x(0)

		if ControlHandler().is_activated('sprint'):
			self.sprint = True
		else:
			self.sprint = False

		speed_px = self.speed * 100 * Camera().get_zoom()  # 1m = 100px lorsque camera.zoom = 1
		if self.sprint:
			speed_px *= 1.5
		self.speed_vector.set_norm(speed_px)

	def set_objective(self, new_objective = None):
		self.objective = new_objective

	def stop_moving(self):
		self.speed_vector.set_all(0, 0)
		self.must_move = False

	def resume_moving(self):
		self.must_move = True

	def handle_animation(self):
		if abs(self.speed_vector.get_y()) >= abs(2 * self.speed_vector.get_x()) + 1:  # ajout d'une constante pour prévenir des instabilités numériques
			if self.speed_vector.get_y() > 0:
				self.change_animation('walking_backward')
			elif self.speed_vector.get_y() < 0:
				self.change_animation('walking_forward')
		elif abs(self.speed_vector.get_x()) > 1:
			if self.speed_vector.get_x() < 0:
				self.turn_left()
			elif self.speed_vector.get_x() > 0:
				self.turn_right()
			self.change_animation('walking')
		else:  # Pas de mouvement ou vitesse négligeable
			self.change_animation('inactive')
			self.reset_animation_state()


	# Cette méthode se charge de véhiculer les NPC à un point fixé (a.k.a. self.objective)
	# Elle est appelé à chaque frame
	def move_npc_to_objective(self):
		if self.objective is not None and self.must_move:
			relative_objective = self.objective - self.position
			if relative_objective.get_norm() <= 1:
				self.stop_moving()
				return False

			self.speed_vector.copy(relative_objective).set_norm(self.speed / 1.5 * 100 * Camera().get_zoom())

			if relative_objective.get_x() < 0:
				self.turn_left()
			elif relative_objective.get_x() > 0:
				self.turn_right()
			return True
		else:
			self.stop_moving()
			return False

	# Cette méthode est appelé à chaque fois que le NPC à atteint un objectif de son pattern
	# Elle gère ainsi les appels aux fonctions qui doivent être appelé dans le pattern
	def handle_events(self):
		count_vector2 = 0
		index_in_timeline = 0
		for index, value in enumerate(self.pattern_timeline):
			if isinstance(value, Vector2):
				count_vector2 += 1
				if count_vector2 == self.pattern_index + 1:
					index_in_timeline = index - 1
					break

		if isinstance(self.pattern_timeline[index_in_timeline], Vector2):
			return False

		do_again = self.pattern_timeline[index_in_timeline](self, TimeHandler().add_chrono_tag(self.name))
		if do_again == False:
			TimeHandler().remove_chrono_tag(self.name)
		return do_again

	# Se charge du bon déroulement de self.pattern_timeline et gère donc les appels de
	# self.handle_events() et self.move_npc_to_objective()
	def update_pattern(self):
		if not self.pattern:
			return

		if self.following_pattern:
			if not self.is_moving:
				do_again = self.handle_events()

				if do_again:
					self.objective = None
					return  # on empêche le redéfinissement de l'objectif, le résultat sera le même la prochaine fois

				else:
					# Le personnage a atteint son obj, n'active pas d'évènements, on lui donne un autre objectif
					self.pattern_index = (self.pattern_index + 1) % len(self.pattern)
					self.set_objective(self.pattern[self.pattern_index])
					self.resume_moving()
		else:
			self.objective = None

		self.is_moving = self.move_npc_to_objective()

	def update(self):
		MapObject.update(self)
		self.update_pattern()
		self.handle_animation()

	def render(self):
		width, height = self.image.get_size()
		Camera().get_screen().blit(
			self.image,
			(
				Camera().get_zoom() * (self.position.x - width / 2 - Camera().get_camera().x),
				Camera().get_zoom() * (self.position.y - height - Camera().get_camera().y)
			)
		)
