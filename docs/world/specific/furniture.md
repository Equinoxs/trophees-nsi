# `Furniture` - Meubles à l'intérieur d'une maison

## Description

Cette classe représente des meubles quelconques que l'on peut retrouver à l'intérieur d'une maison ou d'un bâtiment.

Son fonctionnement repose sur les mêmes principes que [`Building`](building.md) au niveau de la gestion de la `hitbox`.

C'est une image avec une `hitbox` associée. Elle est utilisée pour créer des bibliothèques, des chaises ou encore des poubelles et des caisses en carton.

## Attributs
> hérités des classes parent.
*Remarque : la hitbox et l'interaction peuvent être définies dans les données de l'image*

## Méthodes
- `__init__(data)` &rarr; `None` \
  Initialise la classe parent ainsi que la hitbox et l'interaction comme décrit ci-dessus. \
  Paramètre :
  * `data` : *`dict`*
