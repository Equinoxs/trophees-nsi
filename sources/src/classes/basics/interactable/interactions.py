from src.classes import GameLoop, Player, MissionHandler, LogHandler


class Interactions:
	_instance = None

	# singleton
	def __new__(cls, *args, **kwargs):
		if not isinstance(cls._instance, cls):
			cls._instance = object.__new__(cls, *args, **kwargs)
		return cls._instance

	def __init__(self):
		pass

	def test(_, host):
		GameLoop().get_player().get_focus().get_position().set_all(-20, -20)
		GameLoop().get_player().get_focus().play_sound('meow')


	def start_mission_test(_, host):
		if 'mission_test' not in Player().get_accomplished_missions():
			host.play_sound('voice')
			MissionHandler().start_mission('mission_test')


	def do(self, interaction_name: str, host):
		LogHandler().add(f'interaction {interaction_name} activated')
		match interaction_name:
			case 'test':
				self.test(host)
			case 'house_proprietary_start_mission_test':
				self.start_mission_test(host)
			case _:
				LogHandler().add(f'Unknown interaction: {interaction_name}')
