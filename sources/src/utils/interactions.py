# Toutes les classes peuvent être importées depuis ce fichier
from src.classes import GameLoop


def default(self):
	return


# Les interactions à proprement parler, utilisées par Interactable :

def test(self):
	GameLoop().get_player().get_focus().get_position().set_all(-20, -20)


# Les évenements que les NPC ont avec le décor dans leur pattern timeline :

def npc_event_test(self, delta_time):
	if delta_time == 0 :
		first_time = True  # la fonction s'éxecute pour la première fois

	if delta_time <= 2:
		return True  # la fonction sera réappelé à la prochaine frame
	else:
		return False  # la fonction ne sera pas réappelé

interactions = {
	"default": default,
	"test": test,
	"npc_event_test": npc_event_test
}