# `MiniMap` - petite carte
## Description
Cette classe est nécessaire à l'affichage d'une vue d'ensemble de la carte dans le coin supérieur droit de l'écran.

Elle permet au joueur de voir son écran en plus petit et lors du clic une vue plus large de la carte en plein écran.

Elle dérive de [`Button`](button.md), se référer à sa documentation pour les attributs et méthodes surchargés.

## Attributs
- `height` : *`int`*
- `surface_to_watch` : *`pygame.Surface`*

## Méthodes
- `__init__(data)` &rarr; `None` \
  Initialise [`Button`](button.md) de couleur transparente avec l'action `open_map` et les attributs. \
  Paramètre :
  * `data` : *`dict`* \
    Données pour configurer l'élément.
- `update()` &rarr; `bool` \
  Met à jour l'image affichée et renvoie `True` si le jeu est affiché et `False` si un menu autre est ouvert.
- `render()` &rarr; `None` \
  Affiche l'élément à l'écran.