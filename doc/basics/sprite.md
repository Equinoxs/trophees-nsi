# `Sprite` - Éléments visuels du jeu
## Description
Cette classe est parente de tout ce qui s'affiche à l'écran qui ne fait *pas* partie de l'interface graphique (UI). Ceci inclut le joueur et le fond de carte.

## Attributs
- `position` : *`Vector2`*
- `image_type` : *`str`* \
  Le type d'image du `Sprite`. Cet attribut est défini dans les classes enfant et sert à déterminer le dossier parent de l'image, par exemple `ground_surface` pour les sols ou `npc` pour les PNJ.
- `original_image` : *`pygame.Surface`* \
  L'image telle qu'elle est stockée dans son fichier. Cet attribut permet de rogner l'image ensuite si elle contient plusieurs *frames*.
- `image` : *`pygame.Surface`* \
  L'image telle qu'elle est affichée à l'écran, après toutes les modifications apportées dans le code.
- `image_path` : *`str`* \
  Le chemin du fichier image.
- `image_data` : *`dict`* \
  Les informations de l'image, telles qu'elles sont définies dans le fichier JSON. Ceci inclut les *frames* de l'animation et les données de la *hitbox* du `Sprite`.
- `magnification_coeff` : *`float`* \
  Le coefficient multiplicateur de l'agrandissement, à `1` par défaut, et utilisé pour le zoom du jeu.
- `vertical_flip`: *`bool`* \
  Le renversement vertical du `Sprite`.
- `horizontal_flip`: *`bool`* \
  Le renversement horizontal du `Sprite`, utilisé par exemple pour mettre en miroir le joueur lorsqu'il change de direction.

## Méthodes
- `__init__(position, image_path)` \
  Initialise les attributs et charge l'image. \
  Paramètres :
  * `position` : *`Vector2`*
  * `image_path` : *`str`* \
    Chemin de l'image à charger.
- `switch_horizontal_flip()` \
  Met l'image en miroir horizontalement.
- `switch_vertical_flip()` \
  Met l'image en miroir verticalement.
- `go_to_frame(frame_index, animation_name, coeff=1)` \
  Change de *frame* de l'animation. \
  Paramètres :
  * `frame_index` : *`int`* \
    Index de la *frame* vers laquelle changer.
  * `animation_name` : *`str`* \
    Nom de l'animation en cours.
  * `coeff` : *`float`* \
    Coefficient multiplicateur de la largeur de la *frame*.
- `skew_image(surface, horizontal_skew, vertical_skew)` \
  Déforme une image. \
  Paramètres :
  * `surface` : *`pygame.Surface`* \
    Image à modifier.
  * `horizontal_skew` : *`int`* \
    Déformation horizontale.
  * `vertical_skew` : *`int`* \
    Déformation verticale.
- `fill_surface(self, surface, width, height)` \
  Remplit une surface d'une certaine texture. \
  Paramètres :
  * `surface` : *`pygame.Surface`* \
    Image à appliquer comme texture.
  * `width` : *`int`*
  * `height` : *`int`*
- `rotate(angle)` \
  Pivote l'image d'un certain angle. \
  Paramètre :
  * `angle` : *`int`*
- `set_magnification(magnification_coeff)` \
  Change le coefficient multiplicateur de l'agrandissement, et redimensionne l'image en fonction de celui-ci. \
  Paramètre :
  * `magnification_coeff` : *`float`*
- `move_to(position)` \
  Change la position. \
  Paramètre :
  * `position` : *`Vector2`*