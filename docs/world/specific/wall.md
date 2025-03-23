# `Wal` - Un mur !

## Description

Cette classe est nécessaire pour pouvoir bâtir des murs complexes suivant un tracé de points.

`Wall` est un peu spécial : ce n'est pas un [`MapElement`](../basics/map_element.md). En effet, cette classe, initialisé par [`Map`](map.md), a en réalité comme seule fonction d'initialiser des [`WallSegment`](wall_segment.md). Ceci permet une meilleure gestion des superpositions, en faisant des murs séparés comme ceci, nous avons la possibilité d'intercaler un objet entre deux façades d'un même mur lors du rendu.

> ```json
> {
> 	"type": "Wall",
> 	"name": "main_borders",
> 	"wall_type": "brown_2",
> 	"boundaries": [[0, 900], [0, 0], { "sticker": "door_wood", "x_offset" : 35 }, [1000, 0]]
> }
> ```
> Exemple de dictionnaire d'initialisation de `Wall`.

Le coeur de ce mur est `"boundaries"`, nous remarquons qu'il est constitué de coordonnées mais aussi de `stickers`. *Pour plus d'informations, voir [`WallSegment`](wall_segment.md).*

## Attributs
- `segments` : *`list[WallSegment]`* \
  La liste des [`WallSegment`](wall_segment.md) issus de ce mur.
- `data` : *`dict`* **get** \
  Son dictionnaire d'initialisation.
- `original_data` : *`dict`* \
  Une copie du dictionnaire d'initialisation pour préserver les données originales.
- `name` : *`str`* **get** \
  Le nom du mur.
- `boundaries` : *`list[list[int] | dict]`* \
  Le chemin parcouru par le mur.

## Méthodes
- `__init__(data, map)` &rarr; `None` \
  Initialise ses attributs et appelle `initialize_segments(map)`.
  Paramètres :
  * `data` : *`dict`* \
  Le dictionnaire d'initialisation de la table.
  * `map` : *`Map`* \
  Une référence de la [`Map`](map.md) actuelle afin d'ajouter des [`WallSegment`](wall_segment.md) à cette dernière.

- `initialize_segments(map)` &rarr; `None` \
  Se gère de créer les [`WallSegment`](wall_segment.md) et de les ajouter à `segments`.
  Paramètre :
  * `map` : *`Map`* \
  Une référence de la [`Map`](map.md) actuelle afin d'ajouter des [`WallSegment`](wall_segment.md) à cette dernière.

- `get_data()` &rarr; `dict` \
  Retourne `original_data` en prenant soin d'enlever la clé `"position"` de ce dernier afin d'éviter de sauvegarder des données inutiles.
