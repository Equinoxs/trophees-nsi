# `UIElement` - éléments de l'interface graphique
## Description
Cette classe est nécessaire pour pouvoir créer des éléments visuels quelconques et les afficher à l'écran.

Un élément s'initialise à partir de données renseignées dans le fichier [`data/menus_info.json`](../../data/menus_info.json) pour en faire un élément visible à l'écran.

Un élément permet d'avoir une `class`, c'est un concept inspiré du CSS afin de pouvoir réutiliser du syle, les class sont définies dans le même fichier que les `UIElement`. Une class peut avoir recour à d'autres classes et ses propriétés peuvent être réécrites selon la proximité de la class avec l'élément.

>```json
>{
>	"type": "Button",
>	"label": "Close",
>	"border_radius": 4,
>	"border_length": 2,
>	"border_color": [46, 34, 9],
>	"color": [61, 53, 39],
>	"text_color": [204, 174, 114],
>	"font_size": 50,
>	"x": 50,
>	"y": 40,
>	"width": 140,
>	"height": "auto",
>	"action": "focus_on_game"
>}
>```
> *Exemple de fichier `info.json`*

## Attributs
- `border_radius` : *`int`*  \
  Rayon des bordures de l'élément.
- `label` : *`str`*  \
  Texte affiché dans l'élément.
- `position` : *[`Vector2`](../utils/vector_2.md)*  \
  Position de l'élément dans la fenêtre.
- `color` : *`tuple`*  \
  Couleur de fond de l'élément (R, G, B, A).
- `text_color` : *`tuple`*  \
  Couleur du texte (R, G, B).
- `image_path` : *`str`*  \
  Chemin vers l'image associée à l'élément (facultatif).
- `original_image` : *`pygame.Surface`*  \
  Image d'origine chargée (si applicable).
- `image` : *`pygame.Surface`*  \
  Image redimensionnée pour correspondre à la hauteur spécifiée.
- `image_height` : *`int`*  \
  Hauteur de l'image (facultatif).
- `border_length` : *`int`*  \
  Largeur des bordures de l'élément.
- `border_color` : *`tuple`*  \
  Couleur des bordures (R, G, B).
- `surface` : *`Surface`*  \
  Surface graphique représentant l'élément.
- `rect` : *`Rect`*  \
  Rectangle de position et dimensions de l'élément.
- `_text_surface` : *`Surface`*  \
  Surface contenant le texte rendu.
- `_text_rect` : *`Rect`*  \
  Rectangle de position du texte à l'intérieur de l'élément.

## Méthodes
- `__init__(data)` &rarr; `None` \
  Initialise les attributs d'un élément à partir des données JSON fournies. \
  Paramètre :
  * `data` : *`dict`* \
    Données pour configurer l'élément.

- `update_rect()` &rarr; `None` \
  Met à jour les rectangles (`rect` et `_text_rect`) en fonction de la position et de la surface de l'élément.

- `get_rect()` &rarr; `Rect` \
  Retourne le rectangle principal de l'élément.

- `update()` &rarr; `None` \
  Met à jour l'élément. Peut être surchargée dans des classes enfants.

- `render()` &rarr; `None` \
  Affiche l'élément à l'écran en dessinant la surface, les bordures, le texte et l'image (si applicable).

- `render_text(surface='menu')` &rarr; `None` \
  Affiche le texte sur la surface `surface`. \
  Paramètre :
  * `surface` : *`str`*

- `calculate_text_surface()` &rarr; `None` \
  Calcule la surface du texte de `label`.

- `calculate_text_rect()` &rarr; `None` \
  Calcule le rectangle du texte en fonction de son alignement.