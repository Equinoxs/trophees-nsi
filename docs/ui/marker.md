# `Marker` - marqueur sur la carte
Cette classe est nécessaire à l'affichage de marqueurs d'éléments graphiques fixés à une position sur la carte.

C'est ce qui permet l'affichage des marqueurs "!" pour les missions.
*Remarque : ceux là sont dits marqueurs spéciaux, c'est-à-dire que s'ils sortent de l'écran, ils restent collés au bord.*

Le popup `e` ou `r` pour les interactions pour les items sont aussi des marqueurs mais ceux-là ne sont pas spéciaux.

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