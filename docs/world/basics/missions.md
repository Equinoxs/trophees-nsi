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
- `objectives_store` : *`dict`* \
  Stockage de la progression des objectifs.

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

- `get_objectives_len(mission_name)` &rarr; `int` \
  Renvoie le nombre d'objectifs dans une mission `mission_name`. \
  Paramètres :
  * `mission_name` : *`str`*

- `use_create_dialog(dialog_name, dialog_data, immobilize_player)` &rarr; `int` \
  Crée un dialogue `dialog_name` avec les textes de `dialog_data`, et immobilise le joueur 
  si `immobilize_player` vaut `True`. Renvoie 1 si le dialogue est terminé et 0 sinon. \
  Paramètres :
  * `dialog_name` : *`str`*
  * `dialog_data` : *`dict`*
  * `immobilize_player` : *`bool`*

- `use_move_npc(npc_name, destination)` &rarr; `int` \
  Lance le déplacement d'un NPC `npc_name` vers `destination`. Renvoie 1 si le NPC a atteint sa destination
  et 0 sinon. \
  Paramètres :
  * `npc_name` : *`str`*
  * `destination` : *`Vector2`*

- `use_interaction(object_name)` &rarr; `int` \
  renvoie 1 si l'objet en question a intéragit avec le joueur, 0 sinon.
  Paramètre :
  * `object_name` : *`str`*
  Le nom de l'objet en question.

- `use_wait_for_item(item_name)` &rarr; `int` \
  renvoie 1 si l'item s'est retrouvé dans l'inventaire du joueur, 0 sinon.
  Paramètre :
  * `item_name` : *`str`*
  Le nom de l'item en question.

- `do(mission_name, index)` &rarr; `int` \
  Exécute la méthode associée à l'objectif `index` d'une mission `mission_name` et renvoie le résultat de cet objectif. \
  Paramètres :
  * `mission_name` : *`str`*
  * `index` : *`int`* \
    Indice de l'objectif.

> - `mission_XXXXX_n()` &rarr; `int` \
>   Exécute la méthode associée à l'objectif n de la mission XXXXX et renvoie le résultat de cet objectif.
> 
> *Exemple de méthode pour un objectif XXXXX.*