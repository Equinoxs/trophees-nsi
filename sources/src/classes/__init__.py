# Il est important de mettre les classes dans l'ordre d'importation.
# ex : si A importe B, alors on devra importer B avant A dans ce fichier
# afin que B soit complètement initialisé quand A importera B

# Classes n'important personne
from .basics.vector_2.main import Vector2
from .utils.save_handler.main import SaveHandler
from .utils.time_handler.main import TimeHandler
from .utils.player.main import Player

# GameLoop importe Camera qui importe Player
from .utils.camera.main import Camera
from .utils.game_loop.main import GameLoop

# ControlHandler import SaveHandler
from .utils.control_handler.main import ControlHandler

# SoundMaker importe SoundTrack qui importe SoundMixer
from .utils.sound_mixer.main import SoundMixer
from .utils.sound_track.main import SoundTrack
from .basics.sound_maker.main import SoundMaker

# MapElement importe Animatable, Sprite et SoundMaker
from .basics.sprite.main import Sprite
from .basics.animatable.main import Animatable
from .basics.map_element.main import MapElement

# MapObject importe MapElement, Movable, Collider et Interactable
from .basics.movable.main import Movable
from .basics.collider.main import Collider
from .basics.interactable.main import Interactable
from .basics.map_object.main import MapObject

# Objets enfants de MapObject :
from .specific.npc.main import NPC

# Map importe NPC
from .specific.map.main import Map



# Classes restantes :

# from .specific.tree.main import Tree
# from .specific.mini_map.main import MiniMap
# from .specific.button.main import Button
# from .basics.ui_element.main import UIElement