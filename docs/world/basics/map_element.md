# `MapElement` - éléments visuels de la `Map`

## Description
### Hérite de : `Sprite`, `SoundMaker`, `Animatable`

Cette classe est nécessaire pour afficher les classes enfant sur la `Map` de manière structurée.

Elle permet d'être parente à tous les éléments du jeu, en rassemblant les fonctionnalités de `Sprite`, `SoundMaker` et `Animatable`.

Elle peut être "kill", à ce moment là, elle n'existe plus dans la carte et n'est plus sauvegardée.

Elle reçoit un `dict` dans osn initialisation qui comporte plusieurs propriétés sur l'objet :

> ```json
> {
>   "type": "Tree",
>   "name": "example_tree",
>   "position": [125, 350],
>   "image_path": "oak"
> }
> ```
> Exemple **non exhaustif** d'un dictionnaire d'initialisation

Ici, le `type` renvoie à la class de l'objet, et le reste des propriétés est spécifique à son type.

## Attributs
- `name` : *`str`* **get**
  Son nom unique, utile pour le rechercher
- `killed` : *`bool`* **get / set**
  Indique si l'objet est tué
- `data` : *`dict`* **get** \
  Données servant à la sauvegarde.

## Méthodes
- `__init__(data)` &rarr; `None` \
  Initialise les classes parentes et les attributs
  en fonction de `data`, fourni par `DataHandler` en fonction du fichier JSON. \
  Paramètre :
  * `data` : *`dict`*

- `kill()` &rarr; `None` \
  Tue l'instance en question.

- `catch_event(event)` &rarr; `None` \
  Méthode permettant l'utilisation de mécanismes à interruptions. \
  Paramètre :
  * `event` : *`object`*

- `update()` &rarr; `None` \
  Méthode exécutée à chaque rafraîchissement du jeu, permet de mettre à jour l'image affichée en fonction de l'animation.

- `__del____()` &rarr; `None` \
  Appelle le destructeur de [`SoundMaker`](sound_maker.md).

- `get_data()` &rarr; `None` \
  Retourne les données sauvegardables de l'objet.
