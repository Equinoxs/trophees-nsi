# `MapObject` - éléments "vivants" du jeu

## Description
### Hérite de : `MapElement`, `Collider`, `Interactable`, `Movable`, `SideEffectsManager`

Cette classe est nécessaire pour permettre aux `MapElement` d'avoir des changements 
d'état en fonction de leur environnement et des réactions spécifiques. 

Elle permet à ses classes enfant d'implémenter des collisions, des interactions avec le joueur 
et des effets de bord.

Elle rassemble les classes `MapElement`, `Collider`, `Interactable`, `Movable` et `SideEffectsManager`
et assure leur mise à jour à chaque rafraîchissement d'écran.

Ce qui faut comprendre avec cette classe, c'est qu'elle représente un, véritable objet du monde réel, contrairement à [`MapElement`](map_element.md).

## Attribut
> *aucun*

## Méthodes
- `__init__(data)` &rarr; `None` \
  Initialise les classes parentes en fonction de `data`, fourni par `DataHandler` en fonction du fichier JSON. \
  Paramètre :
  * `data` : *`dict`*

- `catch_event(event)` &rarr; `None` \
  Permet d'intercepter un évènement provenant de la [`Map`](../specific/map.md), appelle la même méthode de [`Interactable`](interactable.md) et de [`MapElement`](map_element.md).
  Paramètre :
  * `event` : *`str | dict`*
    l'évènement à traiter

- `update()` &rarr; `None` \
  Méthode exécutée à chaque rafraîchissement du jeu, permet de mettre à jour les classes parentes
  et de gérer les interactions avec le joueur et les déplacements.

- `__del__()` &rarr; `None` \
  Méthode exécutée à chaque rafraîchissement du jeu, permet de mettre à jour les classes parentes
  et de gérer les interactions avec le joueur et les déplacements.
