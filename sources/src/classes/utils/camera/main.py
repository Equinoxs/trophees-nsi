from src.classes import Player

class Camera:
    def __init__(self, screen):
        self.screen = screen
        self.frame = self.screen.get_rect()
        self.camera = self.frame.copy()

    def update(self):
        elements = Player().get_map().get_elements()
        player_pos = Player().get_focus().get_position().convert_to_tuple()
        width, height = Player().get_focus().get_image().get_size()
        self.camera.center = (player_pos[0] + width / 2, player_pos[1] + height / 2)
        # Remplir l'écran de noir
        self.screen.fill((0,) * 3)
        for element in elements:
            # element.go_next_frame()
            self.screen.blit(element.get_image(), (element.get_position().get_x() - self.camera.x, element.get_position().get_y() - self.camera.y))