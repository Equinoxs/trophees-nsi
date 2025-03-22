# `Player` - joueur (vous)
## Description
Cette classe décrit le&middot;a joueur&middot;se, donc non seulement le [`ǸPC`](../world/specific/npc.md) qui le représente,
mais aussi tout ce qui va avec, c'est-à-dire les [`Mission`](../world/basics/mission.md)s qu'il&middot;elle a accompli.

## Attributs
- `map_name` : *`str`* **get**
- `map` : *[`Map`](../world/specific/map.md)* **get**
- `accomplished_missions` : *`list[str]`* **get** \
  Liste des noms des [`Mission`](../world/basics/mission.md)s accomplies.
- `focus` : *[`NPC`](../world/specific/npc.md)* **get** \
  [`NPC`](../world/specific/npc.md) représentant le&middot;a joueur&middot;se.

## Méthodes
- `__init__(map=None, data_player=None, map_name=None)` &rarr; `None` \
  Initialise les attributs et charge les données en fonction de `data_player`. \
  Paramètres :
  * `map` : *`Map`*
  * `data_player` : *`dict`*
  * `map_name` : *`str`*
- `change_map(map_name)` &rarr; `None` \
  Remplace la [`Map`](../world/specific/map.md) actuelle par celle nommée `map_name`. \
  Paramètre :
  * `map_name` : *`str`*
- `get_level()` &rarr; `int` \
  Renvoie le niveau du [`NPC`](../world/specific/npc.md) `focus`.
- `set_level(level)` &rarr; `None` \
  Met le niveau du [`NPC`](../world/specific/npc.md) `focus` à `level`. \
  Paramètre :
  * `level` : *`int`*
- `add_accomplished_mission(mission)` &rarr; `None` \
  Ajoute la [`Mission`](../world/basics/mission.md) à `accomplished_missions` et ajoute sa récompense au niveau du [`NPC`](../world/specific/npc.md) `focus`. \
  Paramètre :
  * `mission` : *[`Mission`](../world/basics/mission.md)*
- `change_focus(npc_name)` &rarr; `None` \
  Remplace le [`NPC`](../world/specific/npc.md) `focus` par celui nommé `npc_name` 
  s'il existe dans la [`Map`](../world/specific/map.md) actuelle, autrement le jeu plante. \
  Paramètre :
  * `npc_name` : *`str`*
- `teleport_to(point)` &rarr; `None` \
  Téléporte le [`NPC`](../world/specific/npc.md) `focus` au point `point` s'il s'agit d'un [`Vector2`](vector_2.md) 
  et au point associé au [`MapElement`](../world/basics/map_element.md) nommé `point` si c'est une `str`. \
  Paramètre :
  * `point` : *`str|`[`Vector2`](vector_2.md)*
- `update()` &rarr; `None` \
  Met à jour la [`Map`](../world/specific/map.md).
- `load_new_data(data)` &rarr; `None` \
  Indique au [`NPC`](../world/specific/npc.md) `focus` qu'il représente le joueur (de grands pouvoirs impliquent de grandes responsabilités), et charge les [`Mission`](../world/basics/mission.md)s accomplies. \
  Paramètre :
  * `data` : *`dict`*
- `get_data()` &rarr; `dict` \
  Renvoie les données à sauvegarder.