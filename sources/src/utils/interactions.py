from src.classes import SaveHandler
def test(self, player):
    print(type(self))
    player.get_focus().get_position().set_all(-20, -20)
    _, snd_path = SaveHandler().load_sound("nathan", "goose")
    if not self.is_sound_loaded(snd_path):
        self.load_sound(snd_path)
    if not self.get_busy(snd_path):
        # print("snd played!")
        self.play_sound(snd_path)

interactions = {
	"test": test
}