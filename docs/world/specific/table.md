# `Table` - Pour poser des items dessus

## Description

Cette classe est nécessaire pour pouvoir poser des items dessus

Elle hérite de [`Furniture`](furniture.md), car une table est un meuble.

Les fonctionnalités qu'elle apporte en plus sont autour de la gestion des items dessus.
La table contient plusieurs positions relatives à elle qui indiquent les différents emplacements possibles des items sur la table. \
C'est comme ça que le jeu sait si l'item à relâcher doit aller sur une table ou au sol. \
Ainsi, la table contient la liste des [`InventoryItem`](inventory_item.md) qu'elle contient.

> ```json
> {
> 	"type": "Table",
> 	"name": "square_table",
> 	"image_path": "dark_square",
> 	"item_positions": [[20, 50], [70, 20]],
> 	"items": [
> 		{
> 			"type": "InventoryItem",
> 			"image_path": "blue_book",
> 			"name": "mansion_square_table_book_1"
> 		},
> 		{
> 			"type": "InventoryItem",
> 			"image_path": "green_book",
> 			"name": "mansion_square_table_book_2"
> 		}
> 	],
> 	"position": [540, 175]
> }
> ```
> Exemple complet de dictionnaire d'initialisation d'une table

Dans cet exemple, `"blue_book"` va aller à la position `[20, 50]` étant donné que `index_position` n'a pas été renseigné : *Voir [`InventoryItem`](inventory_item.md)*

## Attributs
- `items` : *`list[InventoryItem]`* **get** \
  La liste des [`InventoryItem`](inventory_item.md) posés sur la table.
- `item_positions` : *`list[list[int]]`* **get** \
  La liste des emplacements possibles.

## Méthodes
- `__init__(data)` &rarr; `None` \
  Initialise la classe parent, `item_positions` et `items`. \
  Paramètre :
  * `data` : *`dict`* \
  Le dictionnaire d'initialisation de la table.

- `take_item(item, index_position)` &rarr; `None` \
  Prend un item à la position indiquée. \
  Paramètres :
  * `item` : *`InventoryItem`*
  * `index_position` : *`int`*

- `release_item(item)` &rarr; `None` \
  Relâche l'item indiquée au sol. \
  Paramètre :
  * `item` : *`InventoryItem`*

- `get_item_position(item_ref)` &rarr; `Vector2` \
  Retourne la position de l'item indiquée relativement à la map. \
  Paramètre :
  * `item_ref` : *`InventoryItem`*

- `get_item(item_name)` &rarr; `InventoryItem` \
  Retourne l'item indiquée selon son nom s'il est trouvé. \
  Paramètre :
  * `item_name` : *`str`*

- `item_position_taken(index_position)` &rarr; `bool` \
  Indique si la position indiquée est occupée par un item. \
  Paramètre :
  * `index_position` : *`int`*
  