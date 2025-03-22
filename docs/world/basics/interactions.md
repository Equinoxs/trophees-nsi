# `Interactions` - stockage des interactions
## Description
Cette classe est nécessaire au stockage des interactions.

Elle implémente une méthode `do` permettant à la classe [`Interactable`](interactable.md) d'exécuter la méthode appropriée.

## Méthodes
- `__init__()` &rarr; `None` \
  Méthode présente seulement à des fins de compatibilité.
- `do(interaction_name, host)` &rarr; `None` \
  Exécute l'interaction `interaction_name`, en lui passant le paramètre `host`. \
  Paramètres :
  * `interaction_name` : *`str`*
  * `host` : *[`Interactable`](interactable.md)* \
    [`Interactable`](interactable.md) hôte de l'interaction.
>
> - `xxxxxxxxxxxxx(host)` &rarr; `None` \
>   Exemple de méthode d'interaction. \
>   Paramètre :
>   * `host` : *[`Interactable`](interactable.md)* \
>     [`Interactable`](interactable.md) hôte de l'interaction.