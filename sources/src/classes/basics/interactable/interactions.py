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

	def switch_with_test_2(_, host):
		if Player().get_map_name() == 'bletchley_park':
			Player().change_map('test_2')
		elif Player().get_map_name() == 'test_2':
			Player().change_map('bletchley_park')

	def switch_door_building_1(_, host):
		if Player().get_map_name() == 'bletchley_park':
			Player().change_map('building_1')
			Player().teleport_to('front_door_interior_1')
		elif Player().get_map_name() == 'building_1':
			Player().change_map('bletchley_park')
			Player().teleport_to('building_1_door')

	def switch_door_building_2(_, host):
		if Player().get_map_name() == 'bletchley_park':
			Player().change_map('building_2')
			Player().teleport_to('exit')
		elif Player().get_map_name() == 'building_2':
			Player().change_map('bletchley_park')
			Player().teleport_to('building_2_door')

	def switch_door_little_house(_, host):
		if Player().get_map_name() == 'bletchley_park':
			Player().change_map('little_house')
			Player().teleport_to('exit')
		elif Player().get_map_name() == 'little_house':
			Player().change_map('bletchley_park')
			Player().teleport_to('little_house_door')


	def do(self, interaction_name: str, host):
		LogHandler().add(f'interaction {interaction_name} activated')
		match interaction_name:
			case 'test':
				self.test(host)
			case 'house_proprietary_start_mission_test':
				self.start_mission_test(host)
			case 'switch_with_test_2':
				self.switch_with_test_2(host)
			case 'switch_door_building_1':
				self.switch_door_building_1(host)
			case 'switch_door_building_2':
				self.switch_door_building_2(host)
			case 'switch_door_little_house':
				self.switch_door_little_house(host)
			case _:
				LogHandler().add(f'Unknown interaction: {interaction_name}')
