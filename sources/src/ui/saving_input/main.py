#Projet : Bletchley's Adventure
#Auteurs : Diego GIMENEZ, Maël KEN, Alexis LAROSE, Dimitri NERRAND

from src import TextInput, ButtonActions


class SavingInput(TextInput):
	active_input = None  # Variable statique

	def __init__(self, data: dict):
		super().__init__(data)
		SavingInput.active_input = self  # Définit ce champ comme actif

	def done(self):
		ButtonActions().save_game(self)
