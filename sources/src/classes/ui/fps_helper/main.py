from src.classes import UIElement, TimeHandler

class FPSHelper(UIElement):
	def __init__(self, data: dict):
		super().__init__(data)
		self.time_handler = TimeHandler()
		self.time_handler.add_chrono_tag("fps_timer", reset=True)
		self.toggled = True

	def update(self):
		if self.time_handler.get_delta_time() == 0:
			return
		
		if self.toggled:
			elapsed_time = self.time_handler.add_chrono_tag("fps_timer")
			if elapsed_time >= 0.3:
				fps = int(100 / self.time_handler.get_delta_time()) / 100
				self.set_label(f"{fps} fps")
				self.time_handler.add_chrono_tag("fps_timer", reset=True)
		else:
			self.set_label("")

	def render(self):
		super().render()
