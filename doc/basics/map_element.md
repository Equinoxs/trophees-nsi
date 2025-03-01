# `MapElement` - éléments visuels de la `Map`

## Description
### Hérite de : `Sprite`, `SoundMaker`, `Animatable`

Cette classe est nécessaire pour afficher les classes enfant sur la `Map` de manière structurée.

Elle permet d'être parente à tous les éléments du jeu, en rassemblant les fonctionnalités de `Sprite`, `SoundMaker` et `Animatable`.

Elle implémente un `z_index` comparable à celui du langage CSS, pour gérer les niveaux de l'axe Z,
et un nom associé à l'instance.

## Attributs
- `z_index` : *`int`* **get / set** \
  Niveau de l'axe Z.
- `z_indexes_history` : *`list[int]`* \
  Historique des valeurs de `z_index` de l'instance courante.
- `name` : *`str`* **get**
- `data` : *`dict`* **get** \
  Données servant à la sauvegarde.

## Méthodes
- `__init__(data)` &rarr; `None` \
  Initialise les classes parentes et les attributs
  en fonction de `data`, fourni par `DataHandler` en fonction du fichier JSON. \
  Paramètre :
  * `data` : *`dict`*

- `set_z_index_prev()` &rarr; `None` \
  Associe la valeur du précédent `z_index` à l'attribut `z_index`.

- `catch_event(event)` &rarr; `None` \
  Méthode permettant l'utilisation de mécanismes à interruptions. \
  Paramètre :
  * `event` : *`object`*

- `update()` &rarr; `None` \
  Méthode exécutée à chaque rafraîchissement du jeu, permet de mettre à jour l'image affichée en fonction de l'animation.

- `render()` &rarr; `bool` \
  Méthode appelée par `Camera` pour effectuer le rendu. Renvoie un booléen indiquant si le rendu a été effectué ou pas.
