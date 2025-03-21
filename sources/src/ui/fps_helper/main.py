from src import UIElement, TimeHandler, GameLoop

class FPSHelper(UIElement):
	def __init__(self, data: dict):
		super().__init__(data)
		self.fps_timer = 0
		self.nbr_frame = 0

	def update(self):
		if GameLoop().get_menu_handler().get_fps_toggled():
			self.nbr_frame += 1
			self.fps_timer += TimeHandler().get_delta_time()
			if self.fps_timer >= 0.3:
				fps = int(self.nbr_frame * 100 / self.fps_timer) / 100
				self.set_label(f'{fps} fps')
				self.fps_timer = 0
				self.nbr_frame = 0
		else:
			self.set_label('')
