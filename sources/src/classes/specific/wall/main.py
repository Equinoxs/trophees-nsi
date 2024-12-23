import pygame

from src.classes import MapObject, DataHandler, Vector2


class Wall(MapObject):
    def __init__(self, data):
        self.image_type = 'wall'
        self.wall_type = data['wall_type']
        self.wall_height = data['wall_height']
        self.wall_width = data['wall_width']
        self.boundaries = data['boundaries']
        image_data, front_path, side_path, top_path = DataHandler().load_wall_images(self.wall_type)
        self.original_front_image = pygame.image.load(front_path)
        self.original_side_image = pygame.image.load(side_path)
        self.original_top_image = pygame.image.load(top_path)
        self.image_data = image_data
        self.image_data['animations'] = {}
        self.position = Vector2(0, 0)
        self.calculate_wall_image()
        data['position'] = self.position
        self.image_data['hitbox'] = [point + Vector2(0, self.wall_height) - self.position for point in self.boundaries]
        super().__init__(data)

    def skew_image(self, surface: pygame.Surface, horizontal_skew: int, vertical_skew: int):
        width, height = surface.get_size()
        new_width, new_height = width + horizontal_skew, height + vertical_skew
        skewed_image = pygame.Surface((new_width, new_height), pygame.SRCALPHA)

        for x in range(new_width):
            for y in range(new_height):
                original_x = x - horizontal_skew * y // height
                original_y = y - vertical_skew * x // width

                if 0 <= original_x < width and 0 <= original_y < height:
                    color = surface.get_at((original_x, original_y))
                    skewed_image.set_at((x, y), color)

        return skewed_image

    def calculate_wall_image(self):
        self.position = self.boundaries[0]
        self.position.set_y(self.position.get_y() - self.wall_height)

        for i in range(1, len(self.boundaries)):
            p1 = self.boundaries[i - 1]
            p2 = self.boundaries[i]
            p1_to_p2 = p2 - p1

            if p1_to_p2.get_y() < 0:
                self.position.set_y(self.position.get_y() - p1_to_p2.get_y())

            width, height = self.original_front_image.get_size()
            front_length = int(p1_to_p2.get_norm())
            front_image = pygame.Surface((front_length, self.wall_height), pygame.SRCALPHA)
            front_image.fill((0,) * 4)
            for x in range(0, front_length, width):
                for y in range(0, self.wall_height, height):
                    front_image.blit(self.original_front_image, (x, y))
            front_image = pygame.transform.scale(front_image, (p1_to_p2.get_x(), self.wall_height))
            self.front_image_perspective = self.skew_image(front_image, 0, p2.get_y() - p1.get_y())
            self.image = self.front_image_perspective
