import pygame
import json
from src.classes.basics.ui_element.main import UIButton

class MenuHandler:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_initialized"):
            self._initialized = True
            self.menus = {}
            self.active_menu = None
            self.actions = {}

    def load_menus(self, json_path, actions):
        """
        Charge les menus à partir d'un fichier JSON et associe les actions disponibles.
        """
        self.actions = actions  # Dictionnaire contenant les actions
        with open(json_path, 'r') as file:
            data = json.load(file)
        
        for button_data in data["buttons"]:
            button = UIButton(
                x=button_data["x"],
                y=button_data["y"],
                width=button_data["width"],
                height=button_data["height"],
                label=button_data["label"],
                action=self.actions.get(button_data["action"]),
                color=tuple(button_data["color"]),
                text_color=tuple(button_data["text_color"]),
                font_size=button_data["font_size"]
            )
            menu_name = button_data.get("menu", "default")  # Permet de grouper les boutons par menu
            if menu_name not in self.menus:
                self.menus[menu_name] = []
            self.menus[menu_name].append(button)

    def set_active_menu(self, menu_name):
        """Définit le menu actif."""
        if menu_name in self.menus:
            self.active_menu = menu_name

    def render(self, screen):
        """Affiche les éléments du menu actif."""
        if self.active_menu and self.active_menu in self.menus:
            for element in self.menus[self.active_menu]:
                element.draw(screen)

    def handle_event(self, event):
        """Gère les événements pour les éléments du menu actif."""
        if self.active_menu and self.active_menu in self.menus:
            for element in self.menus[self.active_menu]:
                if isinstance(element, UIButton):
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Clic gauche
                        if element.is_clicked(event.pos):
                            element.click()
