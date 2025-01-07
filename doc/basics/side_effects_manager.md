# `SideEffectsManager` - gestion des effets de bord
## Description
Cette classe permet aux classes enfant de pouvoir exécuter des effets de bord à chaque *frame* du jeu.

Elle permet aux classes enfant d'effectuer des tâches de fond à chaque rafraîchissement de l'écran,
afin de rendre le jeu plus interactif et vivant en fonction de multiples conditions.

Les fonctions exécutées lors des interactions sont stockées dans le dictionnaire `side_effects` dans le fichier `data_functions`.

Le dictionnaire `side_effects_data` permet de renforcer le pouvoir des effets de bord en stockant leurs variables d'état.

## Attributs
- `side_effects` : *`list[function]`* \
  Effets de bord à exécuter à chaque rafraîchissement d'écran.
- `side_effects_data` : *`dict`* \
  Variables d'état utilisées par les fonctions.

## Méthodes
- `__init__(side_effects)` &rarr; `None` \
  Initialise les fonctions des effets de bord. \
  Paramètre : 
  * `side_effects` : *`list[function]`*

- `side_effect_data(key, val=None)` &rarr; `object` \
  Récupère la valeur associée à `key`, et si `val` est spécifiée, la remplacer par `val`. \
  Paramètres :
  * `key` : *`str`*
  * `val` : *`object`*

- `add_side_effect(side_effect_name)` &rarr; `None` \
  Paramètre : 
  * `side_effect_name` : *`str`*

- `remove_side_effect(side_effect_name)` &rarr; `None` \
  Paramètre : 
  * `side_effect_name` : *`str`*

- `apply_side_effects()` &rarr; `None` \
  Exécute toutes les fonctions de `side_effects`.