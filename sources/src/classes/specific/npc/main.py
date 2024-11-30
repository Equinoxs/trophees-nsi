from src.classes import Vector2, TimeHandler, ControlHandler, MapObject, Camera

class NPC(MapObject):
	def __init__(self, name: str, pattern_timeline: list, position: Vector2, image_path: str, z_index: int, interaction: str = None):
		MapObject.__init__(self, name, position, image_path, z_index, interaction)
		self.initial_position = Vector2(position.get_x(), position.get_y())

		self.sprint = False
		self.speed = 1.38  # m/s = 5 km/h
		self.speed_vector = Vector2(0, 0)
  
		self.pattern_timeline = pattern_timeline
		self.pattern = list(filter(lambda val: isinstance(val, Vector2), self.pattern_timeline))
		self.following_pattern = True
		self.back_to_initial = False
		self.walking_time = 0
		self.objective_index = 0
		self.objective = self.pattern[self.objective_index] if len(self.pattern) > 0 else None
		self.delta_time_event = None
		self.is_moving = False

	def go_initial(self):
		self.following_pattern = False
		self.back_to_initial = True
		self.objective = self.initial_position
		self.walking_time = (self.objective - self.position).get_norm() / self.speed

	def turn_right(self):
		if self.horizontal_flip:
			self.switch_horizontal_flip()

	def turn_left(self):
		if not self.horizontal_flip:
			self.switch_horizontal_flip()

	def update_player(self):
		if ControlHandler().is_activated('go_forward'):
			self.speed_vector.set_y(-1)
			self.change_animation('walking')
		elif ControlHandler().is_activated('go_backward'):
			self.speed_vector.set_y(1)
			self.change_animation('walking')
		else:
			self.speed_vector.set_y(0)

		if ControlHandler().is_activated('go_left'):
			self.speed_vector.set_x(-1)
			self.change_animation('walking')
			self.turn_left()
		elif ControlHandler().is_activated('go_right'):
			self.speed_vector.set_x(1)
			self.change_animation('walking')
			self.turn_right()
		else:
			self.speed_vector.set_x(0)
   
		if not ControlHandler().is_activated('go_forward') and not ControlHandler().is_activated('go_backward') and not ControlHandler().is_activated('go_left') and not ControlHandler().is_activated('go_right'):
			self.change_animation('inactive')
			self.reset_animation_state()

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
		self.walking_time = ((self.objective - self.position).get_norm() / self.speed * 1.5) / (100 * Camera().get_zoom()) 

	# Cette méthode se charge de véhiculer les NPC à un point fixé (a.k.a. self.objective)
	# Elle est appelé à chaque frame
	def move_npc_to_objective(self):
		if self.objective is not None:
			dt = TimeHandler().get_delta_time()
			if self.walking_time > 0:
				self.walking_time -= dt
			else:
				self.change_animation('inactive')
				self.reset_animation_state()
				self.objective = None
				self.speed_vector.set_all(0, 0)
				return False

			relative_objective = self.objective - self.position
			self.speed_vector.copy(relative_objective).set_norm(self.speed / 1.5 * 100 * Camera().get_zoom())
			self.change_animation('walking')

			if relative_objective.get_x() < 0:
				self.turn_left()
			elif relative_objective.get_x() > 0:
				self.turn_right()
			return True
		else:
			self.change_animation('inactive')
			self.reset_animation_state()
			self.speed_vector.set_all(0, 0)
			return False

	# Cette méthode est appelé à chaque fois que le NPC à atteint un objectif de son pattern
	# Elle gère ainsi les appels aux fonctions qui doivent être appelé dans le pattern
	def handle_events(self):
		count_vector2 = 0
		index_in_timeline = 0
		for index, value in enumerate(self.pattern_timeline):
			if isinstance(value, Vector2):
				count_vector2 += 1
				if count_vector2 == self.objective_index + 1:
					index_in_timeline = index - 1
					break

		if isinstance(self.pattern_timeline[index_in_timeline], Vector2):
			return False

		if self.delta_time_event is None:
			self.delta_time_event = 0
		elif self.delta_time_event is not None:
			self.delta_time_event += TimeHandler().get_delta_time()

		do_again = self.pattern_timeline[index_in_timeline](self, self.delta_time_event)
		if do_again == False:
			self.delta_time_event = None
		return do_again

	# Se charge du bon déroulement de self.pattern_timeline et gère donc les appels de
	# self.handle_events() et self.move_npc_to_objective()
	def update_pattern(self):
		if not self.pattern:
			return

		if self.following_pattern or self.back_to_initial:
			if not self.is_moving:
				do_again = self.handle_events()
    
				if do_again:
					self.objective = None
					self.change_animation('inactive')
					self.reset_animation_state()
					return  # on empêche le redéfinissement de l'objectif, le résultat sera le même la prochaine fois

				else:
					# Le personnage a atteint son obj, n'active pas d'évènements, on lui donne un autre objectif
					self.objective_index = (self.objective_index + 1) % len(self.pattern)
					self.set_objective(self.pattern[self.objective_index])
		else:
			self.objective = None

		self.is_moving = self.move_npc_to_objective()

	def update(self):
		MapObject.update(self)
		self.update_pattern()

	def render(self):
		width, height = self.image.get_size()
		Camera().get_screen().blit(
			self.image,
			(
				Camera().get_zoom() * (self.position.x - width / 2 - Camera().get_camera().x),
				Camera().get_zoom() * (self.position.y - height - Camera().get_camera().y)
			)
		)
