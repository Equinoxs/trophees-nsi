# `Camera` - gestion de l'affichage
## Description
Cette classe est nécessaire à l'affichage des éléments à l'écran.

Elle permet de générer une image affichable en superposant les images de chaque `Sprite` ou `UIElement`.

Elle appelle les méthodes `render()` de chaque élément à afficher, dans un ordre prédéfini, pour les afficher.

## Attributs
- `screen` : *`Surface`* **get** \
  Surface représentant l'écran fournie par `PyGame`.
- `frame` : *`Rect`* **get** \
  Rectangle représentant l'écran.
- `camera` : *`Rect`* **get** \
  Copie de `frame` utilisée pour le rendu.
- `zoom` : *`float`* **get**
- `map_overflow_factor` : *`float`* \
  Facteur de dépassement de la `Map` utilisé pour le rendu de celle-ci.
- `is_map_rendered` : *`float`* **get/set**
- `is_full_map_rendered` : *`float`* **get/set**
- `player_pos` : *`Vector2`* 
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
  * `position` : *`Vector2`* / *`tuple`*
  * `surface_target_name` : *`str`*
  * `is_player_rendered` : *`bool`* \
    Indique si le `Sprite` en train d'être rendu est le joueur.

