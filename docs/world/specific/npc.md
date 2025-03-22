# `NPC` - Les personnages non-joueur

## Description

Cette classe est nécessaire afin de donner de la vie au jeu.
Grâce à elle, le monde est rempli de personnages fascinants à qui parler.

Les personnages peuvent se déplacer vers un objectif et effectuer une série de tâches pour leur donner une sorte d'animation.

> ```json
> {
> 	"type": "NPC",
> 	"name": "house_proprietary",
> 	"pattern_timeline": [[650, 1300], "npc_event_test", [700, 1110]],
> 	"pattern_type": "back_and_forth",
> 	"position": [670, 1200],
> 	"image_path": "albert",
> 	"mission": "mission_test",
> 	"authorized_sound_tracks": ["footsteps", "voices"],
> 	"side_effects": ["visit_player"],
> 	"sound": "hey"
> }
> ```
> Exemple exhaustif de dictionnaire d'initialisation d'un PNJ.

Les informations nécessaires à ces parcours prédéfinis sont stockées dans les propriétés `"pattern_timeline"` et `"pattern_type"`.

Dans `"pattern_timeline"`, lorsqu'il y a un couple de point, cela signifie un déplacement, lorsqu'il y a une chaîne de caractère, le PNJ effectue l'action spécifiée dans [`PatternEvents`](pattern_events.md).

## Attributs
- `initial_position` : *`Vector2`* \
  Copie de la position initiale du PNJ.
- `sprint` : *`Vector2`* \
  Copie de la position initiale du PNJ.
- `is_player` : *`Vector2`* \
  Copie de la position initiale du PNJ.
- `initial_position` : *`Vector2`* \
  Copie de la position initiale du PNJ.

## Méthodes
- `__init__(map_name)` &rarr; `None`
  Initialise ses attributs, charge les éléments de la carte, et fusionne tous les [`GroundSurface`](ground_surface.md) afin d'éviter de multiples collages pour rien.
  Paramètre :
  * `map_name` : *`str`*
  Le nom de la carte à charger

- `sort_once()` &rarr; `bool`
  Trie les éléments de la map en itérant qu'une seule fois dessus, retourne `True` s'il y a eu des permutations et `False` sinon.

- `sort_elements()` &rarr; `None`
  Trie les éléments du jeu en fonction de leur superposition mutuelle, appelle plusieurs fois la méthode ci-dessus jusqu'à ce qu'il n'y ait plus de permutation.

- `search_by_name(object_name)` &rarr; `MapElement | None`
  Recherche un élément en fonction de son nom et le retourne si trouvé, `None` sinon.
  Paramètre :
  * `object_name` : *`str`*
  Le nom de l'objet à rechercher

- `add(element)` &rarr; `None`
  Ajoute simplement un élément à la map.
  Paramètre :
  * `element` : *`MapElement`*
  La référence de l'objet à ajouter

- `remove_wall(wall_name)` &rarr; `None`
  Enlève un [`Wall`](wall.md) de la carte.
  Paramètre :
  * `wall_name` : *`str`*
  Le nom du mur à enlever

- `remove(element_to_remove)` &rarr; `int | None`
  Enlève l'élément spécifié de la carte, retourne le même élément s'il a été trouvé.
  Paramètre :
  * `element_to_remove` : *`MapElement`*

- `throw_event(event)` &rarr; `None`
  Propage un évènement au sein de ses éléments.
  Paramètre :
  * `event` : *`str | dict`*
  L'évènement à propager.

- `load_elements_from(map_name)` &rarr; `None`
  Charge les éléments depuis une map spécifié
  Paramètre :
  * `map_name` : *`str`*
  Le nom de la carte à charger.

- `add_element(element_data)` &rarr; `None`
  Ajoute un objet à la map selon ses données.
  Paramètre :
  * `element_data` : *`dict`*
  Le dictionnaire d'initialisation de l'objet à ajouter.

- `add_element_ref(element_ref, index)` &rarr; `None`
  Ajoute un objet à la map selon sa référence.
  Paramètre :
  * `element_ref` : *`MapElement`*
  La référence de l'élément à ajouter.
  * `index = None` : *`int | None`*
  L'index du tableau par lequel il faut insérer l'élément.

- `get_index_of(element_ref)` &rarr; `int | None`
  Retourne l'index de l'élément recherché s'il est trouvé.
  Paramètre :
  * `element_ref` : *`MapElement`*
  La référence de l'élément à chercher.

- `remove_element(element_ref)` &rarr; `None`
  Enlève l'élément spécifié de la carte selon une différente méthode que `remove(element_to_remove)`.
  Paramètre :
  * `element_ref` : *`MapElement`*
  L'élément à retirer.

- `which_surface(position)` &rarr; `str | None`
  Retourne le `ground_type` du [`GroundSurface`](ground_surface.md) sur lequel est la position indiquée.
  Paramètre :
  * `position` : *`Vector2`*
  La position (du joueur en général).

- `find_closest_item(position)` &rarr; `tuple[InventoryItem, Table | None]`
  Retourne l'[`InventoryItem`](inventory_item.md) le plus proche de la position indiquée, utile pour en prendre un avec soi.
  Paramètre :
  * `position` : *`Vector2`*
  La position (du joueur en général).

- `find_closest_item_place(position)` &rarr; `dict`
  Retourne l'emplacement d'item sur une [`Table`](table.md) le plus proche de la position indiquée.
  Paramètre :
  * `position` : *`Vector2`*
  La position (du joueur en général).

- `update()` &rarr; `None`
  Update ses éléments si le jeu n'est pas en pause et trie ses éléments à chaque frame.
