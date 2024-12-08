from src.classes import UIElement, ButtonActions, ControlHandler


class Button(UIElement):
	def __init__(self, data):
		UIElement.__init__(self, data)
		self.action_name = data['action']

	def update(self):
		UIElement.update(self)
		if ControlHandler().is_clicked(self):
			ButtonActions().do(self.action_name)
