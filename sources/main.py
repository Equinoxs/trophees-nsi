# Point d'entrée du jeu

from src.classes.utils import GameLoop, TimeHandler, ControlHandler, SaveHandler

control_handler = None
time_handler = None
save_handler = None


def main():
    control_handler = ControlHandler()
    time_handler = TimeHandler()
    save_handler = SaveHandler()
    game_loop = GameLoop()
    return 0


if __name__ == "__main__":
    main()
