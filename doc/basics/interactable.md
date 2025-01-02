# `Interactable` - gestion des interactions avec le joueur
## Description
Cette classe est nécessaire aux classes enfant pour avoir une interaction avec le `Player`.

En fournissant une méthode unique à appeler lors de l'interaction, elle exécute une action spécifique à la classe enfant.

Les fonctions exécutées lors des interactions sont stockées dans le dictionnaire `interactions` dans le fichier `data_functions`,
et celle associée à la classe enfant est assignée à l'initialisation en fonction des données du fichier JSON.

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