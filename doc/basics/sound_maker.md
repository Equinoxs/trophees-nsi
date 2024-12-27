# `SoundMaker` - gestion du son des `Sprite`
## Description
Cette classe permet aux `Sprite` d'émettre un son, en leur fournissant une ou plusieurs `SoundTrack`. Celles-ci sont séparées en types, comme `footsteps` ou `voices`.

Un `Sprite` ne peut émettre qu'un son de chaque type à la fois. Par exemple, il n'est pas possible pour le `Player` de marcher à la fois sur du parquet et dans des feuilles, donc on ne peut pas jouer les sons `walking_wooden` et `walking_leaves` en même temps.

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
- `all_sound_tracks` : *`dict`* \
  Toutes les `SoundTrack` instanciées. Permet au `Player` de pouvoir jouer toutes les `SoundTrack`.
- `sound_tracks` : *`dict`* \
  Les `SoundTrack` utilisées par ce `Sprite`. 

## Méthodes
- `__init__(position = None, authorized_sound_tracks = [])` \
  Initialise toutes les `SoundTrack`. \
  Paramètres :
  * `position` : *`Vector2`* \
    Ce paramètre est défini dans les classes filles par `Sprite` et n'est dans cette classe que pour assurer la compatibilité du code.
  * `authorized_sound_tracks` : *`list`* \
    Indique les types de `SoundTrack` autorisés pour ce `Sprite`.
- `play_sound(sound_name, loop)` \
  Lit un son. \
  Paramètres : 
  * `sound_name`: *`str`* 
  * `loop` : *`bool`* \
    Indique si le son est joué en boucle.
- `stop_sound(sound_name)` \
  Arrête un son en cours de lecture. \
  Paramètres :
  * `sound_name` : *`str`*
- `stop_sound_track(sound_name)` \
  Arrête une `SoundTrack` contenant un son en cours de lecture manuellement. \
  Paramètres :
  * `sound_track_name` : *`str`*
- `remove_sound_track(sound_name)` \
  Supprime une `SoundTrack` manuellement. \
  Paramètres :
  * `sound_track_name` : *`str`*
- `pause(sound_type)` \
  Met un son en cours de lecture en pause. \
  Paramètres : 
  * `sound_type`: *`str`*
- `unpause(sound_type)` \
  Relance un son en pause. \
  Paramètres : 
  * `sound_type`: *`str`*
- `get_busy(sound_type)` \
  Renvoie `True` si un son de du type de `sound_type` est en cours de lecture. \
  Paramètres : 
  * `sound_type`: *`str`*
- `is_sound_loaded(sound_type)` \
  Renvoie `True` si un son de du type de `sound_type` est chargé en mémoire. \
  Paramètres : 
  * `sound_type`: *`str`*
- `gimme_all_sound_tracks(sound_type)` \
  Récupère toutes les `SoundTrack` instanciées.
- `dont_gimme_all_sound_tracks(sound_type)` \
  Arrête et efface toutes les `SoundTrack` instanciées.
