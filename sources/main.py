#Projet : Bletchley's Adventure
#Auteurs : Diego GIMENEZ, Maël KEN, Alexis LAROSE, Dimitri NERRAND

'''
Fichier principal du jeu, seuls Python 3.10 ou une version ultérieure et les requirements sont nécessaires pour l'exécuter.
Python 3.13 est recommandé pour éviter tout problème de version.
'''

import sys
if sys.version_info < (3, 10):  # Empêcher l'exécution du script si Python n'est pas assez récent
	sys.exit('Python 3.10 or a more recent version is required.')

import pygame

from src import TimeHandler, ControlHandler, DataHandler, GameLoop, Map, Player, SoundMixer, Camera, MissionHandler, MenuHandler, LogHandler, SCREEN_WIDTH, SCREEN_HEIGHT


def main() -> int:
	pygame.mixer.init()
	pygame.init()
	pygame.font.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SCALED | pygame.HWSURFACE | pygame.DOUBLEBUF, vsync=1)

	# Initialisation des singletons
	data_handler = DataHandler()
	saved_data = data_handler.load_save()
	sound_mixer = SoundMixer()
	control_handler = ControlHandler(saved_data)
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
