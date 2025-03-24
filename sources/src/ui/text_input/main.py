import pygame

from src import UIElement, ControlHandler


class TextInput(UIElement):
	def __init__(self, data):
		super().__init__(data)

		self.text = data.get('default_text', '')  # Texte par défaut
		self.set_label(self.text)

		self.first_input = True
		self.focus = False  # Si l'utilisateur édite le champ

		self.replace = data.get('replace', True)
		self.underscore = data.get('underscore', False)
		self.done_func = None

		self.intercept = data.get('intercept', 'text')

		self.event_keys = []
		self.last_event_key = None
		self.event_name = data.get('event_name', '')
		self.max_event_key = data.get('max_event_key', None)

	def get_text(self):
		return self.text

	def done(self):
		if callable(self.done_func):
			self.done_func(self)

	def update_label(self):
		if self.underscore:
			self.set_label(self.text + '_')
		else:
			self.set_label(self.text)
		self.calculate_text_surface(self.surface_width)

	def empty_text(self):
		self.event_keys = []
		self.set_text('')

	def set_text(self, new_text: str):
		self.text = new_text
		self.update_label()

	def set_done_func(self, func):
		self.done_func = func

	def get_done_func(self):
		return self.done_func

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
					if self.first_input:
						self.text = ''
						self.event_keys = []
						self.first_input = False

					if event.key == pygame.K_RETURN:
						self.done()

					elif event.key == pygame.K_BACKSPACE:
						if self.intercept == 'keys' and len(self.event_keys) > 0:
							self.event_keys.pop()
							self.last_event_key = 'lol, easter egg'
						elif self.intercept == 'text' and len(self.text) > 0:
							self.text = self.text[:-1]
							self.update_label()

					elif event.key == pygame.K_SPACE and self.intercept == 'keys':
						self.last_event_key = event.key
						self.event_keys.append(self.last_event_key)

					elif self.intercept == 'keys':
						self.last_event_key = event.key
						self.event_keys.append(self.last_event_key)
						key_name = pygame.key.name(self.event_keys[-1])
						self.text += key_name

				elif event.type == pygame.TEXTINPUT and self.intercept == 'text' and len(self.text) <= self.max_event_key:
					self.text += event.text
					self.update_label()

		# Met à jour l'affichage du texte s'il y a eu un changement
		if self.last_event_key is not None and self.intercept == 'keys':
			if self.max_event_key is not None and len(self.event_keys) >= self.max_event_key:
				self.event_keys = self.event_keys[-self.max_event_key:]
				self.done()

			# Met à jour le label (affichage)
			self.text = ''.join([
				' ' if event_key == pygame.K_SPACE else pygame.key.name(event_key)
				for event_key in self.event_keys
			])
			self.update_label()
			self.last_event_key = None
		super().update()

	def render(self):
		self.border_color = (255, 255, 255) if self.focus else (150, 150, 150)
		super().render()
