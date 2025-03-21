# `PillarObject` - pilier
## Description
### Hérite de : `MapObject`
Cette classe représente un pilier, c'est-à-dire un `MapObject` prenant appui au sol en un point.

Elle implémente une méthode permettant aux autres classes de déterminer 
si elles doivent se placer au-dessus ou au-dessous.

Elle contient un attribut contenant son type pour permettre de calculer son placement en fonction du type
de l'autre objet.

## Attribut
- `object_type` : *`str`* = `'pillar'` **get**
## Méthodes
- `__init__(data)` &rarr; `None` \
  Initialise `MapObject` avec `data`. \
  Paramètre : 
  * `data` : *`dict`* \
    Données d'initialisation.

- `goes_on_top_of(map_object)` &rarr; `bool` \
  Indique si cet objet se place au-dessus de `map_object`. \
  Paramètre :
  * `map_object` : *`MapObject`*
