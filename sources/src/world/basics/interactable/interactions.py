#Projet : Bletchley's Adventure
#Auteurs : Diego GIMENEZ, Maël KEN, Alexis LAROSE, Dimitri NERRAND

from src import GameLoop, Player, Vector2, LogHandler


class Interactions:
	_instance = None

	# singleton
	def __new__(cls, *args, **kwargs):
		if not isinstance(cls._instance, cls):
			cls._instance = object.__new__(cls, *args, **kwargs)
		return cls._instance

	def __init__(self):
		pass

	def test(self, _):
		GameLoop().get_player().get_focus().get_position().set_all(-20, -20)
		GameLoop().get_player().get_focus().play_sound('meow')

	def switch_with_test_2(self, _):
		if Player().get_map().get_name() == 'bletchley_park':
			Player().change_map('test_2')
			Player().teleport_to(Vector2())
		elif Player().get_map().get_name() == 'test_2':
			Player().change_map('bletchley_park')
			Player().teleport_to(Vector2())

	def mission_interaction(self, host):
		current_mission = GameLoop().get_mission_handler().get_current_mission()
		if current_mission is not None:
			current_mission.get_missions().get_objectives_store()[host.get_name() + '_interacted'] = True

	def switch_door_building_1(self, _):
		if Player().get_map().get_name() == 'bletchley_park':
			Player().change_map('building_1')
			Player().teleport_to('front_door_interior_1')
		elif Player().get_map().get_name() == 'building_1':
			Player().change_map('bletchley_park')
			Player().teleport_to('building_1_door')

	def switch_door_building_2(self, _):
		if Player().get_map().get_name() == 'bletchley_park':
			Player().change_map('building_2')
			Player().teleport_to('exit')
		elif Player().get_map().get_name() == 'building_2':
			Player().change_map('bletchley_park')
			Player().teleport_to('building_2_door')

	def switch_door_little_house(self, _):
		if Player().get_map().get_name() == 'bletchley_park':
			Player().change_map('little_house')
			Player().teleport_to('exit')
		elif Player().get_map().get_name() == 'little_house':
			Player().change_map('bletchley_park')
			Player().teleport_to('little_house_door')

	def switch_door_hut_6(self, _):
		if Player().get_map().get_name() == 'bletchley_park':
			Player().change_map('hut_6')
			Player().teleport_to('exit')
		elif Player().get_map().get_name() == 'hut_6':
			Player().change_map('bletchley_park')
			Player().teleport_to('hut_6_door')

	def switch_door_hut_8(self, _):
		if Player().get_map().get_name() == 'bletchley_park':
			Player().change_map('hut_8')
			Player().teleport_to('exit')
		elif Player().get_map().get_name() == 'hut_8':
			Player().change_map('bletchley_park')
			Player().teleport_to('hut_8_door')

	def switch_door_block_h(self, _):
		if Player().get_map().get_name() == 'bletchley_park':
			Player().change_map('block_h')
			Player().teleport_to('exit')
		elif Player().get_map().get_name() == 'block_h':
			Player().change_map('bletchley_park')
			Player().teleport_to('block_h_door')

	def switch_door_mansion(self, _):
		if Player().get_map().get_name() == 'bletchley_park':
			Player().change_map('mansion')
			Player().teleport_to('exit')
		elif Player().get_map().get_name() == 'mansion':
			Player().change_map('bletchley_park')
			Player().teleport_to('mansion_door')


	def do(self, interaction_name: str, host):
		LogHandler().add(f'interaction {interaction_name} activated')
		interaction_method = getattr(self, interaction_name, None)
		if interaction_method is None:
			return LogHandler().add(f'Unknown interaction: {interaction_name}')
		interaction_method(host)
