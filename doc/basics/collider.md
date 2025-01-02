# `Collider` - gestion des collisions
## Description
Cette classe est nécessaire aux classes enfant pour pouvoir entrer en collision avec les autres `Sprite` et ne pas passer à travers.

Elle permet de calculer la distance entre le point le plus proche de la *hitbox* du `Sprite` cible et la position de l'instance
de la classe enfant. Ceci permet à l'instance de la classe enfant de faire réagir l'accélération du `Player` en conséquence.

En comparant cette distance et `hitbox_action_radius`, il est possible pour les classes enfant de savoir si un autre élément entre en collision.

***Remarque :*** La position d'un `NPC` est la position de **ses pieds**. 

## Attributs
- `hitbox` : *`list[list[int]]`*
- `hitbox_closed` : *`bool`* \
  Indique si la *hitbox* est fermée.
- `hitbox_action_radius` : *`int`* \
  Rayon d'action de la *hitbox*.

## Méthodes
- `__init__(hitbox)` &rarr; `None` \
  Initialise la *hitbox*. \
  Paramètre :
  * `hitbox` : *`list[list[int]]`*
- `closest_vector_to(position)` &rarr; `Vector2` \
  Renvoie le `Vector2` représentant la distance du `Player` au point le plus proche de la *hitbox*. \
  Paramètre :
  * `position` : *`Vector2`* \
    La position du `Sprite`.