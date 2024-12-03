# Toutes les classes peuvent être importées depuis ce fichier
from src.classes import GameLoop, TimeHandler


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
		return False  # la fonction ne sera pas réappelée


# Les effets de bords :

# Cet effet fait disparaître le pnj pendant 5 secondes si le joueur s'approche trop près
# Une fois le pnj réapparu au bout des 5 secondes, il ne peut plus redisparaître
def npc_side_effect_test(self):
	time = TimeHandler().add_chrono_tag('first_side_effect')
	effect_made = self.side_effect_data('data_test')
	if (self.position - GameLoop().get_player().get_focus().get_position()).get_norm() < 50 * GameLoop().get_camera().get_zoom() and effect_made != True:
		self.set_z_index(-1)
	if time > 4:
		TimeHandler().remove_chrono_tag('first_side_effect')
		self.side_effect_data('data_test', True)
		self.set_z_index(1)

interactions = {
	"default": default,
	"test": test,
	"npc_event_test": npc_event_test,
	"npc_side_effect_test": npc_side_effect_test
}