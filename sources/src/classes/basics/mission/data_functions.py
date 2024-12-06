from src.classes import GameLoop, TimeHandler, Player


# Dans cet exemple, cet objectif consiste à se rendre au dessus de la map en moins de 10 secondes
def objective1():
	time = TimeHandler().add_chrono_tag('objective1')
	if time == 0:
		GameLoop().get_sound_mixer().play_music('tryhard')  # l'objectif commence
	if time > 10:
		TimeHandler().remove_chrono_tag('objective1')  # On libère le chrono tag
		GameLoop().get_sound_mixer().play_music_prev()
		Player().get_focus().play_sound('goose')
		return -1  # mission échouée
	else:
		if Player().get_focus().get_position().get_y() <= 0:
			TimeHandler().remove_chrono_tag('objective1')
			GameLoop().get_sound_mixer().play_music_prev()
			Player().get_focus().play_sound('meow')
			return 1  # objectif réussi
		else:
			return 0  # objectif en cours

mission_test = [objective1]


missions = {
	'mission_test': mission_test
}