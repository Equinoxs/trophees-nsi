from src.classes import GameLoop, TimeHandler, Player


# Dans cet exemple, cet objectif consiste à se rendre au dessus de la map en moins de 10 secondes
def objective1():
	time = TimeHandler().add_chrono_tag('objective1')
	index = 0
	if time == 0:
		GameLoop().get_sound_mixer().play_music('tryhard')  # l'objectif commence
	if time > 10:
		Player().get_focus().play_sound('game_over')
		index = -1  # mission échouée
	else:
		if Player().get_focus().get_position().get_y() <= 0:
			Player().get_focus().play_sound('magical_hit')
			index = 1  # objectif réussi
		else:
			index = 0  # objectif en cours
	if index != 0:
		GameLoop().get_sound_mixer().play_music_prev()
		TimeHandler().remove_chrono_tag('objective1')
	return index

mission_test = [objective1]


missions = {
	'mission_test': mission_test
}