from src.classes import GameLoop, Player, MissionHandler

def test(self):
	GameLoop().get_player().get_focus().get_position().set_all(-20, -20)
	GameLoop().get_player().get_focus().play_sound('meow')


def house_proprietary_start_mission_test(self):
	if 'mission_test' not in Player().get_accomplished_missions():
		self.play_sound('voice')
		MissionHandler().start_mission('mission_test')


interactions = {
	"test": test,
	"house_proprietary_start_mission_test": house_proprietary_start_mission_test
}