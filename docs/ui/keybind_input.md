## `KeybindInput` - gestion des associations de touches
## Description
Cette classe est nécessaire à la mise à jour des associations de touches de [`ControlHandler`](../utils/control_handler.md).

Elle récupère la touche entrée par l'utilisateur et met à jour [`ControlHandler`](../utils/control_handler.md) en conséquence.

Elle dérive de [`TextInput`](text_input.md), se référer à sa documentation pour les attributs et méthodes surchargés.

## Attributs
- `intercept` : *`str`* \
  Vaut `keys` car les touches sont interprétées et non le texte.
- `max_event_key` : *`int`* \
  Vaut `1` car une seule touche est demandée.

## Méthodes
- `__init__(data)` &rarr; `None` \
  Initialise les attributs et [`TextInput`](text_input.md).
  Paramètre :
  * `data` : *`dict`* \
    Données pour configurer l'élément.
- `done()` &rarr; `None` \
  Vérifie si une touche a été entrée et si oui, met à jour [`ControlHandler`](../utils/control_handler.md) en conséquence.
