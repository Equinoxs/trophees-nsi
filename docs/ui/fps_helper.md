# `FPSHelper` - teste indicateur de FPS
## Description
Cette classe est nécessaire à l'affichage du nombre d'images par seconde du jeu.

Elle dérive de [`UIElement`](ui_element.md), se référer à sa documentation pour les attributs et méthodes surchargés.

## Attributs
- `nbr_frame` : *`int`* \
  Nombre de frames écoulées depuis la dernière mise à jour.
- `fps_timer` : *`float`* \
  Compteur de temps depuis la dernière mise à jour.

## Méthodes
- `__init__(data)` &rarr; `None` \
  Initialise [`UIElement`](ui_element.md) et les attributs. \
  Paramètre :
  * `data` : *`dict`* \
    Données pour configurer l'élément.

- `update()` &rarr; `bool` \
  Met à jour les attributs et le texte affiché à l'écran.
