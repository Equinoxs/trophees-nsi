# Point d'entrée du jeu

from src.classes import TimeHandler, ControlHandler, DataHandler, GameLoop, Map, Player, SoundMixer


def main():
	# Initialisation des singletons
	sound_mixer = SoundMixer()
	control_handler = ControlHandler()
	time_handler = TimeHandler()
	save_handler = DataHandler()
	saved_data = save_handler.load_save()
	player = Player(Map(saved_data["player"]["current_map_name"]), saved_data['player']['current_npc_name'])
	game_loop = GameLoop(control_handler, time_handler, save_handler, player, sound_mixer)
	return 0


if __name__ == "__main__":
	main()
