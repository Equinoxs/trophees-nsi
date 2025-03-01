# `Movable` - gestion du déplacement
## Description
Cette classe est nécessaire pour permettre les déplacements sur la `Map`.

Elle implémente une fonction `move` permettant à la classe enfant de se déplacer.

Grâce à un vecteur de vitesse (`speed_vector`) appliqué sur la position au fur et à mesure du déplacement, 
elle permet un déplacement linéaire et lisse.

## Attribut
- `speed_vector` : *`Vector2`* **get**
- `has_moved` : *`bool`* **get** \
  Indique si un mouvement a récemment été effectué.
## Méthodes
- `__init__` &rarr; `None` \
  Initialise le vecteur de vitesse au vecteur nul.

- `apply_force(force)` &rarr; `None` \
  Applique une force sur `speed_vector`, ce qui a pour effet de provoquer une accélération sur un modèle quadratique. \
  Paramètre :
  * `force` : *`Vector2`*

- `move(sprite_position)` &rarr; `None` \
  Applique `speed_vector` sur `sprite_position` en le multipliant par `dt` (&Delta;t) pour respecter la vitesse. \
  Paramètres :
  * `sprite_position` : *`Vector2`*

- `update()` &rarr; `None` \
  Met à jour la position et `has_moved`.