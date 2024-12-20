import pygame

from src.classes import MapObject


class Wall(MapObject):
    def __init__(self, data):
        super().__init__(data)
        self.positions = data['positions']
        self.front_image = data['front_image']
        self.side_image = data['side_image']
        self.top_image = data['top_image']
        self.calculate_wall_image()
    
    # Le fait de mettre ce calcul dans une méthode nous autorise à changer la position des murs (pratique pour les portes)
    def calculate_wall_image(self):
        self.image = pygame.Surface()