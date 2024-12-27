# `Collider` - gestion des collisions des `Sprite`
## Description
Cette classe permet de déterminer si un `Sprite` entre en collision avec **les pieds** du joueur (point de référence de sa position).

## Attributs
- `hitbox` : *`list[list[int]]`*
- `hitbox_closed` : *`bool`* \
  Indique si la *hitbox* est fermée.
- `hitbox_action_radius` : *`int`* \
  Le rayon d'action de la *hitbox*.

## Méthodes
- `__init__(hitbox)` \
  Initialise la *hitbox*. \
  Paramètre :
  * `hitbox` : *`list[list[int]]`*
- `closest_vector_to(position)` \
  Renvoie le `Vector2` représentant la distance du `Player` au point le plus proche de la *hitbox*. \
  Paramètre :
  * `position` : *`Vector2`* \
    La position du `Sprite`.