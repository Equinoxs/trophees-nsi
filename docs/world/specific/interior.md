# `Interior` - L'intérieur d'un bâtiment, un alternative à [`GroundSurface`](ground_surface.md).

## Description

Cette classe est nécessaire pour représenter un intérieur de bâtiment à partir d'**une seule image**.

Pour cela, elle se base sur les données de l'image pour en extraire les boundaries, utiles pour savoir quand produire un son à la marche d'un personnage. On peut aussi savoir la hauteur de cette image.

Cette classe hérite ainsi de [`GroundSurface`](ground_surface.md) afin de profiter de sa gestion habile des `boundaries` et du son qui va avec.

> ```json
> {
> 	"height": 500,
> 	"type": "hallway",
> 	"boundaries": [[0, 0], [700, 0], [700, 500], [0, 500]]
> }
> ```
> Exemple de données d'image pour cette classe.

## Attributs
- `boundaries` : *`list[Vector2]`* \
  Les coordonnées de l'intérieur.

## Méthodes
- `__init__(data)` &rarr; `None` \
  Initialise les classes parent et les boundaries. \
  Paramètre :
  * `data` : *`dict`*
