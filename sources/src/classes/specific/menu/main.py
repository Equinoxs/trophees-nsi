from src.classes import UIElement, Button, MiniMap


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
		self.ui_elements.append(element)
		return element

	def delete_element(self, element: UIElement):
		del self.ui_elements[self.ui_elements.index(element)]

	def load_ui_elements(self, ui_elements_data):
		for ui_element_data in ui_elements_data:
			self.add_element(ui_element_data)

	def update(self):
		for ui_element in self.ui_elements:
			ui_element.update()

	def render(self):
		for element in self.ui_elements:
			element.render()
