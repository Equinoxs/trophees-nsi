class PatternEvents:
	_instance = None

	# singleton
	def __new__(cls, *args, **kwargs):
		if not isinstance(cls._instance, cls):
			cls._instance = object.__new__(cls, *args, **kwargs)
		return cls._instance

	def __init__(self):
		pass

	def npc_event_test(_, host, delta_time):
		if delta_time == 0 :
			first_time = True  # la fonction s'éxecute pour la première fois

		if delta_time <= 2:
			return True  # la fonction sera réappelé à la prochaine frame
		else:
			return False  # la fonction ne sera pas réappelée

	def do(self, pattern_event_name: str, host, delta_time):
		match pattern_event_name:
			case 'npc_event_test':
				return self.npc_event_test(host, delta_time)
