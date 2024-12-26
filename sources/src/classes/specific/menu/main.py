from src.classes import UIElement, Button


class Menu:
	def __init__(self, menu_data):
		self.ui_elements = []
		self.load_ui_elements(menu_data)

	def load_ui_elements(self, ui_elements_data):
		for ui_element_data in ui_elements_data:
			match ui_element_data['type']:
				case 'UIElement':
					self.ui_elements.append(UIElement(ui_element_data))
				case 'Button':
					self.ui_elements.append(Button(ui_element_data))

	def update(self):
		for ui_element in self.ui_elements:
			ui_element.update()

	def render(self):
		for element in self.ui_elements:
			element.render()
