import pygame

from src.classes import TimeHandler, ControlHandler, DataHandler, GameLoop, Map, Player, SoundMixer, Camera, MissionHandler, MenuHandler


def main() -> int:
	# Initialisation des singletons
	pygame.init()
	screen = pygame.display.set_mode((1280, 720), flags=pygame.SCALED, vsync=1)
	sound_mixer = SoundMixer()
	control_handler = ControlHandler()
	time_handler = TimeHandler()
	save_handler = DataHandler()
	saved_data = save_handler.load_save()
	player = Player(Map(saved_data['player']['current_map_name']), saved_data['player'])
	camera = Camera(screen)
	mission_handler = MissionHandler(DataHandler().load_missions())
	menu_handler = MenuHandler()

	game_loop = GameLoop(
		control_handler,
		time_handler,
		save_handler,
		player,
		sound_mixer,
		camera,
		mission_handler,
		menu_handler
	)

	return 0


# Point d'entrée du jeu
if __name__ == '__main__':
	main()
