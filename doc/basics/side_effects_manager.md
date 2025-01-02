# `SideEffectsManager` - gestion des effets de bord
## Description
Cette classe permet aux classes enfant d'implémenter des effets de bord, 
c'est-à-dire des actions dans le jeu avec un état conservé au cours du cycle de vie de la classe enfant.

Elle permet aux classes enfant d'effectuer des tests et des opérations à chaque rafraîchissement de l'écran,
et de conserver leur état pour poursuivre l'avancée dans la chronologie du jeu par exemple.

Elle conserve les variables d'état au sein du dictionnaire `side_effects_data`.

## Attributs
- `side_effects` : *`list[function]`* \
  Effets de bord à exécuter à chaque rafraîchissement d'écran.
- `side_effects_data` : *`dict`* \
  Variables d'état utilisées par les fonctions.

## Méthodes
- `__init__(side_effects)` &rarr; `None` \
  Initialise les fonctions des effets de bord. \
  Paramètre : \
  * `side_effects` : *`list[function]`*

- `side_effect_data(key, val=None)` &rarr; `object` \
  Récupére la valeur associée à `key`, et si `val` est spécifiée, la remplacer par `val`. \
  Paramètres :
  * `key` : *`str`*
  * `val` : *`object`*

- `add_side_effect(side_effect_name)` &rarr; `None` \
  Paramètre : \
  * `side_effect_name` : *`str`*

- `remove_side_effect(side_effect_name)` &rarr; `None` \
  Paramètre : \
  * `side_effect_name` : *`str`*

- `apply_side_effect()` &rarr; `None` \
  Exécute toutes les fonctions de `side_effects`.