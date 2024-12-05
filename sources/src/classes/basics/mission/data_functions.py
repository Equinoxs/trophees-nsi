from src.classes import GameLoop, TimeHandler, Player


def objective1():
    time = TimeHandler().add_chrono_tag('objective1')
    if time == 0:
        Player().get_focus().play_sound('goose')
    if time > 2:
        TimeHandler().remove_chrono_tag('objective1')
        return False
    else:
        return True

mission_test = [objective1]


missions = {
    'mission_test': mission_test
}