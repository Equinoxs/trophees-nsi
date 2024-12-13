import pygame


class GameLoop:
	_instance = None

	# Singleton
	def __new__(cls, *args, **kwargs):
		if not isinstance(cls._instance, cls):
			cls._instance = object.__new__(cls)
		return cls._instance

	def __init__(
		self,
		control_handler = None,
		time_handler = None,
		save_handler = None,
		player = None,
		sound_mixer = None,
		camera = None,
		mission_handler = None,
		menu_handler = None
	):

		if not hasattr(self, '_initialized'):
			self._initialized = True
			pygame.init()
			self.screen = pygame.display.set_mode((1280, 720), flags=pygame.SCALED, vsync=1)
			self.running = True
			self.time_handler = time_handler
			self.time_handler.set_clock(pygame.time.Clock())
			self.save_handler = save_handler
			self.saved_data = self.save_handler.load_save()
			self.player = player
			self.camera = camera
			self.control_handler = control_handler
			self.sound_mixer = sound_mixer
			self.mission_handler = mission_handler
			self.menu_handler = menu_handler

			self.paused = False
			self.can_pause = True

			# Main loop
			while self.running:
				self.update()
				pygame.display.flip()

			pygame.quit()

	def get_player(self):
		return self.player

	def get_camera(self):
		return self.camera

	def get_control_handler(self):
		return self.control_handler

	def get_sound_mixer(self):
		return self.sound_mixer

	def get_time_handler(self):
		return self.time_handler

	def get_menu_handler(self):
		return self.menu_handler

	def is_game_paused(self):
		return self.paused

	def quit_game(self):
		self.running = False

	def pause_game(self):
		self.paused = True
		self.menu_handler.set_current_menu('game_paused')

	def unpause_game(self):
		self.paused = False
		self.menu_handler.set_current_menu('in_game')

	def throw_event(self, event):
		self.get_player().get_map().throw_event(event)

	def update(self):
		self.control_handler.handle_events()
		if self.control_handler.is_activated('quit'):
			self.running = False

		# Système de pause
		if self.control_handler.is_activated('pause'):
			if self.can_pause:
				if self.paused:
					self.unpause_game()
				else:
					self.pause_game()
				self.can_pause = False
			self.control_handler.finish_event('pause')
		else:
			self.can_pause = True

		# Updates
		self.time_handler.update(self.paused)
		self.menu_handler.update()
		self.sound_mixer.update()
		if not self.paused:
			self.player.update()
			self.mission_handler.update()
		self.camera.update()
