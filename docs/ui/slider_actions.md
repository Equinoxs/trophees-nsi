# `ButtonActions` - stockage des actions des boutons
## Description
Cette classe est nécessaire au stockage des actions lors du déplacement des [`Slider`](slider.md).

Elle implémente une méthode `do` permettant à la classe [`Slider`](slider.md) d'exécuter la méthode appropriée.

## Méthodes
- `__init__()` &rarr; `None` \
  Méthode présente seulement à des fins de compatibilité.
- `do(action_name, value=None)`  &rarr; `None` \
  Exécute l'action `action_name`, en lui passant le paramètre `value`. \
  Paramètres :
  * `action_name` : *`str`*
  * `value` : *`float`* \
    Valeur du [`Slider`](slider.md) au moment de l'appel.
>
> - `xxxxxxxxxxxxx(value)` &rarr; `None` \
>   Exemple de méthode d'action. \
>   Paramètre :
>   * `value` : *`float`* \
>     Valeur du [`Slider`](slider.md) au moment de l'appel.