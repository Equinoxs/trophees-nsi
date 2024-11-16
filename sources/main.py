# Point d'entrée du jeu

from src.classes import TimeHandler, ControlHandler, SaveHandler, GameLoop

game_loop = None

def main():
    control_handler = ControlHandler()
    time_handler = TimeHandler()
    save_handler = SaveHandler()
    game_loop = GameLoop()
    return 0


if __name__ == "__main__":
    main()
