# `ButtonActions` - stockage des actions des boutons
## Description
Cette classe est nécessaire au stockage des actions lors du clic des boutons.

Elle implémente une méthode `do` permettant à la classe `Button` d'exécuter la méthode appropriée.

## Méthodes
- `__init__()` &rarr; `None` \
  Méthode présente seulement à des fins de compatibilité.
- `do(action_name, button=None)`  &rarr; `None` \
  Exécute l'action `action_name`, en lui passant le paramètre `button`. \
  Paramètres :
  * `action_name` : *`str`*
  * `button` : *`Button`* \
    Bouton originaire de l'action.
>
> - `xxxxxxxxxxxxx(button)` &rarr; `None` \
>   Exemple de méthode d'action. \
>   Paramètre :
>   * `button` : *`Button`* \
>     Bouton originaire de l'action.