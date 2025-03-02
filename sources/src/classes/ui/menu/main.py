import pygame

from src.classes import UIElement
from src import classes

class Menu:
	def __init__(self, menu_data):
		self.ui_elements = []
		self.load_ui_elements(menu_data)

	def get_elements(self, event=None):
		if event:
			return [element for element in self.ui_elements if getattr(element, 'event_name', None) == event]
		return self.ui_elements

	def get_element_by_id(self, id: str):
		for element in self.ui_elements:
			if element.get_id() == id:
				return element
		return None

	def add_element_ref(self, element_ref):
		self.ui_elements.append(element_ref)

	def add_element(self, element_data: dict):
		element_class = getattr(classes, element_data['type'], None)
		if element_class is None:
			return
		element = element_class(element_data)

		self.ui_elements.append(element)
		return element

	def delete_element_by_id(self, id: str):
		element = self.get_element_by_id(id)
		if element is not None:
			self.delete_element(element)

	def delete_element(self, element: UIElement):
		if element is not None and element in self.ui_elements:
			del self.ui_elements[self.ui_elements.index(element)]

	def load_ui_elements(self, ui_elements_data):
		for ui_element_data in ui_elements_data:
			self.add_element(ui_element_data)

	def update(self):
		cursor_pointer = False
		for i in range(len(self.ui_elements) - 1, -1, -1):
			if self.ui_elements[i].update():
				cursor_pointer = True
		if cursor_pointer:
			pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
		else:
			pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

	def render(self):
		for element in self.ui_elements:
			element.render()
