# `Interactable` - gestion des interactions et des missions avec le joueur
## Description
Cette classe est nécessaire aux classes enfant pour avoir une interaction avec le `Player` ainsi que des missions.

En fournissant une méthode unique à appeler lors de l'interaction, elle exécute une action spécifique à la classe enfant, elle fait de même pour les missions.

Les fonctions exécutées lors des interactions sont stockées dans la classe [`Interactions`](interactions/md), ces intéractions sont crées au besoin, c'est pareil pour les missions mais les fonctions de mission sont créées dans [`Missions`](missions.md), elle ne peut n'avoir qu'une mission à la fois.

Les indicateurs d'interaction et de mission son gérés par cette classe

## Attribut
- `interaction` : *`str`* **get / set**  \
  Nom de la méthode de `Interactions` à exécuter lors de l'interaction.
- `interaction_marker` : *`str`* \
  Le popup qui indique que l'on peut intéragir avec un élélement.
- `interaction_available` : *`str`* **set** \
  Savoir si l'interaction peut être exécuté.
- `interaction_force` : *`str`* \
  Savoir si l'interaction doit être exécuté même si `interaction_available` dit le contraire.
- `mission` : *`str`* **get / set** \
  Nom de la mission à exécuter.
- `mission_marker` : *`str`* \
  Le marker de la mission.

## Méthodes
- `__init__(interaction, mission)` \
  Initialise la fonction d'interaction et celle de mission. \
  Paramètres :
  * `interaction` : *`str`*
  * `mission` : *`str`*
- `handle_interaction(closest_vector)` &rarr; `None` \
  Exécute l'interaction **si** le `Sprite` est proche du `Player` et **si** la touche d'interaction est appuyée. \
  Paramètre :
  * `closest_vector` : *`Vector2`* \
    `Vector2` représentant la distance du `Player` au point le plus proche de la *hitbox* de ce `Sprite`.
- `is_interaction_available()` &rarr; `bool` \
  Retourne si l'interaction peut être exécuté ou pas
- `is_mission_available()` &rarr; `bool` \
  Pareil mais pour la mission.
- `catch_event(event)` &rarr; `None` \
  Regarde si un mission a été accomplie, si oui et que c'est sa mission, elle est retirée et réglée à `None`.
- `update()` &rarr; `None` \
  Gère l'état de ses différents attributs en fonction de ce qui se passe dans le jeu.
- `__del__()` \
  Supprime `interaction_marker` et `mission_marker`.
