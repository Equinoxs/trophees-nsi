import pygame

from src.classes import Vector2, DataHandler


class Sprite:
	def __init__(self, position: Vector2, image_path: str):
		self.position = position
		self.vertical_flip = False
		self.horizontal_flip = False
		self.magnification_coeff = 1  # image x fois plus grande
		if not hasattr(self, 'image_type'):
			self.image_type = ''
   
		if hasattr(self, 'image'):
			return

		data, png_path = DataHandler().load_image(image_path, self.image_type)
		self.original_image = pygame.image.load(png_path)
		self.image = pygame.image.load(png_path)
		self.image_path = image_path
		self.image_data = data  # les infos de l'image
		self.go_to_frame(0, 'inactive')


	def switch_horizontal_flip(self):
		self.horizontal_flip = not self.horizontal_flip
		self.image = pygame.transform.flip(self.image, True, self.vertical_flip)

	def switch_vertical_flip(self):
		self.vertical_flip = not self.vertical_flip
		self.image = pygame.transform.flip(self.image, self.horizontal_flip, True)

	def get_position(self):
		return self.position

	def get_image(self):
		return self.image

	def get_image_data(self):
		return self.image_data

	def go_to_frame(self, frame_index, animation_name, coeff=1):
		width, height = self.image.get_size()
		if self.image_data['animations'] == {}:
			return
		left = sum(frame["width"] for frame in self.image_data['animations'][animation_name]['widths'][0:frame_index])

		top = 0
		for animation_key, val in self.image_data['animations'].items():
			if animation_key == animation_name:
				subsurface_height = val["height"]
				break
			top += val["height"]

		if len(self.image_data['animations'][animation_name]['widths']) == 0:
			subsurface_width = width
		else:
			subsurface_width = int((self.image_data['animations'][animation_name]['widths'][frame_index]["width"]) * coeff)

		# Ajuster pour éviter les erreurs liées à des tailles impaires
		subsurface_width -= subsurface_width % 2
		subsurface_height -= subsurface_height % 2

		# Rogner l'image (subsurface)
		self.image = self.original_image.subsurface((left, top, subsurface_width, subsurface_height))

		# Réappliquer les inversions d'axes
		self.image = pygame.transform.flip(self.image, self.horizontal_flip, self.vertical_flip)

	def skew_image(self, surface: pygame.Surface, horizontal_skew: int, vertical_skew: int):
		width, height = surface.get_size()
		new_width = int(width + abs(horizontal_skew))
		new_height = int(height + abs(vertical_skew))
		skewed_image = pygame.Surface((new_width, new_height), pygame.SRCALPHA)
		
		x_offset = min(0, horizontal_skew)
		y_offset = min(0, vertical_skew)
		
		for x in range(new_width):
			for y in range(new_height):
				original_x = x - horizontal_skew * (y / height) + x_offset
				original_y = y - vertical_skew * (x / width) + y_offset

				if 0 <= original_x < width and 0 <= original_y < height:
					color = surface.get_at((int(original_x), int(original_y)))
					skewed_image.set_at((x, y), color)

		return skewed_image

	def fill_surface(self, surface: pygame.Surface, width: int, height: int):
		surface_width, surface_height = surface.get_size()
		filled_surface = pygame.Surface((width, height), pygame.SRCALPHA)
		filled_surface.fill((0,) * 4)
		
		# Remplissage bord à bord
		for x in range(0, width, surface_width):
			for y in range(0, height, surface_height):
				blit_width = min(surface_width, width - x)
				blit_height = min(surface_height, height - y)
				
				temp_surface = pygame.Surface((blit_width, blit_height), pygame.SRCALPHA)
				temp_surface.blit(surface, (0, 0))
				
				filled_surface.blit(temp_surface, (x, y))

		return filled_surface

	def get_magnification(self):
		return self.magnification_coeff

	def set_magnification(self, magnification_coeff):
		width, height = self.image.get_size()

		# Redimensionner l'image (scale)
		self.image = pygame.transform.scale(self.image, (width * magnification_coeff, height * magnification_coeff))
		self.magnification_coeff = magnification_coeff

	def rotate(self, angle):
		# Rotation de l'image
		self.image = pygame.transform.rotate(self.image, angle)

	def move_to(self, position: Vector2):
		self.position.copy(position)
