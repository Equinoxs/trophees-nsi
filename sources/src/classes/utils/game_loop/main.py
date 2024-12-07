import pygame
from src.classes.basics.ui_element.main import UIElementManager
from src.classes.specific.button.actions import ButtonActions  # type: ignore
from src.classes.specific.menu.main import MenuHandler


class GameLoop:
    _instance = None

    # Singleton
    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, control_handler=None, time_handler=None, save_handler=None, player=None, sound_mixer=None, camera=None, mission_handler=None):
        if not hasattr(self, "_initialized"):
            self._initialized = True

            # Initialisations
            pygame.init()
            self.screen = pygame.display.set_mode((1280, 720), flags=pygame.SCALED, vsync=1)
            self.running = True
            self.time_handler = time_handler
            self.time_handler.set_clock(pygame.time.Clock())
            self.save_handler = save_handler
            self.saved_data = self.save_handler.load_save()
            self.player = player
            self.camera = camera
            self.control_handler = control_handler
            self.sound_mixer = sound_mixer
            self.mission_handler = mission_handler

            # Pause management
            self.paused = False
            self.can_pause = True

            # UI Management
            self.ui_manager = UIElementManager()
            self.actions = ButtonActions(self)

            # Menu Handler
            self.menu_handler = MenuHandler()
            self._initialize_menus()

            # Set default menu
            self.menu_handler.set_active_menu("default")

            # Main loop
            while self.running:
                self.update()
                pygame.display.flip()

            pygame.quit()

    def _initialize_menus(self):
        """
        Initialize menus using MenuHandler and predefined actions.
        """
        # Load menus from JSON or hardcode buttons here if necessary
        json_path = '../ui_element/data.json'  # Replace with the path to your JSON file
        self.menu_handler.load_menus(
            json_path,
            {
                "pause_game": self.actions.pause_game,
                "unpause_game": self.actions.unpause_game,
                "quit_game": self.actions.quit_game,
            }
        )

    def get_player(self):
        return self.player

    def get_camera(self):
        return self.camera

    def get_control_handler(self):
        return self.control_handler

    def get_sound_mixer(self):
        return self.sound_mixer

    def get_time_handler(self):
        return self.time_handler

    def is_game_paused(self):
        return self.paused

    def update(self):
        # Handle general control events
        self.control_handler.handle_events(pygame)

        # Quit event
        if self.control_handler.is_activated("quit"):
            self.running = False

        # Pause handling
        if self.control_handler.is_activated("pause"):
            if self.can_pause:
                self.paused = not self.paused
                self.menu_handler.set_active_menu("pause" if self.paused else "default")
                self.can_pause = False
            self.control_handler.finish_event("pause")
        else:
            self.can_pause = True

        # Handle active menu events
        for event in pygame.event.get():
            MenuHandler().handle_event(event)


        # Updates
        self.time_handler.update(self.paused)
        self.sound_mixer.update()
        if not self.paused:
            self.player.update()
            self.mission_handler.update()

        # Rendering
        self.camera.update()
        self.camera.render(self.screen)
        self.menu_handler.render(self.screen)
