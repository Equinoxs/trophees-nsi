# `LogHandler` - gestion des journaux
## Description
Cette classe est nécessaire au développement et au débogage du jeu.
Elle ne sert que lorsque la variable `DEBUG` est à *`True`*.

Elle permet de laisser des traces de tout le fonctionnement du jeu.

Elle est appelée par une multitude de classes et affiche à l'écran et dans la console les messages.

## Attributs
- `log` : *`list`* \
  Journaux par ordre d'ajout.
- `length` : *`int`* **set** \
  Longueur des journaux à afficher à l'écran.

## Méthodes
- `__init__()` &rarr; `None` \
  Initialise les attributs.

- `add(*args)` &rarr; `None` \
  ∀ n ∈ ℕ, ajoute les n paramètres à la liste des journaux. \
  Paramètre(s) :
  * `*args`

- `get_log()` &rarr; `list` \
  Renvoie la liste des logs précédée d'un en-tête.

- `render()` &rarr; `None` \
  Affiche la fenêtre de journaux à l'écran.
