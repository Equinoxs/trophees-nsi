#Projet : Bletchley's Adventure
#Auteurs : Diego GIMENEZ, Maël KEN, Alexis LAROSE, Dimitri NERRAND

import pygame

from src import UIElement, GameLoop, TimeHandler, DataHandler, ControlHandler, MenuHandler


class Dialog(UIElement):
	def __init__(self, data):
		UIElement.__init__(self, data)
		self._text_surfaces = {}
		self.messages = data.get('messages', [])
		self.title = data['title']

		self.message_id = -1
		self.next_message()

		self.text_margin = data.get('text_margin', 20)
		self.arrow_image = pygame.image.load(DataHandler().load_ui_elements_image('arrow'))
		self.wrapped_text_finish = False

		self.chrono_tag_set = False

	def wrap_text(self, use_chrono_tag = False):
		y = self.rect.top + self.text_margin
		font_height = self.font.size('Tg')[1]
		if use_chrono_tag:
			text = self.label[:round(len(self.label) * (TimeHandler().add_chrono_tag('dialog_text_wrap') / self.text_display_duration))]
		else:
			text = self.label
		self._text_surfaces = {}
		self._text_surface = None
		while text:
			i = 1
			if y + font_height > self.rect.bottom:
				break
			while self.font.size(text[:i])[0] < (self.rect.width - 2 * self.text_margin) and i < len(text):
				i += 1

			if i < len(text):
				i = text.rfind(" ", 0, i) + 1

			self._text_surfaces[y] = self.font.render(text[:i], True, self.text_color)
			if not self._text_surface:
				self._text_surface = self._text_surfaces[y]

			y += font_height

			text = text[i:]
		return text

	def render_text(self, surface_name: str = 'menu'):
		if not self.chrono_tag_set:
			TimeHandler().add_chrono_tag('dialog_text_wrap', True)
			self.chrono_tag_set = True

		if ControlHandler().is_activated('skip_dialog'):
			self.message_id = -1
			self.next_message()
			return MenuHandler().remove_dialog(self.title)

		if TimeHandler().add_chrono_tag('dialog_text_wrap') < self.text_display_duration:
			self.wrap_text(True)
		else:
			if not self.wrapped_text_finish:
				self.wrap_text()
				self.wrapped_text_finish = True

			arrow_position = list(self.rect.bottomright)
			arrow_position[0] = arrow_position[0] - self.arrow_image.get_rect().width - self.text_margin
			arrow_position[1] = arrow_position[1] - self.arrow_image.get_rect().height - self.text_margin - (abs((TimeHandler().add_chrono_tag('dialog_text_wrap') % 1) - 0.5) * 10)

			GameLoop().get_camera().draw(self.arrow_image, tuple(arrow_position), surface_name)
			if ControlHandler().is_activated('pass_message_dialog') or ControlHandler().is_activated('enter'):
				if self.message_id == len(self.messages) - 1:
					self.message_id = -1
					self.next_message()
					return MenuHandler().remove_dialog(self.title)
				self.next_message()

		for y, line in self._text_surfaces.items():
			GameLoop().get_camera().draw(line, (self.rect.topleft[0] + self.text_margin, y), surface_name)

	def calculate_text_surface(self, width: str):
		pass

	def calculate_text_rect(self):
		pass

	def set_label(self, new_label: str):
		super().set_label(new_label)
		self.chrono_tag_set = False

	def next_message(self):
		self.message_id += 1
		self.wrapped_text_finish = False
		self.set_label(self.messages[self.message_id])
		self.text_display_duration = 0.025 * len(self.messages[self.message_id])
