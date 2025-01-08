from src.classes import GameLoop, TimeHandler, Player


class Missions:
	_instance = None

	# singleton
	def __new__(cls, *args, **kwargs):
		if not isinstance(cls._instance, cls):
			cls._instance = object.__new__(cls, *args, **kwargs)
		return cls._instance

	def __init__(self):
		if not hasattr(self, '_initialized'):
			self._initialized = True

			# Les clés ci-dessous doivent être de la forme <nom_de_la_mission>_<index_de_l'objectif>
			self.objective_descriptions = {
				'mission_test_0': 'get your y coordinate below 0 under 10 seconds!'
			}

	def get_description(self, mission_name: str, index: int):
		return self.objective_descriptions.get(f'{mission_name}_{index}', 'Mysterious objective...')

	def mission_test_0(_):
		time = TimeHandler().add_chrono_tag('mission_test_0')
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
			TimeHandler().remove_chrono_tag('mission_test_0')
		return index

	def mission_test(self, index: int):
		match index:
			case 0:
				return self.mission_test_0()
		

	def do(self, mission_name: str, index: int):
		match mission_name:
			case 'mission_test':
				return self.mission_test(index)
