from src import TextInput, ButtonActions


class SavingInput(TextInput):
	active_input = None  # Variable statique

	def __init__(self, data: dict):
		super().__init__(data)
		SavingInput.active_input = self  # Définit ce champ comme actif

	def done(self):
		ButtonActions().save_game(self)
