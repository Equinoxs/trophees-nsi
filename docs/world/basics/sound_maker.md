# `SoundMaker` - gestion du son
## Description
Cette classe est nécessaire aux classes enfant pour pouvoir émettre du son.

En fournissant une interface indirecte aux [`SoundTrack`](../../utils/sound_track.md), elle leur permet de ne pas les manipuler directement pour une gestion plus simple et moins sujette aux erreurs. 

Elle permet à ses classes enfant de jouer un son à partir de son nom, en gérant la création de l'objet [`SoundTrack`](../../utils/sound_track.md) associé, et son stockage afin de ne pas le ré-instancier. 

De plus, elle implémente un système de type de son empêchant plusieurs sons de se jouer en même temps si cela est incohérent. 

Les sons sont rangés dans un dossier indiquant leur type, comme `footsteps` ou `animals`, qui contient **un** fichier `info.json` indiquant tous les sons de ce type et leur extension. 
>```json
>{
>	"sounds": {
>		"walking_leaves": {
>			"extension": "mp3"
>		},
>		"walking_concrete": {
>			"extension": "opus"
>		},
>		...
>	}
>}
>```
>*Exemple de fichier `info.json`*

## Attributs
- `position` : *`Vector2`*
- `all_sound_tracks` : *`dict`* \
  Toutes les [`SoundTrack`](../../utils/sound_track.md) instanciées. Permet au `Player` de pouvoir jouer toutes les [`SoundTrack`](../../utils/sound_track.md).
- `sound_tracks` : *`dict`* \
  Les [`SoundTrack`](../../utils/sound_track.md) utilisées par la classe enfant. 

## Méthodes
- `__init__(position=None, authorized_sound_tracks=[])` &rarr; `None` \
  Instancie toutes les [`SoundTrack`](../../utils/sound_track.md) des types spécifiés dans `authorized_sound_tracks`. \
  Paramètres :
  * `position` : *`Vector2`* \
    Ce paramètre est défini dans les classes enfant par `Sprite` et n'est dans cette classe que pour assurer la compatibilité du code.
  * `authorized_sound_tracks` : *`list`* \
    Indique les types de [`SoundTrack`](../../utils/sound_track.md) autorisés pour cette classe enfant.

- `play_sound(sound_name, loop)` &rarr; `None` \
  Lit un son. \
  Paramètres : 
  * `sound_name`: *`str`* 
  * `loop` : *`bool`* \
    Indique si le son est joué en boucle.

- `stop_sound(sound_name)` &rarr; `None` \
  Arrête un son en cours de lecture. \
  Paramètre :
  * `sound_name` : *`str`*

- `stop_sound_track(sound_name)` &rarr; `None` \
  Arrête une [`SoundTrack`](../../utils/sound_track.md) contenant un son en cours de lecture manuellement. \
  Paramètre :
  * `sound_track_name` : *`str`*

- `remove_sound_track(sound_name)` &rarr; `None` \
  Supprime une [`SoundTrack`](../../utils/sound_track.md) manuellement. \
  Paramètre :
  * `sound_track_name` : *`str`*

- `pause(sound_type)` &rarr; `None` \
  Met un son en cours de lecture en pause. \
  Paramètre : 
  * `sound_type`: *`str`*

- `unpause(sound_type)` &rarr; `None` \
  Relance un son en pause. \
  Paramètre : 
  * `sound_type`: *`str`*

- `get_busy(sound_type)` &rarr; `bool` \
  Renvoie `True` si un son de du type de `sound_type` est en cours de lecture. \
  Paramètre : 
  * `sound_type`: *`str`*

- `is_sound_loaded(sound_type)` &rarr; `bool` \
  Renvoie `True` si un son de du type de `sound_type` est chargé en mémoire. \
  Paramètre : 
  * `sound_type`: *`str`*

- `gimme_all_sound_tracks(sound_type)` &rarr; `None` \
  Récupère toutes les [`SoundTrack`](../../utils/sound_track.md) du type `sound_type` instanciées et les stocke dans `all_sound_tracks`. \
  Paramètre :
  * `sound_type` : *`str`*

- `dont_gimme_all_sound_tracks(sound_type)` &rarr; `None` \
  Arrête et efface toutes les [`SoundTrack`](../../utils/sound_track.md) du type `sound_type` instanciées stockées dans `all_sound_tracks`. \
  Paramètre :
  * `sound_type` : *`str`*

- `update()` &rarr; `None` \
  Méthode seulement présente pour assurer une compatibilité de code.