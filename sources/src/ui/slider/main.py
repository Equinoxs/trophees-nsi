import pygame

from src import UIElement, SliderActions, ControlHandler, GameLoop


class Slider(UIElement):
    def __init__(self, data):
        super().__init__(data)

        self.min_value = data.get("min_value", 0)
        self.max_value = data.get("max_value", 100)
        self.current_value = data.get("default_value", self.min_value)

        self.slider_width = data.get("slider_width", 10)
        self.track_color = tuple(data.get("track_color", (200, 200, 200)))
        self.slider_color = tuple(data.get("slider_color", (255, 255, 255)))
        self.border_radius = data.get("border_radius", 0)
        self.border_color = tuple(data.get("border_color", (0, 0, 0)))

        self.action_name = data["action"]  # L'action à exécuter
        self.dragging = False

    def update(self):
        super().update()
        mouse_pos = pygame.mouse.get_pos()

        if ControlHandler().is_clicked(self):
            self.dragging = True
        elif not pygame.mouse.get_pressed()[0]:
            self.dragging = False

        if self.dragging:
            rel_x = max(0, min(mouse_pos[0] - self.rect.x, self.rect.width))
            new_value = self.min_value + (rel_x / self.rect.width) * (self.max_value - self.min_value)
            new_value = int(new_value)  # Conversion en entier

            if new_value != self.current_value:
                self.current_value = new_value
                SliderActions().do(self.action_name, self.current_value)

        if self.rect.collidepoint(mouse_pos):
            return True
        return False

    def render(self):
        surface = GameLoop().get_camera().get_surface("menu")
        pygame.draw.rect(surface, self.track_color, self.rect, border_radius=self.border_radius)
        
        # Limiter la position du slider pour qu'il ne dépasse pas la barre
        slider_x = self.rect.x + (self.current_value - self.min_value) / (self.max_value - self.min_value) * self.rect.width
        slider_x = max(self.rect.x + self.slider_width // 2, min(slider_x, self.rect.right - self.slider_width // 2))
        
        slider_rect = pygame.Rect(slider_x - self.slider_width // 2, self.rect.y, self.slider_width, self.rect.height)
        
        pygame.draw.rect(surface, self.slider_color, slider_rect, border_radius=self.border_radius)
        pygame.draw.rect(surface, self.border_color, self.rect, width=1, border_radius=self.border_radius)
    
    def get_value(self):
        return self.current_value
