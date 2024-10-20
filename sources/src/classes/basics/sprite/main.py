import pygame
from .. import Vector2

class Sprite:
	def __init__(self, position: Vector2, image_path: str, frame: tuple = (0, 10_000)):
		self.position = position
		self.image = pygame.image.load(image_path)
		self.frame = frame  # le bord gauche et le bord droit

	def move_frame(self, deplacement, coeff=1):
		# Récupérer la taille de l'image
		width, height = self.image.get_size()
		left = self.frame[0] + deplacement
		right = (self.frame[1] + deplacement) * coeff

		# Vérifier que la fenêtre de cadrage ne dépasse pas les limites de l'image
		if left < 0: left = 0
		if right > width: right = width

		# Rogner l'image (subsurface)
		self.image = self.image.subsurface((left, 0, right - left, height))

	def magnify(self, magnification_coeff):
		width, height = self.image.get_size()

		# Redimensionner l'image (scale)
		self.image = pygame.transform.scale(self.image, (int(width * magnification_coeff), int(height * magnification_coeff)))
		self.move_frame(0, magnification_coeff)

	def rotate(self, angle):
		# Rotation de l'image
		self.image = pygame.transform.rotate(self.image, angle)

	def move(self, x, y):
		self.position.set_all(x, y)
