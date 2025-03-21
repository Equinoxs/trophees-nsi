# `Sprite` - éléments visuels du jeu
## Description
Cette classe est nécessaire pour afficher des éléments visuels à l'écran relativement à la `Map`, contrairement aux `UIElement` qui ont une position fixe.

Elle permet aux éléments d'avoir une image, une *hitbox* (boîte de collisions) et une position dans l'espace en 2 dimensions de la `Map`.

Elle permet de charger une image en mémoire et de l'afficher à l'écran et en implémentant toutes les méthodes nécessaires aux transformations d'image.

## Attributs
- `position` : *`Vector2`* **get**
- `image_type` : *`str`* \
  Type d'image du `Sprite`. Cet attribut est défini dans les classes enfant et sert à déterminer le dossier parent de l'image, par exemple `ground_surface` pour les sols ou `npc` pour les PNJ.
- `original_image` : *`pygame.Surface`* \
  Image telle qu'elle est stockée dans son fichier. Cet attribut permet de rogner l'image ensuite si elle contient plusieurs *frames*.
- `image` : *`pygame.Surface`* **get**\
  Image telle qu'elle est affichée à l'écran, après toutes les modifications apportées dans le code.
- `image_path` : *`str`* \
  Chemin du fichier image.
- `image_data` : *`dict`* **get** \
  Informations de l'image, telles qu'elles sont définies dans le fichier JSON. Ceci inclut les *frames* de l'animation et les données de la *hitbox* du `Sprite`.
- `magnification_coeff` : *`float`* **get** \
  Coefficient multiplicateur de l'agrandissement, à `1` par défaut et utilisé pour le zoom du jeu.
- `vertical_flip`: *`bool`* \
  Renversement vertical du `Sprite`.
- `horizontal_flip`: *`bool`* \
  Renversement horizontal du `Sprite`, utilisé par exemple pour mettre en miroir le joueur lorsqu'il change de direction.
- `rendered` : *`bool`* \
  Indique si le `Sprite` a été rendu à l'écran au dernier rafraîchissement.
- `must_render` : *`bool`* **get / set**\
  Indique si le `Sprite` doit être rendu à l'écran au prochain rafraîchissement.


## Méthodes
- `__init__(position, image_path)` &rarr; `None` \
  Initialise les attributs et charge l'image. \
  Paramètres :
  * `position` : *`Vector2`*
  * `image_path` : *`str`* \
    Chemin de l'image à charger.

- `switch_horizontal_flip()` &rarr; `None` \
  Met l'image en miroir horizontalement.

- `switch_vertical_flip()` &rarr; `None` \
  Met l'image en miroir verticalement.

- `go_to_frame(frame_index, animation_name, coeff=1)` &rarr; `None` \
  Change de *frame* de l'animation en sélectionnant le tronçon approprié de l'image. \
  Paramètres :
  * `frame_index` : *`int`* \
    Index de la *frame* vers laquelle changer.
  * `animation_name` : *`str`* \
    Nom de l'animation en cours.
  * `coeff` : *`float`* \
    Coefficient multiplicateur de la largeur de la *frame*.

- `skew_image(surface, horizontal_skew, vertical_skew)` &rarr; `pygame.Surface` \
  Déforme une image. \
  Paramètres :
  * `surface` : *`pygame.Surface`* \
    Image à modifier.
  * `horizontal_skew` : *`int`* \
    Déformation horizontale.
  * `vertical_skew` : *`int`* \
    Déformation verticale.

- `fill_surface(self, surface, width, height)` &rarr; `pygame.Surface` \
  Remplit une surface d'une certaine texture. \
  Paramètres :
  * `surface` : *`pygame.Surface`* \
    Image à appliquer comme texture.
  * `width` : *`int`*
  * `height` : *`int`*

- `rotate(angle)` &rarr; `None` \
  Pivote l'image d'un certain angle. \
  Paramètre :
  * `angle` : *`int`*

- `set_magnification(magnification_coeff)` &rarr; `None` \
  Change le coefficient multiplicateur de l'agrandissement et redimensionne l'image en fonction de celui-ci. \
  Paramètre :
  * `magnification_coeff` : *`float`*

- `move_to(position)` &rarr; `None` \
  Change la position. \
  Paramètre :
  * `position` : *`Vector2`*

- `update()` &rarr; `None` \
  Met à jour l'animation en cours.

- `render` &rarr; `None` \
  Méthode appelée par `Camera` pour effectuer le rendu. 