import pygame

class UIButton:
    def __init__(self, x, y, width, height, label, action, color, text_color, font_size):
        self.rect = pygame.Rect(x, y, width, height)
        self.label = label
        self.action = action
        self.color = color
        self.text_color = text_color
        self.font = pygame.font.Font(None, font_size)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = self.font.render(self.label, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, position):
        return self.rect.collidepoint(position)

    def click(self):
        if callable(self.action):
            self.action()


class UIElementManager:
    def __init__(self):
        self.active_elements = []

    def set_buttons(self, buttons):
        """Ajoute une liste de boutons actifs."""
        self.active_elements = buttons

    def draw(self, screen):
        """Dessine tous les éléments actifs."""
        for element in self.active_elements:
            element.draw(screen)

    def handle_event(self, event):
        """Gère les clics sur les éléments."""
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Clic gauche
            for element in self.active_elements:
                if isinstance(element, UIButton) and element.is_clicked(event.pos):
                    element.click()
