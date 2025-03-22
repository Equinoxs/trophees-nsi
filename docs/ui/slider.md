# `Slider` - barre de défilement
Cette classe représente une barre de défilement.

Elle permet de choisir un nombre entre deux valeurs données.

Elle dérive de [`UIElement`](ui_element.md), se référer à sa documentation pour les attributs et méthodes surchargés.
## Attributs
- `min_value` : *`float`* \
  Valeur minimum, par défaut 0.
- `max_value` : *`float`* \
  Valeur maximum, par défaut 100.
- `current_value` : *`float`*
- `slider_width` : *`int`* \
  Longueur de la barre, par défaut 10.
- `track_color` : *`tuple(int)`* \
  Couleur de la barre, par défaut gris clair (200, 200, 200).
- `slider_color` : *`tuple(int)`* \
  Couleur du curseur, par défaut blanc.
- `border_radius`: *`int`*
- `border_color` : *`tuple(int)`* \
  Couleur de la bordure, par défaut noir.
- `action_name` : *`str`* \
  Nom de l'action de [`SliderActions`](slider_actions.md)
- `dragging` : *`bool`* \
  Indique si l'utilisateur est en train de déplacer le curseur.

## Méthodes
- `update()` &rarr; `None` \
  Met à jour la barre, appelle la méthode de [`SliderActions`](slider_actions.md) associée à `action_name` et 
  renvoie `True` si le curseur a été déplacé et `False` sinon.
- `render()` &rarr; `None` \
  Affiche la barre et son curseur à l'écran.
- `get_value()` &rarr; `float` \
  Renvoie la valeur actuelle du curseur.
  