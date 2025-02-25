from src.classes import TextInput, ControlHandler, ButtonActions

class SavingInput(TextInput):
    active_input = None  # Variable statique

    def __init__(self, data: dict):
        super().__init__(data)
        self.text = data.get("default_text", "")
        SavingInput.active_input = self  # Définit ce champ comme actif

    def done2(self):
        ButtonActions().save_game()