# Constantes
DEBUG = True
SAVE = False

# Il est important de mettre les classes dans l'ordre d'importation.
# ex : si A importe B, alors on devra importer B avant A dans ce fichier
# afin que B soit complètement initialisé quand A importera B

# Classes n'important personne
from .utils.game_loop.main import GameLoop
from .utils.log_handler.main import LogHandler
from .utils.time_handler.main import TimeHandler
from .basics.vector_2.main import Vector2
from .basics.ui_element.main import UIElement
from .utils.player.main import Player

# MissionHandler importe Mission
from .basics.mission.main import Mission
from .utils.mission_handler.main import MissionHandler

# DataHandler importe utils/interactions qui importe GameLoop
from .basics.interactable.data_functions import interactions
from .specific.npc.data_functions import pattern_events
from .basics.side_effects_manager.data_functions import side_effects
from .basics.mission.data_functions import missions
from .utils.data_handler.main import DataHandler

# ControlHandler importe DataHandler
from .utils.control_handler.main import ControlHandler

# MenuHandler importe DataHandler et Menu qui importe Button qui importe ButtonActions
from .specific.button.actions import ButtonActions
from .specific.button.main import Button
from .specific.menu.main import Menu
from .utils.menu_handler.main import MenuHandler

# Camera importe Player et SoundMixer
from .utils.sound_mixer.main import SoundMixer
from .utils.camera.main import Camera

# SoundMaker importe SoundTrack qui importe SoundMixer
from .utils.sound_track.main import SoundTrack
from .basics.sound_maker.main import SoundMaker

# MapElement importe Animatable, Sprite et SoundMaker
from .basics.sprite.main import Sprite
from .basics.animatable.main import Animatable
from .basics.map_element.main import MapElement
from .specific.ground_surface.main import GroundSurface

# MapObject importe MapElement, Movable, Collider et Interactable
from .basics.side_effects_manager.main import SideEffectsManager
from .basics.movable.main import Movable
from .basics.collider.main import Collider
from .basics.interactable.main import Interactable
from .basics.map_object.main import MapObject

# Objets enfants de MapObject :
from .specific.npc.main import NPC

# Map importe NPC
from .specific.map.main import Map
