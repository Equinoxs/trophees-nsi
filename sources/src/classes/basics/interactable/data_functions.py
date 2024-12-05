from src.classes import GameLoop

def test(self):
	GameLoop().get_player().get_focus().get_position().set_all(-20, -20)
	GameLoop().get_player().get_focus().play_sound('meow')


interactions = {
	"test": test
}