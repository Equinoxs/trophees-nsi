# `FPSHelper` - teste indicateur de FPS
## Description
Cette classe est nécessaire à l'affichage du nombre d'images par seconde du jeu, situé en bas à droite.

Le calcul se fait sur un cycle de 0.3 secondes : *fps = nbr de frames écoulées depuis 0.3s / 0.3*

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
