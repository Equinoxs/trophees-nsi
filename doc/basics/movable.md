# `Movable` - gestion du déplacement
## Description
Cette classe est nécessaire pour permettre les déplacements sur la `Map`.

Elle implémente une fonction `move` permettant à la classe enfant de se déplacer.

Grâce à un vecteur de vitesse (`speed_vector`) appliqué sur la position au fur et à mesure du déplacement, 
elle permet un déplacement linéaire et lisse.

## Attribut
- `speed_vector` : *`Vector2`* **get**

## Méthodes
- `__init__` &rarr; `None` \
  Initialise le vecteur de vitesse à un vecteur nul.

- `apply_force(force)` &rarr; `None` \
  Applique une force sur `speed_vector`. \
  Paramètre :
  * `force` : *`Vector2`*

- `move(sprite_position)` &rarr; `None` \
  Met à jour `sprite_position` en fonction de `speed_vector`. \
  Paramètres :
  * `sprite_position` : *`Vector2`*