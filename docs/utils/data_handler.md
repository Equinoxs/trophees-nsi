# `DataHandler` - Gestion des données du jeu
## Description
La classe `DataHandler` est responsable de la gestion de la sauvegarde et du chargement des données du jeu. 

Elle permet de charger, sauvegarder et manipuler les informations liées à l'état du jeu, y compris les données de l'environnement, des objets et des joueurs.

Elle centralise l'accès aux différentes ressources comme les sons, les images, les éléments de mission.
Les fonctions `load_XXXXX` et `get_XXXXX_data` sont différentes : la première charge les données depuis le cache avant
d'appeler la deuxième qui charge depuis le stockage si l'objet demandé n'est pas caché.

## Attributs
- `model` : *`dict`* \
  Modèle de données par défaut pour les éléments du jeu.
- `default_save_path` : *`str`* \
  Chemin par défaut vers le fichier de sauvegarde principal.

- `images_data` : *`dict`* **get**
- `sounds_data` : *`dict`* **get**
- `stickers_data` : *`dict`* **get**
- `fonts` : *`dict`* **get**
- `save_allowed` : *`bool`* **get/set**
- `missions_data` : *`dict`* **get**
- `menus_data` : *`dict`* **get**
- `current_save_chrono_tag` : *`str`* \
  Timestamp de la sauvegarde en cours.
- `last_save_player_position` : *`Vector2`* \
  Position du joueur lors de la dernière sauvegarde.
- `current_save` : *`dict`* **get**
## Méthodes
- `__init__()` &rarr; `None` \
  Initialise l'objet, configure les chemins de sauvegarde et initialise les données.

- `is_valid_date(date, format_str = "%Y-%m-%d_%H-%M-%S")` &rarr; `bool` \
  Vérifie si une date donnée est valide selon un format donné. \
  Paramètres :
  * `date` : *`str`*
  * `format_str` : *`str`*

- `get_data_from_last_save(name = None, new_game = False)` &rarr; `dict` \
  Charge les données de la dernière sauvegarde. Si un nom de sauvegarde est donné, charge cette sauvegarde manuelle, 
  sinon charge la sauvegarde automatique la plus récente. \
  Paramètres :
  * `name` : *`str`*
  * `new_game` : *`bool`*

- `normalize_data(data)` &rarr; `dict` \
  Normalise les données en assurant que tous les champs du modèle sont présents, 
  puis transforme les listes en objets `Vector2` ou autres formats appropriés. \
  Paramètre :
  * `data` : *`dict`*

- `reload_game()` &rarr; `None` \
  Recharge l'état du jeu en réinitialisant les éléments nécessaires comme les images, sons ou la position du joueur.

- `load_save(name = None, new_game = False, force = False, reload = False)` &rarr; `dict` \
  Charge les données de la sauvegarde spécifiée ou d'une nouvelle partie si `new_game` est activé et recharge 
  l'état du jeu si `reload` est activé. \
  Paramètres :
  * `name` : *`str`*
  * `new_game` : *`bool`*
  * `force` : *`bool`* \
    Force le rechargement même si la sauvegarde est déjà chargée.
  * `reload` : *`bool`*

- `save_data(original_data, name)` &rarr; `None` \
  Sauvegarde les données du jeu dans un fichier JSON. 
  Si aucun nom n'est fourni, un nom de fichier basé sur la date et l'heure est généré. \
  Paramètres :
  * `original_data` : *`dict`*
  * `name` : *`str`*

- `update_current_save_map()` &rarr; `None` \
  Met à jour la carte actuelle du joueur avec les éléments du jeu.

- `save(self, name: str = None, force: bool = False)` &rarr; `None` \
  Sauvegarde les données actuelles du jeu sous le nom spécifié ou de manière automatique. \
  Paramètres :
  * `name` : *`str`* \
    Le nom de la sauvegarde (si `None`, une sauvegarde automatique est créée).
  * `force` : *`bool`* \
    Force la sauvegarde même si elle n'est pas autorisée.

- `get_save_files(names=False, manual=True, automatic=False)` &rarr; `list` \
  Renvoie une liste des fichiers de sauvegarde disponibles, soit manuels, soit automatiques. \
  Paramètres :
  * `names` : *`bool`* \
    Si `True`, retourne uniquement les noms des fichiers sans l'extension `.json`.
  * `manual` : *`bool`* \
    Si `True`, inclut les sauvegardes manuelles.
  * `automatic` : *`bool`* \
    Si `True`, inclut les sauvegardes automatiques.


