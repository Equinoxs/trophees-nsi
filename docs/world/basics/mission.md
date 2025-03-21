# `Mission` - gestion des missions
## Description
Cette classe permet au jeu d'avoir une progression, grâce à des missions.

Chaque mission est composée d'une suite d'objectifs que le joueur doit atteindre pour la compléter.

Les missions permettent au joueur d'augmenter en niveau, en lui remettant une récompense lorsqu'elles sont terminées, 
pour ainsi débloquer d'autres missions. 

Les missions sont stockées dans le fichier `missions.py` adjacent à celui de cette classe. Il est composé d'une classe 
stockant les missions sous forme de méthodes représentant chacune un objectif.

## Attributs
- `name` : *`str`* **get**
- `description` : *`str`* **get**
- `required_level` : *`str`* **get** \
  Niveau requis pour lancer la mission.
- `rewards` : *`list`* **get** \
  Récompenses de la mission.
- `objective_len` : *`int`* **get** \
  Quantité d'objectifs de la mission.
- `objective_index` : *`int`* **get** \
  Indice de l'objectif en cours.
- `indicator` : *`int`* \
  Indicateur du statut de la mission. 1 : réussie, 0 : en cours, -1 : ratée.
- `displayed_description` : *`str`* \
  Description affichée à l'écran.

## Méthodes
- `__init__(mission_data, name)` &rarr; `None` \
  Initialise les attributs en fonction de `mission_data` et le nom de la mission. \
  Paramètres : 
  * `mission_data` : *`dict`* \
    Données d'initialisation.
  * `name` : *`str`*

- `display_objective_description()` &rarr; `None` \
  Affiche la description de l'objectif en cours.

- `delete_objective_description()` &rarr; `None` \
  Efface la description affichée à l'écran.
- `update()` &rarr; `int` \
  Méthode exécutée à chaque rafraîchissement du jeu, permet de mettre à jour le statut de la mission en cours.
  Renvoie le statut de la mission.