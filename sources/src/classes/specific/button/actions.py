from src.classes import GameLoop, LogHandler


class ButtonActions:
	_instance = None

	# singleton
	def __new__(cls, *args, **kwargs):
		if not isinstance(cls._instance, cls):
			cls._instance = object.__new__(cls, *args, **kwargs)
		return cls._instance

	def __init__(self):
		pass

	def focus_on_game(self):
		GameLoop().get_menu_handler().set_current_menu('in_game')
		GameLoop().get_sound_mixer().unpause_music()
		GameLoop().unpause_game()

	def pause_game(self):
		GameLoop().pause_game()
		GameLoop().get_menu_handler().set_current_menu('game_paused')
		GameLoop().get_sound_mixer().pause_music()

	def quit_game(self):
		GameLoop().quit_game()

	def open_settings(self):
		pass

	def open_map(self):
		GameLoop().get_menu_handler().set_current_menu('map_opened')

	def do(self, action_name):
		LogHandler().add(f'Button action {action_name} activated')
		match action_name:
			case 'focus_on_game':
				self.focus_on_game()
			case 'pause_game':
				self.pause_game()
			case 'quit_game':
				self.quit_game()
			case 'open_settings':
				self.open_settings()
			case 'open_map':
				self.open_map()
			case _:
				LogHandler().add(f'Unknown button action: {action_name}')
