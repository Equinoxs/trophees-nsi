# `BaseObject` - objet de base
## Description
### Hérite de : `MapObject`
Cette classe représente un `MapObjet` de base.

Elle sert de classe de test.
## Attribut
- `object_type` : *`str`* **get**
## Méthodes
- `__init__(data)` &rarr; `None` \
  Initialise `object_type`. \
  Paramètre : 
  * `data` : *`dict`* \
    Données d'initialisation.

- `goes_on_top_of(map_object)` &rarr; `bool` \
  Indique si cet élément se place au-dessus de `map_object`. \
  Paramètres :
  * `map_object` : *`MapObject`*
