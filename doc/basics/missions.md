# `Mission` - stockage des missions
## Description
Cette classe permet de stocker les missions.

Au lieu d'utiliser un dictionnaire contenant toutes les fonctions métier, une classe *singleton* permet de les accompagner de
méthodes utilitaires permettant une meilleure gestion.

Elle implémente une liste de missions et d'objectifs avec leur description et les méthodes nécessaires à leur gestion.

## Attributs
- `_initialized` : *`bool`* \
  Indique si la classe a été initialisée afin de n'avoir qu'une instance.
- `missions_set` : *`set`* **get**
- `objective_descriptions` : *`dict`* \
  Description des objectifs sous la forme <nom_de_la_mission>_<indice_de_l'objectif>.

## Méthodes
- `__init__()` &rarr; `None`
- `update_missions_set()` &rarr; `None` \
  Met à jour ou crée `missions_set` en fonction des objectifs.

- `is_mission(mission_name)` &rarr; `bool` \
  Renvoie `True` si la mission existe. \
  Paramètre :
  * `mission_name` : *`str`*

- `get_description(mission_name, index)` &rarr; `str` \
  Renvoie la description d'un objectif, et "Mysterious objective..." si celle-ci n'est pas définie. \
  Paramètres :
  * `mission_name` : *`str`*
  * `index` : *`int`* \
    Indice de l'objectif.

- `do(mission_name, index)` &rarr; `int` \
  Exécute la méthode associée à l'objectif `index` d'une mission `mission_name` et renvoie le résultat de cet objectif. \
  Paramètres :
  * `mission_name` : *`str`*
  * `index` : *`int`* \
    Indice de l'objectif.

> - `mission_XXXXX(index)` &rarr; `int` \
>   Exécute la méthode associée à l'objectif `index` de la mission XXXXX et renvoie le résultat de cet objectif. \
>   Paramètre :
>   * `index` : *`int`* \
>      Indice de l'objectif.
> - `mission_XXXXX_n()` &rarr; `int` \
>   Exécute la méthode associée à l'objectif n de la mission XXXXX et renvoie le résultat de cet objectif.
> 
> *Exemple de fonctions pour un objectif XXXXX.*