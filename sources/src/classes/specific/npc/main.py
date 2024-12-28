from src.classes import Vector2, TimeHandler, ControlHandler, PillarObject, Camera, DataHandler, GameLoop, Player


class NPC(PillarObject):
	def __init__(self, data):
		self.image_type = 'npc'
		super().__init__(data)
		self.initial_position = Vector2(data['position'].get_x(), data['position'].get_y())

		self.sprint = False
		self.is_player = False
		self.speed = 1.38  # m/s = 5 km/h
		self.speed_vector = Vector2(0, 0)
		self.walking_on = None
		self.level = None
		self.set_level(data['level'])
  
		self.pattern_timeline = data['pattern_timeline']
		self.pattern = list(filter(lambda val: isinstance(val, Vector2), self.pattern_timeline))
		self.following_pattern = True
		self.pattern_index = 0
		self.pattern_type = data['pattern_type']

		self.objective = self.pattern[self.pattern_index] if len(self.pattern) > 0 else None

		self.delta_time_event = None
		self.is_moving = False  # permet de SAVOIR si le NPC se dirige vers un objectif
		self.must_move = True  # permet de CONTRÔLER si le NPC doit se diriger vers son objectif

	def get_level(self):
		return self.level

	def set_level(self, level: float):
		self.level = level
		if self.is_player:
			GameLoop().throw_event('player_level_change')

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
		if DataHandler().must_save(): DataHandler().save(automatic=True)

	def set_objective(self, new_objective = None):
		self.objective = new_objective
		if self.objective is None:
			self.stop_moving()
		else:
			self.resume_moving()

	def set_following_pattern(self, new_following_pattern: bool):
		self.following_pattern = new_following_pattern

	def set_is_player(self, new_state: bool):
		self.is_player = new_state
		if new_state == True:
			self.gimme_all_sound_tracks()
		else:
			self.dont_gimme_all_sound_tracks()

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

	# Cette méthode est appelée à chaque fois que le NPC a atteint un objectif de son pattern
	# Elle gère ainsi les appels aux fonctions définies dans le pattern
	def handle_events(self):
		count_vector2 = 0
		index_in_timeline = None

		for index, value in enumerate(self.pattern_timeline):
			if isinstance(value, Vector2):
				count_vector2 += 1
				if count_vector2 == self.pattern_index + 1:
					index_in_timeline = index - 1
					break

		if index_in_timeline is None or not callable(self.pattern_timeline[index_in_timeline]):
			return False

		do_again = self.pattern_timeline[index_in_timeline](self, TimeHandler().add_chrono_tag(self.name))
		if do_again is False:
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
					if self.pattern_index + 1 == len(self.pattern):
						match self.pattern_type:
							case 'loop':
								self.pattern_index = 0
							case 'back_and_forth':
								self.pattern_index = 0
								self.pattern.reverse()
					self.pattern_index += 1
					self.set_objective(self.pattern[self.pattern_index])
					self.resume_moving()
		self.is_moving = self.move_npc_to_objective()

	def update(self):
		if self.speed_vector.get_norm() > 1:
			surface_type = Player().get_map().which_surface(self.position)
			if surface_type != self.walking_on:
				self.walking_on = surface_type
				self.set_animation_sound_name(f'walking_{self.walking_on}')
		elif self.walking_on is not None:
			self.walking_on = None
			self.set_animation_sound_name(self.walking_on)

		super().update()
		self.handle_animation()
		if self.is_player:
			self.update_player()
		else:
			self.update_pattern()

	def render(self):
		width, height = self.image.get_size()
		x, y = self.position.convert_to_tuple()
		self.position.set_all(int(x) - width // 2, int(y) - height)
		super().render()
		self.position.set_all(x, y)
