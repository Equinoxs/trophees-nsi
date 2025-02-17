import pygame
from src.classes import UIElement, GameLoop, ControlHandler

class TextInput(UIElement):
    def __init__(self, data):
        super().__init__(data)
        self.text = data.get("default_text", "")  # Texte par défaut
        self.active = False  # Si l'utilisateur édite le champ

    def update(self):
        # Vérifier si on clique sur l'élément
        if ControlHandler().is_clicked(self):
            self.active = True
        elif not self.rect.collidepoint(pygame.mouse.get_pos()) and ControlHandler().is_activated('clicked'):
            self.active = False


        # Si le champ est actif, détecter la saisie
        if self.active:
            for action, key in ControlHandler().keybinds.items():
                if ControlHandler().is_activated(action):
                    key_name = pygame.key.name(key)
                    # Correction des noms de touches spéciales

                    if key == pygame.K_BACKSPACE:
                        self.text = "Backspace"
                    if key == pygame.K_RETURN:
                        self.text = "Enter"
                    else:
                        self.text = key_name



        # Met à jour l'affichage du texte
        self.set_label(self.text)

    def render(self):
        # Dessine l'élément et met à jour sa bordure si actif
        border_color = (255, 255, 255) if self.active else (150, 150, 150)
        pygame.draw.rect(GameLoop().get_camera().get_surface("menu"), border_color, self.rect, width=2)
        super().render()
