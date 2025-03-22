# `Button` - bouton
## Description
Cette classe répond à un besoin d'intéraction avec l'utilisateur.

C'est un [`UIElement`](ui_element.md) qui permet d'appeler une méthode définie lors du clic de l'utilisateur.

Elle dérive donc de `UIElement` et charge les méthodes *callback* depuis [`ButtonActions`](button_actions.md).

Elle prend le nom de la méthode de la méthode de `ButtonActions` à appeler dans la propriété `"action"` dans son dictionnaire fournie en entrée.

## Attributs
- `action_name` : *`str`* **get**
  le nom de l'intéraction du bouton

## Méthodes
- `__init__(data)` &rarr; `None` \
  Initialise `UIElement` et l'attribut `action_name`. \
  Paramètre :
  * `data` : *`dict`* \
    Données pour configurer l'élément.

- `update()` &rarr; `bool` \
  Vérifie si le bouton est cliqué et si oui, appelle la méthode appropriée.
  Renvoie `True` si le bouton est survolé par la souris et `False` sinon.
  Cela sert à la gestion du curseur de la souris (son icône).
