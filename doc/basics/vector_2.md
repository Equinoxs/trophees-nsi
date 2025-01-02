# `Vector2` - représentation des vecteurs et points en 2D
## Description
Cette classe est nécessaire pour représenter les points pour les positions par exemple et les vecteurs pour les trajectoires par exemple.

Elle permet de stocker les valeurs `x` et `y` du vecteur, et d'effectuer toutes les opérations vectorielles nécessaires.

## Attributs
- `x` : *`int`* **get / get**
- `y` : *`int`* **get / get**

## Méthodes
- `__init__(x=0, y=0)` &rarr; `None` \
  Initialise les coordonnées x et y. \
  Paramètres :
  * `x` : *`float`*
  * `y` : *`float`*

- `copy(position=None)` &rarr; `Vector2` \
  Renvoie une copie de cette instance ou prend les valeurs d'une autre instance si elle est fournie en paramètre. \
  Paramètre :
  * `position` : *`Vector2`*

- `set_all(x, y)` &rarr; `None` \
  Paramètres : \
  * `x` : *`float`*
  * `y` : *`float`*