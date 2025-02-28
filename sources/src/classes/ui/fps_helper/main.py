from src.classes import UIElement, TimeHandler, GameLoop

class FPSHelper(UIElement):
	def __init__(self, data: dict):
		super().__init__(data)
		self.time_handler = TimeHandler()
		self.time_handler.add_chrono_tag("fps_timer", reset=True)
		self.nbr_frame = 0

	def update(self):
		self.nbr_frame += 1
		if self.time_handler.get_delta_time() == 0:
			return
		
		if GameLoop().get_menu_handler().get_fps_toggled():
			elapsed_time = self.time_handler.add_chrono_tag("fps_timer")
			if elapsed_time >= 0.3:
				fps = int(self.nbr_frame * 100 / elapsed_time) / 100
				self.set_label(f"{fps} fps")
				self.time_handler.add_chrono_tag("fps_timer", reset=True)
				self.nbr_frame = 0
		else:
			self.set_label("")

	def render(self):
		super().render()
