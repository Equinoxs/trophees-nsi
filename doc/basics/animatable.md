# `Animatable` - gestion de l'animation des `Sprite`
## Description
Cette classe permet aux `Sprite` d'avoir une animation. Celle-ci est composée de plusieurs *frames*, rassemblées dans **une seule** image, et placées côte à côte. Chaque ligne de l'image représente une animation différente. 
>![Animation](/sources/assets/images/npc/nathan/image.png) \
> *Exemple d'image d'animation.*

Les informations de l'animation sont présentes dans le fichier `info.json` associé. Chaque entrée du dictionnaire des animations représente une ligne de l'image et chaque entrée du tableau `widths` représente une *frame* de l'animation. 
> ```json
> {
> 	"animations": {
> 		"inactive": {
> 			"widths":[
> 				{ "width": 44, "time": 1000 }
> 			],
> 			"height": 93
> 		},
> 		"walking_forward": {
> 			"widths": [
> 				{ "width": 43, "time": 0.2 },
> 				{ "width": 43, "time": 0.2 },
> 				{ "width": 43, "time": 0.2 },
> 				{ "width": 43, "time": 0.2 },
> 				{ "width": 43, "time": 0.2 }
> 			],
> 			"height": 95
> 		},
>         ...
> 	},
> }
> ```
> *Exemple de fichier `info.json`*

## Attributs
- `animation_running` : *`bool`* \
  Indique si l'animation tourne.
- `frame_index` : *`int`* \
  L'index de la *frame* actuelle.
- `infinite` : *`bool`*
- `animation_name` : *`str`*
- `dt` : *`float`* \
  &Delta;t. Le temps depuis la dernière mise à jour de l'animation.
- `animation_sound_name` : *`str`* \
  Le nom du son à jouer pendant l'animation.
- `image_path` : *`str`*
- `animations` : *`dict`* \
  Les informations sur les différentes animations, chargées depuis `info.json`.

## Méthodes
- `__init__(position, image_path)` \
  Initialise les attributs. \
  Paramètre :
  * `image_path` : *`str`* \
    Chemin de l'image à charger.
- `set_animation_sound_name(sound_name)` \
  Change ou arrête **manuellement** le son de l'animation en cours.
  Paramètres :
  * `sound_name` : *`str`*
- `change_animation(animation_name, force)` \
  Change l'animation en cours vers une animation différente.
  Paramètres :
  * `animation_name` : *`str`*
  * `force` : *`bool`* \
  Force le changement même si l'animation cible est celle en cours.
- `stop_animation()` \
  Arrête l'animation en cours.
- `resume_animation()` \
  Reprend l'animation précédemment arrêtée.
- `reset_animation_state()` \
  Remet l'animation en cours à zéro.
- `update_animation_index()` \
  Méthode exécutée à chaque boucle du jeu, permet de mettre à jour l'état de l'animation.
