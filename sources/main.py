# Point d'entrée du jeu

from src.classes.utils import GameLoop, TimeHandler, ControlHandler

def main():
	control_handler = ControlHandler()
	time_handler = TimeHandler()
	gameLoop = GameLoop(control_handler, time_handler)
	return 0

if __name__ == "__main__":
	main()
