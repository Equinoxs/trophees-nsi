# `Camera` - gestion de l'affichage
## Description
Cette classe est nécessaire à l'affichage des éléments à l'écran.

Elle permet de générer une image affichable en superposant les images de chaque `Sprite` ou `UIElement`.

Pour cela, le rendu est segmenté en plusieurs surfaces indépendantes les unes des autres. Par exemple, il y a une surface pour la map, et une pour les menus, ils ne rentrent pas en contact, ce qui permet d'appliquer des logiques différentes pour chacune d'elle et d'éviter certains bugs.

Elle appelle ainsi les méthodes `render()` de chaque élément de la map à afficher, dans un ordre prédéfini pour qu'ils se superposent bien.

## Attributs
- `screen` : *`Surface`* **get** \
  Surface représentant l'écran fourni par `PyGame`.
- `frame` : *`Rect`* **get** \
  Rectangle représentant l'écran __par rapport à la carte du jeu__.
- `camera` : *`Rect`* **get** \
  Copie de `frame` utilisée pour le rendu.
- `zoom` : *`float`* **get**
  Le facteur d'agrandissement de la carte.
- `map_overflow_factor` : *`float`* \
  Facteur de dépassement de la `Map` utilisé pour le rendu de celle-ci et de la `MiniMap`.
- `is_map_rendered` : *`float`* **get/set**
  Utilisé pour optimiser le jeu et éviter des rendus de la carte inutiles
- `is_full_map_rendered` : *`float`* **get/set**
  Pareil mais pour la grande map, quand elle est ouverte.
- `player_pos` : *`Vector2`*
  Un pointeur vers la position du joueur afin d'ajuster `camera`.
- `surfaces` : *`dict`* \
  Dictionnaire contenant les surfaces à rendre pour chaque écran.

## Méthodes
- `__init__(screen=None)` &rarr; `None` \
  Initialise les attributs. \
  Paramètre :
  * `screen` : *`Surface`*

- `initialize()` &rarr; `None` \
  Méthode appelée par `__init__`, elle charge les éléments et leur applique le zoom approprié.

- `initialize_surfaces()` &rarr; `None` \
  Méthode appelée par `initialize`, elle charge les surfaces et les distribue dans les cases de `surfaces`.

- `get_surface(surface_name)` &rarr; `Surface` \
  Retourne la surface associée au nom `surface_name`. \
  Paramètre :
  * `surface_name` : *`str`*

- `update()` &rarr; `None` \
  Met à jour l'écran en affichant la surface de la `Map` et des éventuels menus, composée par `draw`.

- `draw(surface_to_draw, position=(0, 0), surface_target_name='map', is_player_rendered=False)` &rarr; `None` \
  Méthode appelée par tous les `Sprite` ou `UIElement`, permettant de les rendre sur une surface stockée dans la liste 
  associée à `surface_target_name` dans `surfaces`. \
  Paramètres :
  * `surface_to_draw` : *`Surface`*
  * `position` : *`Vector2 | tuple`*
  * `surface_target_name` : *`str`*
  * `is_player_rendered` : *`bool`* \
    Indique si le `Sprite` en train d'être rendu est le joueur, si c'est le cas, il est rendu au centre de l'écran.
