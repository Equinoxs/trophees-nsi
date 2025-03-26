# `Building` - Les bâtiments vu de l'extérieur.

## Description

Cette classe représente les bâtiments vu de l'extérieur. Ils sont représentés par une image de bâtiment ainsi que d'une `hitbox` qui leur est associée dans les données de l'image.

Ses autres attributs étant initialisés selon ses classes parent, `Building` initialise sa hitbox de manière légèrement différente : les nombres renseignés dans la hitbox ne font pas référence à des positions statiques mais à des pourcentages de la hauteur et largeur du bâtiment.

> ```json
> {
> 	"height": 550,
> 	"hitbox": [[0, 50], [100, 50], [100, 98], [0, 98]],
> 	"hitbox_action_radius": 20,
> 	"door": {
> 		"name": "mansion_door",
> 		"interaction": "switch_door_mansion",
> 		"position": [78, 99]
> 	}
> }
> ``` 
> Exemple de données dans `data/assets/images/building/XXX/info.json`.

Comme vous pouvez le constater, une porte peut être rajoutée au `Building`. La position de la porte est également sous forme de pourcentages.
*Plus d'informations dans la [`documentation de Door`](door.md)

## Attributs
- `required_level` : *`int`* \
  Le niveau requis pour rentrer dans le bâtiment.

## Méthodes
- `__init__(data)` &rarr; `None` \
  Initialise la classe parent, la `hitbox` et la `Door` comme précisées ci-dessus. \
  Paramètre :
  * `data` : *`dict`*

- `get_data()` &rarr; `dict | None` \
  Renvoie les données de la classe parente en y ajoutant la clé `"required_level"`.
