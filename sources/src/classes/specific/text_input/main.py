import pygame
from src.classes import UIElement, GameLoop, ControlHandler

class TextInput(UIElement):
	def __init__(self, data):
		super().__init__(data)
		self.text = data.get("default_text", "")  # Texte par défaut
		self.event_keys = []
		self.last_event_key = None
		self.event_name = data.get('event_name', '')
		self.max_event_key = data.get('max_event_key', None)
		self.set_label(self.text)
		self.focus = False  # Si l'utilisateur édite le champ

	def done(self):
		pass

	def update(self):
		# Vérifier si on clique sur l'élément
		if ControlHandler().is_clicked(self):
			self.focus = True
		elif not self.rect.collidepoint(pygame.mouse.get_pos()) and ControlHandler().is_activated('clicked'):
			self.focus = False

		# Si le champ est actif, détecter la saisie
		if self.focus:
			for event in ControlHandler().get_pygame_events():
				if event.type == pygame.KEYDOWN:

					# Correction des noms de touches spéciales
					if event.key == pygame.K_BACKSPACE:
						self.event_keys = self.event_keys[:-1]
					else:
						self.last_event_key = event.key
						self.event_keys.append(self.last_event_key)
						key_name = pygame.key.name(self.event_keys[-1])
						self.text += key_name

		# Met à jour l'affichage du texte s'il y a eu un changement
		if self.last_event_key is not None:
			if self.max_event_key is not None and len(self.event_keys) >= self.max_event_key + 1:
				self.event_keys = self.event_keys[-self.max_event_key:]
				self.done()
			elif self.max_event_key is not None and len(self.event_keys) == self.max_event_key:
				self.done()
			elif ControlHandler().is_activated('enter'):
				self.done()

			self.text = ''.join([pygame.key.name(event_key) for event_key in self.event_keys])
			self.set_label(self.text)
			self.last_event_key = None

	def render(self):
		# Dessine l'élément et met à jour sa bordure si actif
		border_color = (255, 255, 255) if self.focus else (150, 150, 150)
		pygame.draw.rect(GameLoop().get_camera().get_surface("menu"), border_color, self.rect, width=2)
		super().render()
