# `Map` - La carte du jeu

## Description

Cette classe a pour rôle de gérer tous les objets du jeu.

`Map` s'occupe de l'initialisation des différents objets de la carte en fonction de son `type` qui correspond à la classe à instancier, une classe qui est forcément "spécifique".

Il faut donc les trier pour savoir qui est rendu au dessus de qui (dans une logique de fausse perspective), de l'optimisation est préférable.

## Attributs
- `elements` : *`list[MapElement]`* **get** \
  les éléments de la carte.
- `walls` : *`list[WallSegment]`* \
  La liste des différents murs du jeu, car ils ne doivent pas être sauvegardés tels quels.
- `name` : *`str`* **get** \
  Le nom de la map.
- `allow_map_change` : *`bool`* **get / set** \
  Indique si le changement de map est autorisé, utile pour certaines missions par exemple.

## Méthodes
- `__init__(map_name)` &rarr; `None` \
  Initialise ses attributs, charge les éléments de la carte, et fusionne tous les [`GroundSurface`](ground_surface.md) afin d'éviter de multiples collages pour rien. \
  Paramètre :
  * `map_name` : *`str`* \
  Le nom de la carte à charger

- `sort_once()` &rarr; `bool` \
  Trie les éléments de la map en n'itérant qu'une seule fois dessus, retourne *`True`* s'il y a eu des permutations et *`False`* sinon.

- `sort_elements()` &rarr; `None` \
  Trie les éléments du jeu en fonction de leurs superpositions mutuelles, appelle plusieurs fois la méthode ci-dessus jusqu'à ce qu'il n'y ait plus de permutation.

- `search_by_name(object_name)` &rarr; `MapElement | None` \
  Recherche un élément en fonction de son nom et le retourne si trouvé, `None` sinon. \
  Paramètre :
  * `object_name` : *`str`* \
  Le nom de l'objet à rechercher

- `add(element)` &rarr; `None` \
  Ajoute simplement un élément à la map. \
  Paramètre :
  * `element` : *`MapElement`* \
  La référence de l'objet à ajouter

- `remove_wall(wall_name)` &rarr; `None` \
  Enlève un [`Wall`](wall.md) de la carte. \
  Paramètre :
  * `wall_name` : *`str`* \
  Le nom du mur à enlever

- `remove(element_to_remove)` &rarr; `int | None` \
  Enlève l'élément spécifié de la carte, retourne le même élément s'il a été trouvé. \
  Paramètre :
  * `element_to_remove` : *`MapElement`*

- `throw_event(event)` &rarr; `None` \
  Propage un évènement au sein de ses éléments. \
  Paramètre :
  * `event` : *`str | dict`* \
  L'évènement à propager.

- `load_elements_from(map_name)` &rarr; `None` \
  Charge les éléments depuis une map spécifié \
  Paramètre :
  * `map_name` : *`str`* \
  Le nom de la carte à charger.

- `add_element(element_data)` &rarr; `None` \
  Ajoute un objet à la map selon ses données. \
  Paramètre :
  * `element_data` : *`dict`* \
  Le dictionnaire d'initialisation de l'objet à ajouter.

- `add_element_ref(element_ref, index)` &rarr; `None` \
  Ajoute un objet à la map selon sa référence. \
  Paramètre :
  * `element_ref` : *`MapElement`* \
  La référence de l'élément à ajouter.
  * `index = None` : *`int | None`*
  L'index du tableau par lequel il faut insérer l'élément.

- `get_index_of(element_ref)` &rarr; `int | None` \
  Retourne l'index de l'élément recherché s'il est trouvé. \
  Paramètre :
  * `element_ref` : *`MapElement`* \
  La référence de l'élément à chercher.

- `remove_element(element_ref)` &rarr; `None` \
  Enlève l'élément spécifié de la carte selon une différente méthode que `remove(element_to_remove)`. \
  Paramètre :
  * `element_ref` : *`MapElement`* \
  L'élément à retirer.

- `which_surface(position)` &rarr; `str | None` \
  Retourne le `ground_type` du [`GroundSurface`](ground_surface.md) sur lequel est la position indiquée. \
  Paramètre :
  * `position` : *`Vector2`* \
  La position (du joueur en général).

- `find_closest_item(position)` &rarr; `tuple[InventoryItem, Table | None]` \
  Retourne l'[`InventoryItem`](inventory_item.md) le plus proche de la position indiquée, utile pour en prendre un avec soi. \
  Paramètre :
  * `position` : *`Vector2`* \
  La position (du joueur en général).

- `find_closest_item_place(position)` &rarr; `dict` \
  Retourne l'emplacement d'item sur une [`Table`](table.md) le plus proche de la position indiquée. \
  Paramètre :
  * `position` : *`Vector2`* \
  La position (du joueur en général).

- `update()` &rarr; `None` \
  Update ses éléments si le jeu n'est pas en pause et trie ses éléments à chaque frame.
