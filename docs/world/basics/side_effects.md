# `SideEffects` - stockage des effets de bord
## Description
Cette classe est nécessaire au stockage des effets de bord.

Elle implémente une méthode `do` permettant à la classe [`SideEffectsManager`](side_effects_manager.md) d'exécuter la méthode appropriée.

## Méthodes
- `__init__()` &rarr; `None` \
  Méthode présente seulement à des fins de compatibilité.
- `do(side_effect_name, host)` &rarr; `None` \
  Exécute l'effet de bord `side_effect_name`, en lui passant le paramètre `host`. \
  Paramètres :
  * `side_effect_name` : *`str`*
  * `host` : *[`MapObject`](map_object.md)* \
    [`MapObject`](map_object.md) hôte de l'effet de bord.
>
> - `xxxxxxxxxxxxx(host)` &rarr; `None` \
>   Exemple de méthode d'effet de bord. \
>   Paramètre :
>   * `host` : *[`MapObject`](map_object.md)* \
>     [`MapObject`](map_object.md) hôte de l'effet de bord.