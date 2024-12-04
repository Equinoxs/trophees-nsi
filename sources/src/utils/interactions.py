# Toutes les classes peuvent être importées depuis ce fichier
from src.classes import GameLoop, TimeHandler


def default(self):
	return


# Les interactions à proprement parler, utilisées par Interactable :

def test(self):
	GameLoop().get_player().get_focus().get_position().set_all(-20, -20)
	GameLoop().get_player().get_focus().play_sound('meow')


# Les évenements que les NPC ont avec le décor dans leur pattern timeline :

def npc_event_test(self, delta_time):
	if delta_time == 0 :
		first_time = True  # la fonction s'éxecute pour la première fois

	if delta_time <= 2:
		return True  # la fonction sera réappelé à la prochaine frame
	else:
		return False  # la fonction ne sera pas réappelée


# Les effets de bords :

# Cet effet fait disparaître le pnj pendant 3 secondes si le joueur s'approche trop près
# Une fois le pnj réapparu au bout des 3 secondes, il ne peut plus redisparaître
def npc_side_effect_test(self):
	time = TimeHandler().add_chrono_tag('first_side_effect')
	effect_made = self.side_effect_data('data_test')
 
	if not effect_made:
		TimeHandler().remove_chrono_tag('first_side_effect')
		if (self.position - GameLoop().get_player().get_focus().get_position()).get_norm() < 50 * GameLoop().get_camera().get_zoom() and not effect_made:
			self.set_z_index(-1)
			self.side_effect_data('data_test', True)

	elif time > 3:
		self.set_z_index(1)
		TimeHandler().remove_chrono_tag('first_side_effect')

interactions = {
	"default": default,
	"test": test,
	"npc_event_test": npc_event_test,
	"npc_side_effect_test": npc_side_effect_test
}