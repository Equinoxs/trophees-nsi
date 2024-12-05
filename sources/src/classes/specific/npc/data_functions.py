from src.classes import GameLoop

def npc_event_test(self, delta_time):
	if delta_time == 0 :
		first_time = True  # la fonction s'éxecute pour la première fois

	if delta_time <= 2:
		return True  # la fonction sera réappelé à la prochaine frame
	else:
		return False  # la fonction ne sera pas réappelée


pattern_events = {
	"npc_event_test": npc_event_test
}