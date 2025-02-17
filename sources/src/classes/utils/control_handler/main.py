import pygame
from src.classes import DataHandler

class ControlHandler:
    _instance = None

    # Singleton
    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, '_initialized'):
            self._initialized = True
            save = DataHandler().load_save()
            self.events = {'quit': False, 'clicked': False}
            self.keybinds = self.load_keybinds(save['keybinds'])
            self.mouse_position = None
            self.consumed_events = set()

    def load_keybinds(self, keybinds_data):
        """
        Convertit les valeurs stockées en constantes Pygame si nécessaire.
        """
        return {action: getattr(pygame, key) if isinstance(key, str) else key for action, key in keybinds_data.items()}

    def handle_events(self):
        self.mouse_position = pygame.mouse.get_pos()
        self.finish_event('clicked')  # Réinitialiser l'état de clic à chaque frame
        
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self.events['quit'] = True
                case pygame.KEYDOWN:
                    for action, key in self.keybinds.items():
                        if key == event.key and action not in self.consumed_events:
                            self.activate_event(action)
                case pygame.KEYUP:
                    for action, key in self.keybinds.items():
                        if key == event.key:
                            self.finish_event(action)
                            self.consumed_events.discard(action)
                case pygame.MOUSEBUTTONDOWN:
                    self.activate_event('clicked')

    def is_activated(self, event: str):
        return self.events.get(event, False)

    def is_clicked(self, button):
        return self.is_activated('clicked') and button.get_rect().collidepoint(self.mouse_position)

    def activate_event(self, event: str):
        self.events[event] = True

    def finish_event(self, event_name: str):
        self.events[event_name] = False

    def consume_event(self, event_name: str):
        self.consumed_events.add(event_name)
        self.finish_event(event_name)

    def get_key_letter(self, event_name: str):
        """
        Retourne le nom de la touche associée à un événement.
        """
        key = self.keybinds.get(event_name)
        return pygame.key.name(key) if key else None
