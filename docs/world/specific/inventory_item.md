# `InventoryItem` - Un objet pour se balader avec.

## Description

Cette classe est nécessaire afin de donner de la matière au système d'inventaire.

Elle représente un objet que l'on peut prendre dans son inventaire, et déposer à sa guise sur le sol ou sur une [`Table`](table.md).

Elle gère, tout comme [`Interactable`](../basics/interactable.md), un [`Marker`](../../ui/marker.md) pour savoir si on peut prendre un objet avec soi.

## Attributs
- `pickup_marker` : *`Marker | None`* \
  le `Marker` de l'item.
- `index_position` : *`int | None`* **get / set** \
  Utilisé par [`Table`](table.md) pour savoir où est-ce que l'item se situe sur la table.

## Méthodes
- `__init__(data)` &rarr; `None`
  Initialise les classes parent ainsi que les deux attributs supplémentaires.
  Paramètre :
  * `data` : *`dict`*
- `remove_pickup_marker()` &rarr; `None`
  Retire le marker du jeu.
- `update()` &rarr; `None`
  Gère l'état de `pickup_marker`.
- `render()` &rarr; `None`
  Fais en sorte que la position de l'item corresponde au milieu de son image.
- `__del__()` &rarr; `None`
  enlève le `pickup_marker` en plus d'appeler le destructeur de la class parent.
