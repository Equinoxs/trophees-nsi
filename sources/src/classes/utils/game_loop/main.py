import pygame

from src.classes import  SCREEN_WIDTH, SCREEN_HEIGHT

class GameLoop:
	_instance = None

	# Singleton
	def __new__(cls, *args, **kwargs):
		if not isinstance(cls._instance, cls):
			cls._instance = object.__new__(cls)
		return cls._instance

	def __init__(
		self,
		screen = None,
		control_handler = None,
		time_handler = None,
		data_handler = None,
		player = None,
		sound_mixer = None,
		camera = None,
		mission_handler = None,
		menu_handler = None,
		log_handler = None
	):

		if not hasattr(self, '_initialized'):
			self._initialized = True

			self.running = True
			self.paused = False
			self.fullscreen = False

			self.screen = screen

			# singletons
			self.time_handler = time_handler
			self.data_handler = data_handler
			self.saved_data = self.data_handler.load_save()
			self.player = player
			self.camera = camera
			self.control_handler = control_handler
			self.sound_mixer = sound_mixer
			self.mission_handler = mission_handler
			self.menu_handler = menu_handler
			self.log_handler = log_handler

			self.time_handler.set_clock(pygame.time.Clock())

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

	def get_data_handler(self):
		return self.data_handler

	def get_mission_handler(self):
		return self.mission_handler

	def get_log_handler(self):
		return self.log_handler

	def is_game_paused(self):
		return self.paused

	def quit_game(self):
		self.running = False

	def pause_game(self):
		self.paused = True

	def unpause_game(self):
		self.paused = False

	def throw_event(self, event):
		self.get_player().get_map().throw_event(event)
	
	def toggle_fullscreen(self):
		if self.fullscreen == False:
			pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN | pygame.SCALED | pygame.HWSURFACE | pygame.DOUBLEBUF, vsync=1)
			self.fullscreen = True
		else:
			pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SCALED | pygame.HWSURFACE | pygame.DOUBLEBUF, vsync=1)
			self.fullscreen = False

	def update(self):
		self.control_handler.handle_events()
		if self.control_handler.is_activated('quit'):
			self.running = False

		# Quelques fonctionnalités
		if self.camera.get_is_map_rendered():
			if self.control_handler.is_activated('pause'):
				if self.menu_handler.get_current_menu_name() == 'in_game':
					self.menu_handler.get_button_actions().do('pause_game')
				elif self.menu_handler.get_current_menu_name() == 'saving':
					self.menu_handler.get_button_actions().do('pause_game')
				elif self.menu_handler.get_current_menu_name() == 'game_paused':
					self.menu_handler.get_button_actions().do('focus_on_game')
				elif self.menu_handler.get_current_menu_name() == 'map_opened':
					self.menu_handler.get_button_actions().do('focus_on_game')
				self.control_handler.consume_event('pause')
			if self.control_handler.is_activated('toggle_map'):
				if self.menu_handler.get_current_menu_name() == 'in_game':
					self.menu_handler.get_button_actions().do('open_map')
				elif self.menu_handler.get_current_menu_name() == 'map_opened':
					self.menu_handler.get_button_actions().do('focus_on_game')
				self.control_handler.consume_event('toggle_map')

		if self.control_handler.is_activated('enter') and self.menu_handler.get_current_menu_name() == 'welcome':
			self.menu_handler.get_button_actions().do('focus_on_game')

		# Updates
		self.time_handler.update()
		self.sound_mixer.update()
		if not self.paused:
			self.player.update()
			self.mission_handler.update()
		self.menu_handler.update()
		self.camera.update()

		# Gérer les sauvegardes automatiques
		if self.data_handler.must_save():
			self.data_handler.save()
