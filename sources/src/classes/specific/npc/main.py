from src.classes import Vector2, TimeHandler, ControlHandler, MapObject, Camera

class NPC(MapObject):
	def __init__(self, pattern: list[Vector2], position: Vector2, image_path: str, z_index: int, interaction: str = None):
		MapObject.__init__(self, position, image_path, z_index, interaction)
		self.initial_position = Vector2(position.get_x(), position.get_y())
		self.pattern = pattern
		self.following_pattern = True
		self.back_to_initial = False
		self.walking_time = 0
		self.speed = 1.38 # m/s = 5 km/h
		self.sprint = False
		self.objective_index = -1
		self.objective = self.pattern[self.objective_index]
		self.speed_vector = Vector2(0, 0)

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
			self.resume_animation()
		elif ControlHandler().is_activated('go_backward'):
			self.speed_vector.set_y(1)
			self.resume_animation()
		else:
			self.speed_vector.set_y(0)

		if ControlHandler().is_activated('go_left'):
			self.speed_vector.set_x(-1)
			self.resume_animation()
			self.turn_left()
		elif ControlHandler().is_activated('go_right'):
			self.speed_vector.set_x(1)
			self.resume_animation()
			self.turn_right()
		else:
			self.speed_vector.set_x(0)
   
		if not ControlHandler().is_activated('go_forward') and not ControlHandler().is_activated('go_backward') and not ControlHandler().is_activated('go_left') and not ControlHandler().is_activated('go_right'):
			self.stop_animation()
			self.reset_animation_state()

		if ControlHandler().is_activated('sprint'):
			self.sprint = True
		else:
			self.sprint = False

		speed_px = self.speed * 100 * Camera().get_zoom()  # 1m = 100px lorsque camera.zoom = 1
		if self.sprint:
			speed_px *= 1.5
		self.speed_vector.set_norm(speed_px)

	def update_pattern(self):
		if self.following_pattern or self.back_to_initial:
			dt = TimeHandler().get_delta_time()
			if self.walking_time > 0:
				self.walking_time -= dt
			else:
				self.objective_index += 1
				if self.objective_index == len(self.pattern):
					self.objective_index -= len(self.pattern)
				self.objective = self.pattern[self.objective_index]
				self.walking_time = self.objective.get_norm() / self.speed # v = d/t <=> t = d/v
			self.apply_force((self.objective - self.position).set_norm(self.speed * dt))

	def update(self):
		MapObject.update(self)
		self.update_pattern()
