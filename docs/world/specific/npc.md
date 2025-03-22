# `NPC` - Les personnages non-joueur

## Description

Cette classe est nécessaire afin de donner de la vie au jeu.
Grâce à elle, le monde est rempli de personnages fascinants à qui parler.

Les personnages peuvent se déplacer vers un objectif et effectuer une série de tâches pour leur donner une sorte d'animation.

> ```json
> {
> 	"type": "NPC",
> 	"name": "house_proprietary",
> 	"pattern_timeline": [[650, 1300], "npc_event_test", [700, 1110]],
> 	"pattern_type": "back_and_forth",
> 	"position": [670, 1200],
> 	"image_path": "albert",
> 	"mission": "mission_test",
> 	"authorized_sound_tracks": ["footsteps", "voices"],
> 	"side_effects": ["visit_player"],
> 	"sound": "hey"
> }
> ```
> Exemple exhaustif de dictionnaire d'initialisation d'un PNJ.

Les informations nécessaires à ces parcours prédéfinis sont stockées dans les propriétés `"pattern_timeline"` et `"pattern_type"`.

Dans `"pattern_timeline"`, lorsqu'il y a un couple de point, cela signifie un déplacement, lorsqu'il y a une chaîne de caractère, le PNJ effectue l'action spécifiée dans [`PatternEvents`](pattern_events.md).

## Attributs
- `initial_position` : *`Vector2`* \
  Copie de la position initiale du PNJ.
- `sprint` : *`bool`* \
  Indique si le PNJ est en train de courir.
- `is_player` : *`bool`* **set** \
  Indique si le PNJ est en fait le joueur principal.
- `speed` : *`float`* \
  Sa vitesse en m/s.
- `walking_on` : *`str | None`* \
  Ce sur quoi marche le personnage.
- `level` : *`int`* **get / set** \
  Le niveau du PNJ

- `pattern_timeline` : *`list[Vector2 | str]`* \
  Le pattern du PNJ.
- `pattern` : *`list[Vector2]`* \
  Le pattern avec uniquement les positions, sans les évènements.
- `following_pattern` : *`bool`* **set** \
  Indique si le personnage est en train de suivre son pattern.
- `pattern_index` : *`int`* \
  L'index du pattern.
- `pattern_type` : *`str`* \
  Indique comment le PNJ effectue son pattern, valeurs possibles : `"back_and_forth"` ou `"loop"`

- `objective` : *`Vector2`* **set** \
  Position vers laquelle le PNJ doit se déplacer.

- `is_moving` : *`bool`* \
  Permet de savoir si le PNJ se déplace.
- `must_move` : *`bool`* **get / set** \
  Permet de contrôler si le PNJ a le droit de se déplacer ou non.

- `inventory` : *`InventoryItem | None`* **get** \
  L'inventaire du joueur (=l'item que le joueur porte sur lui)
- `sound` : *`str`* **get** \
  Le son que fait le PNJ lorsqu'il a un certain [side effect](../basics/side_effects.md)

## Méthodes
- `__init__(data)` &rarr; `None`
  Initialise simplement ses attributs ainsi que sa classe parent.
  Paramètre :
  * `data` : *`dict`*
  Le dictionnaire d'initialisation du PNJ.

- `go_initial()` &rarr; `None`
  Fait retourner le PNJ à sa position d'origine

- `turn_right()` &rarr; `None`
  Le PNJ tourne à droite.

- `turn_left()` &rarr; `None`
  Le PNJ tourne à gauche.

- `update_player()` &rarr; `None`
  Une fonction pour actualiser l'état du joueur si `is_player` est à *`True`*.

- `set_objective(new_objective)` &rarr; `None`
  Règle une nouvelle position pour le pnj.
  Paramètre :
  * `new_objective` : *`Vector2 | None`*
  Vers où le PNJ doit aller.

- `stop_moving()` &rarr; `None`
  Arrête le déplacement du personnage.

- `stop_moving()` &rarr; `None`
  Annule la méthode ci-dessus.

- `handle_animation()` &rarr; `None`
  Gère les animations du personnage en fonction de son dernier déplacement.
  Annule la méthode ci-dessus.

- `move_npc_to_objective()` &rarr; `bool`
  Se charge de bouger le PNJ vers son objectif, retourne *`True`* si le personnage s'est déplacé, *`False`* sinon.

- `handle_events()` &rarr; `bool`
  Vérifie si un pattern event doit être effectué, si oui, on l'exécute et on retourne *`True`*, *`False`* sinon.

- `update_pattern()` &rarr; `None`
  Se charge du bon déroulement de `pattern_timeline` et gère donc les appels de `handle_events()` et `move_npc_to_objective()`.

- `purge_inventory()` &rarr; `None`
  Règle l'inventaire du joueur à *`None`*.

- `pick_item(item)` &rarr; `None`
  Récupère l'item renseigné dans l'inventaire.
  Paramètre :
  * `item` : *`InventoryItem`*
  l'item en question.

- `drop_inventory()` &rarr; `None`
  Lâche l'inventaire au sol.

- `handle_invnetory()` &rarr; `None`
  Gère l'état de l'inventaire si le personnage est contrôlé par le joueur.

- `give_inventory_to(table, index_position)` &rarr; `None`
  Lâche l'inventaire sur une [`Table`](table.md).
  Paramètres :
  * `table` : *`Table`*
  La table destinataire de l'inventaire.
  * `index_position` : *`int`*
  La position de l'item sur la table.

- `update()` &rarr; `None`
  Actualise l'état du PNJ en coordonnant ses différentes activités (inventaire, pattern, joueur).

- `render()` &rarr; `None`
  Fais en sorte que la position du joueur soit au niveau de ses pieds.

- `get_data()` &rarr; `None`
  Retourne la data de la classe parent et y ajoute l'inventaire.
