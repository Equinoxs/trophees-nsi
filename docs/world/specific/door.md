# `Door` - Les portes : portails entre deux cartes.

## Description

Comme tout jeu contient plusieurs complexes à explorer, cette classe nous permet ainsi de voyager entre les cartes.

Ce sont des classes fantômes, c'est-à-dire qu'elles n'ont pas d'image à rendre, ce sont juste des entités permettant de voyager.

La destination de ces portes est déterminé par une interaction. *Voir [`Interactable`](../basics/interactable.md).*

On peut les initialiser soit comme n'importe quel autre objet, soit à travers un [`Building`](building.md).

## Attributs
- `required_level` : *`int`* \
  Le niveau requis pour passer à travers la porte.
- `belongs_to_building` : *`bool`* \
  Indique si la porte a été générée par un `Building`.

## Méthodes
- `__init__(data)` &rarr; `None`
  Initialise la classe parent ainsi que les deux attributs supplémentaires.
  Paramètre :
  * `data` : *`dict`*

- `update()` &rarr; `None` \
  Gère l'état de l'attribut `is_interaction_available` de [`Interactable`](../basics/interactable.md).

- `render()` &rarr; `None` \
  Empêche le rendu de quoi que ce soit à l'écran

- `get_data()` &rarr; `dict | None` \
  Renvoie les données de la classe parente si la porte n'appartient pas à un `Building`, elle renvoie *`None`* sinon pour ne pas être sauvegardée.
