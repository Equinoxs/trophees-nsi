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

	def pause_game(self):
		GameLoop().pause_game()
		GameLoop().get_menu_handler().render(GameLoop().get_camera().get_screen())  # Rendu du menu avec le rectangle

	def unpause_game(self):
		GameLoop().unpause_game()

	def quit_game(self):
		GameLoop().quit_game()

	def open_settings(self):
		pass

	def do(self, action_name):
		LogHandler().add(f'Button action {action_name} activated')
		match action_name:
			case 'pause_game':
				self.pause_game()
			case 'unpause_game':
				self.unpause_game()
			case 'quit_game':
				self.quit_game()
			case _:
				LogHandler().add(f'Unknown button action: {action_name}')
