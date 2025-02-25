import pygame
from src.classes import UIElement, GameLoop, ControlHandler

class TextInput(UIElement):
	def __init__(self, data):
		super().__init__(data)
		self.text = data.get('default_text', '')  # Texte par défaut
		self.event_keys = []
		self.last_event_key = None
		self.event_name = data.get('event_name', '')
		self.max_event_key = data.get('max_event_key', None)
		self.set_label(self.text)
		self.focus = False  # Si l'utilisateur édite le champ
		self.replace = data.get('replace', 'True') == 'True'
		self.first_input = True

		# Liste des touches spéciales à ignorer
		self.invalid_keys = [
			# Touches de contrôle
			pygame.K_LSHIFT, pygame.K_RSHIFT, pygame.K_LCTRL, pygame.K_RCTRL,
			pygame.K_LALT, pygame.K_RALT, pygame.K_CAPSLOCK, pygame.K_TAB,
			pygame.K_NUMLOCK, pygame.K_SCROLLLOCK, pygame.K_ESCAPE,

			# Touches fonctionnelles (F1 à F12)
			*[getattr(pygame, f'K_F{i}') for i in range(1, 13)],

			# Pavé numérique
			pygame.K_KP0, pygame.K_KP1, pygame.K_KP2, pygame.K_KP3, pygame.K_KP4,
			pygame.K_KP5, pygame.K_KP6, pygame.K_KP7, pygame.K_KP8, pygame.K_KP9,
			pygame.K_KP_PERIOD, pygame.K_KP_DIVIDE, pygame.K_KP_MULTIPLY,
			pygame.K_KP_MINUS, pygame.K_KP_PLUS, pygame.K_KP_ENTER, pygame.K_KP_EQUALS
		]

	def get_text(self):
		return self.text

	def done(self):
		pass
	
	def done2(self):
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
					# Nettoyer le texte si c'est la première saisie et replace est désactivé
					if self.first_input and not self.replace:
						self.text = ''
						self.event_keys = []
						self.first_input = False

					if not self.replace and event.key in self.invalid_keys:
						continue

					if event.key == pygame.K_RETURN and not self.replace:
						self.done2()

					if event.key == pygame.K_BACKSPACE and len(self.event_keys) != 0:
						self.event_keys.pop()
						self.last_event_key = 'lol, easter egg'


					elif event.key == pygame.K_SPACE:
						self.last_event_key = event.key
						self.event_keys.append(self.last_event_key)
						self.text += ' '  # Remplace par un vrai espace

					elif event.key != pygame.K_BACKSPACE and event.key != pygame.K_RETURN:
						self.last_event_key = event.key
						self.event_keys.append(self.last_event_key)
						key_name = pygame.key.name(self.event_keys[-1])
						self.text += key_name
						print

		# Met à jour l'affichage du texte s'il y a eu un changement
		if self.last_event_key is not None:
			if self.max_event_key is not None and len(self.event_keys) >= self.max_event_key:
				if self.replace:
					self.event_keys = self.event_keys[-self.max_event_key:]
				else:
					while len(self.event_keys) >= self.max_event_key:
						self.event_keys.pop()
				self.done()

			# Met à jour le label (affichage)
			self.text = ''.join([
				' ' if event_key == pygame.K_SPACE else pygame.key.name(event_key)
				for event_key in self.event_keys
			])
			self.set_label(self.text)
			self.last_event_key = None

	def render(self):
		# Dessine l'élément et met à jour sa bordure si actif
		border_color = (255, 255, 255) if self.focus else (150, 150, 150)
		pygame.draw.rect(GameLoop().get_camera().get_surface('menu'), border_color, self.rect, width=2)
		super().render()
