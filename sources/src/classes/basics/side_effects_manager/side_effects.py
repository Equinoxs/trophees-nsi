from src.classes import GameLoop, TimeHandler, LogHandler


class SideEffects:
	_instance = None

	# singleton
	def __new__(cls, *args, **kwargs):
		if not isinstance(cls._instance, cls):
			cls._instance = object.__new__(cls, *args, **kwargs)
		return cls._instance

	def __init__(self):
		pass

	# Cet effet fait disparaître le pnj pendant 3 secondes si le joueur s'approche trop près
	# Une fois le pnj réapparu au bout des 3 secondes, il ne peut plus redisparaître
	def npc_side_effect_test(_, host):
		if GameLoop().get_player().get_focus() == host:
			return  # On ne veut pas que cet effet s'applique si on est le focus du Player

		effect_made = host.side_effect_data('npc_side_effect_test_effect_made')
		cleared = host.side_effect_data('npc_side_effect_test_cleared')
		if not cleared:
			time = TimeHandler().add_chrono_tag('first_side_effect')

		if not effect_made:
			TimeHandler().remove_chrono_tag('first_side_effect')
			if (host.position - GameLoop().get_player().get_focus().get_position()).get_norm() < 50 * GameLoop().get_camera().get_zoom() and not effect_made:
				host.set_z_index(-1)
				LogHandler().add(f'{host.get_name()} * switch Z index to -1')
				host.side_effect_data('npc_side_effect_test_effect_made', True)

		elif not cleared and time > 3:
			LogHandler().add(f'{host.get_name()} * switch to the previous Z index')
			host.set_z_index_prev()
			TimeHandler().remove_chrono_tag('first_side_effect')
			host.side_effect_data('npc_side_effect_test_cleared', True)

	def visit_player(_, host):
		distance = host.get_position().distance_to(GameLoop().get_player().get_focus().get_position())
		out = host.side_effect_data('visit_player_out')
		if distance < 80:
			if out:
				host.play_sound('okay')
			host.side_effect_data('visit_player_out', False)
			TimeHandler().remove_chrono_tag('visit_player')
			host.set_following_pattern(False)
			host.set_objective(GameLoop().get_player().get_focus().get_position())
			host.move_npc_to_objective()
			if distance < 30:
				host.stop_moving()
		else:
			if not out:
				host.side_effect_data('visit_player_out', True)
				host.set_following_pattern(True)
				host.set_objective(None)


	def do(self, side_effect_name: str, host):
		match side_effect_name:
			case 'npc_side_effect_test':
				self.npc_side_effect_test(host)
			case 'visit_player':
				self.visit_player(host)