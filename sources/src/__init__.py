#Projet : Bletchley's Adventure
#Auteurs : Diego GIMENEZ, Maël KEN, Alexis LAROSE, Dimitri NERRAND

# Constantes
DEBUG = False  # Active le mode développement si DEBUG est à True
SAVE = True
SCREEN_WIDTH = 1280  # Ce jeu a été créé en partant du principe que ces valeurs restent inchangées
SCREEN_HEIGHT = 800  # Merci de ne pas les modifier au risque de ne pas apprécier l'expérience de jeu

# Il est important de mettre les classes dans l'ordre d'importation.
# ex : si A importe B, alors on devra importer B avant A dans ce fichier
# afin que B soit complètement initialisé quand A importera B

# Classes n'important personne (sauf GameLoop)
from .utils.game_loop.main import GameLoop
from .utils.log_handler.main import LogHandler
from .utils.time_handler.main import TimeHandler
from .utils.vector_2.main import Vector2
from .utils.player.main import Player

# MissionHandler importe Mission
from .world.basics.mission.missions import Missions
from .world.basics.mission.main import Mission
from .utils.mission_handler.main import MissionHandler

# DataHandler importe utils/interactions qui importe GameLoop
from .utils.data_handler.main import DataHandler

# SoundMixer importe DataHandler
from .utils.sound_mixer.main import SoundMixer

# ControlHandler importe DataHandler
from .utils.control_handler.main import ControlHandler

# MenuHandler importe DataHandler et Menu importe Button qui importe ButtonActions et UIElement
from .ui.ui_element.main import UIElement
from .ui.marker.main import Marker
from .ui.fps_helper.main import FPSHelper
from .ui.button.actions import ButtonActions
from .ui.button.main import Button
from .ui.text_input.main import TextInput
from .ui.keybind_input.main import KeybindInput
from .ui.saving_input.main import SavingInput
from .ui.slider.actions import SliderActions
from .ui.slider.main import Slider
from .ui.line.main import Line

# Objets enfant de Button
from .ui.mini_map.main import MiniMap

from .ui.menu.main import Menu
from .utils.menu_handler.main import MenuHandler
from .ui.dialog.main import Dialog

# Camera importe Player et SoundMixer
from .utils.camera.main import Camera

# SoundMaker importe SoundTrack qui importe SoundMixer
from .utils.sound_track.main import SoundTrack
from .world.basics.sound_maker.main import SoundMaker

# MapElement importe Animatable, Sprite et SoundMaker
from .world.basics.sprite.main import Sprite
from .world.basics.animatable.main import Animatable
from .world.basics.map_element.main import MapElement
from .world.specific.ground_surface.main import GroundSurface

# MapObject importe MapElement, Movable, Collider et Interactable
from .world.basics.side_effects_manager.side_effects import SideEffects
from .world.basics.side_effects_manager.main import SideEffectsManager
from .world.basics.movable.main import Movable
from .world.basics.collider.main import Collider
from .world.basics.interactable.interactions import Interactions
from .world.basics.interactable.main import Interactable
from .world.basics.map_object.main import MapObject

# Objets enfant de MapObject :
from .world.basics.pillar_object.main import PillarObject
from .world.basics.base_object.main import BaseObject
from .world.basics.ridge_object.main import RidgeObject
from .world.specific.npc.pattern_events import PatternEvents
from .world.specific.inventory_item.main import InventoryItem
from .world.specific.npc.main import NPC
from .world.specific.tree.main import Tree
from .world.specific.wall_segment.main import WallSegment
from .world.specific.door.main import Door
from .world.specific.building.main import Building
from .world.specific.interior.main import Interior
from .world.specific.furniture.main import Furniture
from .world.specific.table.main import Table
from .world.specific.natural_object.main import NaturalObject
# Wall importe WallSegment
from .world.specific.wall.main import Wall

# Map importe NPC, Wall et donc tout
from .world.specific.map.main import Map
