import pygame

from src.classes import UIElement, Button, MiniMap, Marker, FPSHelper, TextInput


class Menu:
	def __init__(self, menu_data):
		self.ui_elements = []
		self.load_ui_elements(menu_data)

	def add_element(self, element_data: dict):
		match element_data['type']:
			case 'UIElement':
				element = UIElement(element_data)
			case 'Button':
				element = Button(element_data)
			case 'MiniMap':
				element = MiniMap(element_data)
			case 'Marker':
				element = Marker(element_data)
			case 'FPSHelper':
				element = FPSHelper(element_data)
			case 'TextInput':
				element = TextInput(element_data)
		self.ui_elements.append(element)
		return element

	def delete_element(self, element: UIElement):
		del self.ui_elements[self.ui_elements.index(element)]

	def load_ui_elements(self, ui_elements_data):
		for ui_element_data in ui_elements_data:
			self.add_element(ui_element_data)

	def update(self):
		cursor_pointer = False
		for ui_element in self.ui_elements:
			if ui_element.update():
				cursor_pointer = True
		if cursor_pointer:
			pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
		else:
			pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

	def render(self):
		for element in self.ui_elements:
			element.render()
