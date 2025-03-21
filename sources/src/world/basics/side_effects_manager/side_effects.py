from src import GameLoop, TimeHandler, LogHandler, Player


class SideEffects:
	_instance = None

	# singleton
	def __new__(cls, *args, **kwargs):
		if not isinstance(cls._instance, cls):
			cls._instance = object.__new__(cls, *args, **kwargs)
		return cls._instance

	def __init__(self):
		pass

	def npc_side_effect_test(_, host):
		if GameLoop().get_player().get_focus() == host:
			return

		effect_made = host.side_effect_data('npc_side_effect_test_effect_made')
		cleared = host.side_effect_data('npc_side_effect_test_cleared')
		if not cleared:
			time = TimeHandler().add_chrono_tag('first_side_effect')

		if not effect_made:
			TimeHandler().remove_chrono_tag('first_side_effect')
			if (host.position - GameLoop().get_player().get_focus().get_position()).get_norm() < 50 * GameLoop().get_camera().get_zoom():
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
		sound = host.get_sound()

		if distance < 80:
			if out and sound:
				host.play_sound(sound)
			host.side_effect_data('visit_player_out', False)
			TimeHandler().remove_chrono_tag('visit_player')
			host.set_following_pattern(False)
			host.set_objective(GameLoop().get_player().get_focus().get_position())
			host.move_npc_to_objective()
			if distance < 30:
				host.set_objective(None)
		elif not out:
			host.side_effect_data('visit_player_out', True)
			host.set_following_pattern(True)
			host.set_objective(None)
			host.resume_moving()

	def fix_when_player(_, host):
		if host.side_effect_data('fix_when_player') is None:
			host.side_effect_data('fix_when_player', host.get_must_move())
		if GameLoop().get_player().get_focus().get_position().distance_to(host.get_position()) < 50:
			if host.get_must_move():
				host.stop_moving()
				host.side_effect_data('fix_when_player', False)
		elif not host.get_must_move() and not host.side_effect_data('fix_when_player'):
			host.resume_moving()
			host.side_effect_data('fix_when_player', True)



	# --- RÉSERVÉ À CERTAINS PERSONNAGES POUR LEUR PERMETTRE D'AVOIR PLUSIEURS MISSIONS ---


	def handle_alastair_denniston(_, denniston):
		if Player().get_level() == 3 and denniston.get_mission() is None:
			denniston.set_mission_name('act2_upgrade')
		elif Player().get_level() == 7 and denniston.get_mission() is None:
			denniston.set_mission_name('act3_upgrade')
		elif Player().get_level() == 9 and denniston.get_mission() is None:
			denniston.set_mission_name('final')

	def handle_alan_turing(_, turing):
		if turing.get_mission() is None:
			turing.set_mission_name('decrypt_enigma')
		if Player().get_level() >= 10 and not turing.get_killed():
			turing.kill()

	def handle_hugh_alexander(_, alexander):
		if alexander.get_mission() is None:
			alexander.set_mission_name('bombes_manipulation')



	def do(self, side_effect_name: str, host):
		side_effect_method = getattr(self, side_effect_name, None)
		if side_effect_method is None:
			return
		side_effect_method(host)
