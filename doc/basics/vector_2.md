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
  Paramètres : 
  * `x` : *`float`*
  * `y` : *`float`*

- `get_squared_norm()` &rarr; `float` \
  Renvoie la norme au carré de ce vecteur, pour effectuer moins de calculs.

- `get_norm()` &rarr; `float` \
  Renvoie la norme de ce vecteur, lorsque sa valeur exacte est nécessaire.

- `normalize()` &rarr; `Vector2` \
  Règle la norme de ce vecteur à 1 et le renvoie.

- `set_norm(norm)` &rarr; `Vector2` \
  Règle la norme de ce vecteur à `norm` et le renvoie. \
  Paramètre :
  * `norm` : *`float`*

- `scalar_product(vector_2)` &rarr; `float` \
  Renvoie le produit scalaire de ce vecteur et de `vector_2`. \
  Paramètre :
  * `vector_2` : *`Vector2`*

- `distance_to(vector_2)` &rarr; `float` \
  Renvoie la distance jusqu'au vecteur `vector_2`. \
  Paramètre :
  * `vector_2` : *`Vector2`*

- `add(vector_2)` &rarr; `None` \
  Ajoute le vecteur `vector_2` à ce vecteur. \
  Paramètre :
  * `vector_2` : *`Vector2`*

- `orthogonal_projection(vector_2, return_t = False)` &rarr; `float|tuple[float]` \
  Renvoie le projeté orthogonal de vector2 sur self. \
  Paramètres :
  * `vector_2` : *`Vector2`*
  * `return_t` : *`bool`* \
    Renvoyer la valeur du coefficient de colinéarité t.

- `convert_to_tuple()` &rarr; `tuple` \
  Renvoie ce vecteur converti en tuple.

  
