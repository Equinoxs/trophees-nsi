# `Marker` - marqueur "!" 
Cette classe est nécessaire à l'affichage de marqueurs "!".

Elle pointe un [`NPC`](../world/specific/npc.md) par une image et indique sa position dans le jeu.

Elle dérive de [`UIElement`](ui_element.md), se référer à sa documentation pour les attributs et méthodes surchargés.

## Attributs
- `position` : *[`Vector2`](../utils/vector_2.md)* \
  Position **dans le jeu** et non à l'écran. 
- `real_image` : *`str`*
- `x_offset` : *`int`*
- `y_offset` : *`int`*
- `special` : *`bool`* **get** \
  Indique si le marqueur doit être affiché en tout temps à l'écran.

## Méthodes
- `__init__(data)` &rarr; `None` \
  Initialise les attributs et [`UIElement`](ui_element.md).
  Paramètre :
  * `data` : *`dict`* \
    Données pour configurer l'élément.
- `render()` rarr; `None`
  Affiche le marqueur à l'écran.