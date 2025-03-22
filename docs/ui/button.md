# `Button` - bouton
## Description
Cette classe est nécessaire à l'affichage des boutons dans les menus.

Elle permet d'appeler une méthode définie lors du clic de l'utilisateur.

Elle dérive de [`UIElement`](ui_element.md) et charge les méthodes *callback* depuis [`ButtonActions`](button_actions.md).

## Attributs
- `action_name` : *`str`*

## Méthodes
- `__init__(data)` &rarr; `None` \
  Initialise `UIElement` et l'attribut. \
  Paramètre :
  * `data` : *`dict`* \
    Données pour configurer l'élément.

- `update()` &rarr; `bool` \
  Vérifie si le bouton est cliqué et si oui, appelle la méthode appropriée.
  Renvoie `True` si le bouton est cliqué et `False` sinon. \
