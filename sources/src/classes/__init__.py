# Constantes
DEBUG = False
SAVE = False
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800

# Il est important de mettre les classes dans l'ordre d'importation.
# ex : si A importe B, alors on devra importer B avant A dans ce fichier
# afin que B soit complètement initialisé quand A importera B

# Classes n'important personne (sauf GameLoop)
from .utils.game_loop.main import GameLoop
from .utils.log_handler.main import LogHandler
from .utils.time_handler.main import TimeHandler
from .basics.vector_2.main import Vector2
from .utils.player.main import Player

# MissionHandler importe Mission
from .basics.mission.missions import Missions
from .basics.mission.main import Mission
from .utils.mission_handler.main import MissionHandler

# DataHandler importe utils/interactions qui importe GameLoop
from .utils.data_handler.main import DataHandler

# ControlHandler importe DataHandler
from .utils.control_handler.main import ControlHandler

# MenuHandler importe DataHandler et Menu importe Button qui importe ButtonActions et UIElement
from .basics.ui_element.main import UIElement
from .specific.marker.main import Marker
from .specific.fps_helper.main import FPSHelper
from .specific.button.actions import ButtonActions
from .specific.button.main import Button

# Objets enfant de Button
from .specific.mini_map.main import MiniMap

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
from .basics.side_effects_manager.side_effects import SideEffects
from .basics.side_effects_manager.main import SideEffectsManager
from .basics.movable.main import Movable
from .basics.collider.main import Collider
from .basics.interactable.interactions import Interactions
from .basics.interactable.main import Interactable
from .basics.map_object.main import MapObject

# Objets enfant de MapObject :
from .basics.pillar_object.main import PillarObject
from .basics.base_object.main import BaseObject
from .basics.ridge_object.main import RidgeObject
from .specific.npc.pattern_events import PatternEvents
from .specific.npc.main import NPC
from .specific.tree.main import Tree
from .specific.wall_segment.main import WallSegment

# Wall importe WallSegment
from .specific.wall.main import Wall

# Map importe NPC, Wall et donc tout
from .specific.map.main import Map
