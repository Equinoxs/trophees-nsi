import pygame

from src.classes import TimeHandler, ControlHandler, DataHandler, GameLoop, Map, Player, SoundMixer, Camera, MissionHandler, MenuHandler, LogHandler, SCREEN_WIDTH, SCREEN_HEIGHT


def main() -> int:
	pygame.init()
	pygame.font.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.NOFRAME | pygame.SCALED | pygame.HWSURFACE | pygame.DOUBLEBUF, vsync=1)

	# Initialisation des singletons
	data_handler = DataHandler()
	saved_data = data_handler.load_save()
	sound_mixer = SoundMixer()
	control_handler = ControlHandler()
	time_handler = TimeHandler()
	player = Player(Map(saved_data['player']['current_map_name']), saved_data['player'], saved_data['player']['current_map_name'])
	camera = Camera(screen)
	mission_handler = MissionHandler(DataHandler().load_missions())
	menu_handler = MenuHandler()
	log_handler = LogHandler()

	game_loop = GameLoop(
		screen,
		control_handler,
		time_handler,
		data_handler,
		player,
		sound_mixer,
		camera,
		mission_handler,
		menu_handler,
		log_handler
	)

	return 0


# Point d'entrée du jeu
if __name__ == '__main__':
	main()
