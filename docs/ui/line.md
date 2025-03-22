# `Line` - ligne
Cette classe est nécessaire à l'affichage de lignes à l'écran.

Elle dérive de [`UIElement`](ui_element.md), se référer à sa documentation pour les attributs et méthodes surchargés.

## Attributs
- `start_pos` : *[`Vector2`](../utils/vector_2.md)* **get**
- `end_pos` : *[`Vector2`](../utils/vector_2.md)* **get**
- `color` : *`tuple`* **set** \
  Couleur au format RGBA.
- `width` : *`int`* **set**

## Méthodes
- `__init__(data)` &rarr; `None` \
  Initialise les attributs et [`UIElement`](ui_element.md).
  Paramètre :
  * `data` : *`dict`* \
    Données pour configurer l'élément.
- `update()` &rarr; `None`
  Ne fait rien, présente pour des raisons de compatibilité.
- `render()` rarr; `None`
  Affiche la ligne à l'écran.