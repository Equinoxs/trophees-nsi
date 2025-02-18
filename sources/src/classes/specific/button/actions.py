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
		GameLoop().get_camera().map_rendered()
		GameLoop().get_menu_handler().set_current_menu('in_game')
		GameLoop().get_sound_mixer().unpause_music()
		GameLoop().unpause_game()

	def pause_game(self):
		GameLoop().pause_game()
		GameLoop().get_menu_handler().set_current_menu('game_paused')
		GameLoop().get_sound_mixer().pause_music()

	def return_to_title(self):
		GameLoop().pause_game()
		GameLoop().get_menu_handler().set_current_menu('welcome')
		GameLoop().get_sound_mixer().pause_music()

	def open_settings(self):
		GameLoop().pause_game()
		GameLoop().get_menu_handler().set_current_menu('settings')
		GameLoop().get_sound_mixer().pause_music()

	def quit_game(self):
		GameLoop().quit_game()

	def return_to_last_menu(self):
		GameLoop().get_menu_handler().set_last_menu()

	def open_credits(self):
		GameLoop().pause_game()
		GameLoop().get_menu_handler().set_current_menu('credits')
		GameLoop().get_sound_mixer().pause_music()

	def toggle_fullscreen(self):
		GameLoop().toggle_fullscreen()

	def open_map(self):
		GameLoop().pause_game()
		GameLoop().get_menu_handler().set_current_menu('map_opened')

	def open_dialog(self):
		GameLoop().get_menu_handler().set_current_menu('dialog_opened')

	def do(self, action_name):
		LogHandler().add(f'Button action {action_name} activated')
		action_method = getattr(self, action_name, None)
		if action_method is None:
			return LogHandler().add(f'Unknown button action: {action_name}')
		action_method()
