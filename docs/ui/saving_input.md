# `SavingInput` - case de texte servant à sauvegarder
## Description
Cette classe représente un [`Button`](button.md) servant à sauvegarder le jeu.

Elle dérive de [`Button`](button.md), se référer à sa documentation pour les attributs et méthodes surchargés.

## Attribut
- `active_input` : *[`SavingInput`](#)* \
  Représente l'instance en cours, de sorte à ce qu'une seule instance soit créée.

## Méthodes
- `__init__(data)` &rarr; `None` \
  Initialise [`Button`](button.md) et l'attribut. \
  Paramètre :
  * `data` : *`dict`* \
    Données pour configurer l'élément.
- `done()` &rarr; `None` \
  Méthode appelant l'action `save_game` lorsque la saisie est terminée.