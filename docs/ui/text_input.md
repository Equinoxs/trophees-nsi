# `TextInput` - gestion de l'entrée utilisateur
## Description
Cette classe est nécessaire pour entrer du texte.

Elle permet d'afficher une case remplissable avec du texte.

Elle dérive de [`UIElement`](ui_element.md), se référer à sa documentation pour les attributs et méthodes surchargés.

## Attributs
- `text` : *`str`* **get**
- `first_input` : *`bool`* \
  Indique si c'est la première fois que l'utilisateur tape dans le champ.
- `focus` : *`bool`* \
  Indique si l'utilisateur édite le champ.
- `replace` : *`bool`* \
  Indique si le texte par défaut du champ doit être remplacé (*placeholder*).
- `underscore` : *`bool`* \
  Indique si un underscore (_) doit être concaténé au texte entré par l'utilisateur.
- `done_func` : *`function`* **get/set** \
  Fonction exécutée lors de l'appui de la touche entrée indiquant si l'entrée utilisateur est terminée.
- `intercept` : *`str`* \
  Indique le type de données à intercepter (`keys` pour des touches de clavier ou `text` pour du texte).
- `last_event_key` : `int` \
  Dernière touche appuyée par l'utilisateur.
- `event_name` : *`str`*
- `max_event_key` : *`int`* \
  Longueur maximale du champ.

## Méthodes
- `__init__(data)` &rarr; `None` \
  Initialise les attributs et [`UIElement`](ui_element.md).
  Paramètre :
  * `data` : *`dict`* \
    Données pour configurer l'élément.
- `done()` &rarr; `None` \
  Appelle la fonction stockée dans `done_func` si elle est définie.
- `update_label()` &rarr; `None` \
  Met à jour le `label` de `UIElement` en fonction de l'entrée utilisateur.
- `empty_text()` &rarr; `None` \
  Remet à zéro le texte de la case.
- `set_text(new_text)` &rarr; `None` \
  Met le texte du champ à `new_text` et met à jour le `label` de `UIElement`.
- `update()` &rarr; `None` \
  Si l'élément est actif (il a été cliqué précédemment), met à jour son contenu :
  * avec le nom de la touche appuyée si `intercept` vaut `keys` ;
  * avec la touche appuyée si `intercept` vaut `text`.
- `render()` &rarr; `None` \
  Affiche la case à l'écran et dessine une bordure blanche si celle-ci est active et grise sinon.
