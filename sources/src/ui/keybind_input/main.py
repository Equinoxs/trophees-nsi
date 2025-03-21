from src import TextInput, ControlHandler


class KeybindInput(TextInput):
	def __init__(self, data: dict):
		super().__init__(data)
		self.intercept = 'keys'
		self.event_key = None
		self.event_name = data.get('event_name', '')
		self.max_event_key = 1

	def done(self):
		if len(self.event_keys) > 0:
			ControlHandler().set_keybind(self.event_name, self.last_event_key)