- `save_name_valid(name: str)` &rarr; `bool` \
  Vérifie si le nom de la sauvegarde est valide. \
  Paramètre :
  * `name` : *`str`*

- `must_save()` &rarr; `bool` \
  Détermine si une nouvelle sauvegarde doit être effectuée, basé sur la distance parcourue par le joueur et le temps écoulé.

- `get_image_data(dir_name)` &rarr; `tuple(dict, str)` \
  Charge et renvoie les données d'image associées à un nom de répertoire. \
  Paramètre :
  * `dir_name` : *`str`*

- `load_image(dir_name, image_type='', force=False)` &rarr; `tuple(dict, str)` \
  Charge les données d'une image spécifique selon son type et le répertoire. \
  Paramètres :
  * `dir_name` : *`str`*
  * `image_type` : *`str`*
  * `force` : *`bool`*

- `load_wall_images(dir_name)` &rarr; `tuple(dict, dict, dict, dict)` \
  Charge les images pour un mur spécifique, avec les vues de face, latérales et supérieures. \
  Paramètre :
  * `dir_name` : *`str`*

- `load_ui_elements_image(image_name)` &rarr; `str` \
  Charge les images des éléments de l'interface utilisateur. \
  Paramètre :
  * `image_name` : *`str`*

- `get_sticker_data(sticker_name)` &rarr; `tuple(dict, str)` \
  Charge les données d'un sticker mural spécifique. \
  Paramètre :
  * `sticker_name` : *`str`*

- `load_sticker_data(sticker_name, height=None, force=False)` &rarr; `tuple(dict, pygame.Surface)` \
  Charge et redimensionne une image de sticker selon sa hauteur spécifiée. \
  Paramètres :
  * `sticker_name` : *`str`* 
  * `height` : *`int`* 
    La hauteur souhaitée de l'image.
  * `force` : *`bool`* 
    Force le rechargement des données.

- `get_image_surface(image_path, target_height=None)` &rarr; `pygame.Surface` \
  Charge et redimensionne une image à une hauteur cible. \
  Paramètres :
  * `image_path` : *`str`* 
  * `target_height` : *`int`* 
    La hauteur souhaitée de l'image.

- `get_sound_track_data(dir_name)` &rarr; `tuple(dict, dict)` \
  Charge les données associées à un effet sonore spécifique. \
  Paramètre :
  * `dir_name` : *`str`*

- `get_all_sound_tracks_data()` &rarr; `dict` \
  Charge toutes les données des effets sonores disponibles dans le jeu.

- `load_sound(dir_name, sound_name, force=False)` &rarr; `pygame.mixer.Sound` \
  Charge un son spécifique et le renvoie. Peut forcer le rechargement si nécessaire. \
  Paramètres :
  * `dir_name` : `str`
  * `sound_name` : `str`
  * `force` : `bool`

- `load_music(music_name)` &rarr; `tuple(dict, str)` \
  Charge les données et le fichier d'une musique spécifique. \
  Paramètres :
  * `music_name` : `str`

- `get_missions_data()` &rarr; `dict` \
  Charge les données des missions du jeu.

- `load_missions(self, force: bool = False)` &rarr; `dict` \
  Charge et renvoie les données des missions. \
  Paramètres :
  * `force` : `bool`

- `get_menus_data()` &rarr; `dict` \
  Charge les données des menus du jeu.

- `load_menus(force=False)` &rarr; `dict` \
  Charge et renvoie les données des menus du jeu.

- `get_font_data(font_name, font_size)` &rarr; `pygame.font.Font` \
  Récupère un objet de police Pygame à partir d'un nom de police et d'une taille donnés. \
  Paramètres :
  * `font_name` : `str`
  * `font_size` : `int`

- `load_font(font_name, font_size, force=False)` &rarr; `pygame.font.Font` \
  Charge et renvoie une police de caractères. \
  Paramètres :
  * `font_name` : `str`
  * `font_size` : `int`
  * `force` : `bool`

- `list_to_vector2(list2)` &rarr; `Vector2` \
  Convertit une liste de deux éléments en un objet `Vector2`. \
  Paramètre :
  * `list2` : `list`

- `list_transform(list2)` &rarr; `list` \
  Transforme une liste contenant des listes de deux éléments en une liste contenant des `Vector2`. \
  Paramètre :
  * `list2` : `list`

## Classe associée

- `JSONEncoder` - Encodeur JSON personnalisé pour sérialiser des objets `Vector2`.
