from src.classes import GameLoop, LogHandler, DataHandler


class ButtonActions:	
	_instance = None

	# singleton
	def __new__(cls, *args, **kwargs):
		if not isinstance(cls._instance, cls):
			cls._instance = object.__new__(cls, *args, **kwargs)
		return cls._instance

	def __init__(self):
		pass

	def start_new_game(self, _):
		GameLoop().get_menu_handler().set_current_menu('loading', True)
		DataHandler().load_save(new_game=True, reload=True)
		self.focus_on_game(_)

	def focus_on_game(self, _):
		GameLoop().get_camera().map_rendered()
		GameLoop().get_menu_handler().set_current_menu('in_game')
		GameLoop().get_sound_mixer().unpause_music()
		GameLoop().unpause_game()

	def pause_game(self, _):
		GameLoop().pause_game()
		DataHandler().save()
		GameLoop().get_menu_handler().set_current_menu('game_paused')
		GameLoop().get_sound_mixer().pause_music()

	def return_to_title(self, _):
		GameLoop().pause_game()
		GameLoop().get_menu_handler().set_current_menu('welcome')
		GameLoop().get_sound_mixer().pause_music()

	def open_settings(self, _):
		GameLoop().pause_game()
		GameLoop().get_menu_handler().set_current_menu('settings')
		GameLoop().get_sound_mixer().pause_music()

	def quit_game(self, _):
		GameLoop().quit_game()

	def return_to_last_menu(self, _):
		GameLoop().get_menu_handler().set_last_menu()

	def open_credits(self, _):
		GameLoop().pause_game()
		GameLoop().get_menu_handler().set_current_menu('credits')
		GameLoop().get_sound_mixer().pause_music()

	def toggle_fullscreen(self, _):
		GameLoop().toggle_fullscreen()

	def open_map(self, _):
		GameLoop().pause_game()
		GameLoop().get_menu_handler().set_current_menu('map_opened')

	def open_saving(self, _):
		GameLoop().pause_game()
		GameLoop().get_menu_handler().set_current_menu('saving')

	def save_game(self, _):
		from src.classes import SavingInput
		input_field = SavingInput.active_input
		text = input_field.get_text()
		LogHandler().add(f'Saved to file {text}')
		DataHandler().save(text)

	def load_game(self, button):
		GameLoop().get_menu_handler().set_current_menu('loading', True)
		DataHandler().load_save(name=button.get_label(), force=True, reload=True)
		self.focus_on_game(button)

	def open_loading(self, _):
		GameLoop().pause_game()
		GameLoop().get_menu_handler().set_current_menu('loading_games')
		current_menu = GameLoop().get_menu_handler().get_current_menu()
		for idx, save_file in enumerate(DataHandler().get_save_files(names=True)):
			current_menu.add_element({
				'type': 'Button',
				'class': 'pause_button',
				'label': save_file,
				'y': 250 + 60 * idx,
				'width': 'auto',
				'x': 'center',
				'action': 'load_game'
			})

	def do(self, action_name, button = None):
		LogHandler().add(f'Button action {action_name} activated')
		action_method = getattr(self, action_name, None)
		if action_method is None:
			return LogHandler().add(f'Unknown button action: {action_name}')
		return action_method(button)