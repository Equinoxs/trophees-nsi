# `Interactable` - gestion des interactions des `Sprite` avec le joueur
## Description
Cette classe permet à un `Sprite` d'exécuter une action lorsque le `Player` interagit avec lui par l'appui de la touche associée.

Ces fonctions sont stockées dans le fichier `data_functions`, et celle associée au `Sprite` est récupérée à l'initialisation.
## Attribut
- `interaction` : *`function`* \
  Fonction à exécuter lors de l'interaction.

## Méthodes
- `__init__(interaction)` \
  Initialise la fonction d'interaction. \
  Paramètre :
  * `interaction` : *`function`*
- `handle_interaction(closest_vector)` \
  Exécute l'interaction **si** le `Sprite` est proche du `Player` et la touche est appuyée. \
  Paramètre :
  * `closest_vector` : *`Vector2`* \
    `Vector2` représentant la distance du `Player` au point le plus proche de la *hitbox* de ce `Sprite`.