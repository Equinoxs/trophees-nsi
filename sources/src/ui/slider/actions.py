#Projet : Bletchley's Adventure
#Auteurs : Diego GIMENEZ, Maël KEN, Alexis LAROSE, Dimitri NERRAND

from src import LogHandler, SoundMixer


class SliderActions:
    _instance = None

    # Singleton
    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        pass

    def set_music_volume(self, value):
        sound_mixer = SoundMixer()
        normalized_value = max(0.0, min(value / 100.0, 1.0))

        sound_mixer.set_music_coefficient(normalized_value)
        LogHandler().add(f"Music volume set to {normalized_value:.2f}")
    
    def set_sound_volume(self, value):
        sound_mixer = SoundMixer()
        normalized_value = max(0.0, min(value / 100.0, 1.0))

        sound_mixer.set_sound_coefficient(normalized_value)
        LogHandler().add(f"Sound volume set to {normalized_value:.2f}")

    def do(self, action_name, value):
        LogHandler().add(f'Slider action "{action_name}" activated with value {value}')
        match action_name:
            case 'set_music_volume':
                self.set_music_volume(value)
            case 'set_sound_volume':
                self.set_sound_volume(value)
            case _:   
                LogHandler().add(f'Unknown slider action: {action_name}')
