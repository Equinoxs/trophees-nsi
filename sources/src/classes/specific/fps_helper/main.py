from src.classes import UIElement, TimeHandler


class FPSHelper(UIElement):
	def __init__(self, data: dict):
		super().__init__(data)

	def update(self):
		if TimeHandler().get_delta_time() == 0:
			fps = 60
		else:
			fps = int(100 / TimeHandler().get_delta_time()) / 100
		self.set_label(str(fps) + ' fps')

	def render(self):
		super().render()