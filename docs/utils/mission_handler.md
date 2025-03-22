# `MissionHandler` - gestion des missions
## Description
Cette classe permet de gérer l'**exécution** des missions.

Elle permet au jeu d'avoir une progression dans le temps selon une trame narrative bien définie.

Se référer à [la documentation de `Mission`](../world/basics/mission.md) pour plus d'informations quant à leur fonctionnement.
## Attributs
- `missions_data` : *`list`* \
  Données des missions récupérées depuis le JSON par [`DataHandler`](data_handler.md).
- `missions` : *`dict`* \
  Stockage des [`Mission`](../world/basics/mission.md)s une fois initialisées.
- `current_mission` : *[`Mission`](../world/basics/mission.md)* **get**
- `mission_description_displayed` : *[`UIElement`](../ui/ui_element.md)* \
  Description de la [`Mission`](../world/basics/mission.md) affichée à l'écran.
- `mission_popup` : *[`UIElement`](../ui/ui_element.md)* \
  Popup affiché à l'écran lors de la réussite ou de l'échec d'une [`Mission`](../world/basics/mission.md).

## Méthodes
- `__init__(missions_data)` &rarr; `None` \
  Initialise les attributs. \
  Paramètre :
  * `missions_data` : *`list`*
- `get_mission(mission_name)` &rarr; [`Mission`](../world/basics/mission.md) \
  Renvoie la [`Mission`](../world/basics/mission.md) nommée `mission_name`. \
  Paramètre :
  * `mission_name` : *`str`*
- `get_current_mission_name()` &rarr; `str` \
  Renvoie le nom de la [`Mission`](../world/basics/mission.md) en cours.
- `mission_ongoing()` &rarr; `bool` \
  Renvoie `True` si une [`Mission`](../world/basics/mission.md) est en cours et `False` sinon.
- `initialize_missions()` &rarr; `None` \
  Méthode appelée par `__init__`. 
  Instancie les [`Mission`](../world/basics/mission.md)s de `missions` à partir de `missions_data`.
- `abort_mission()` &rarr; `None` \
  Si une [`Mission`](../world/basics/mission.md) est en cours, l'annule et remet le jeu dans son état précédent le lancement de ladite [`Mission`](../world/basics/mission.md).
- `start_mission(mission_name)` &rarr; `None` \
  Démarre une [`Mission`](../world/basics/mission.md) à partir de son nom `mission_name`. \
  Paramètre :
  * `mission_name` : *`str`*
- `display_description_of_current_mission()` &rarr; `None` \
  Affiche la description de la [`Mission`](../world/basics/mission.md) en cours à l'écran.
- `delete_description_displayed()` &rarr; `None` \
  Supprime la description affichée.
- `update()` &rarr; `None` \
  Met à jour le jeu en fonction du statut actuel de la [`Mission`](../world/basics/mission.md) : 
  * si elle est terminée, il met à jour les [`Mission`](../world/basics/mission.md)s accomplies du joueur, sauvegarde et affiche le popup ;
  * si elle est échouée, il affiche le popup et termine la mission ;
  * si elle est en cours, il met à jour la description affichée.
  