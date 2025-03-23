# `SoundMixer` - mixeur de sons
## Description
Les pas des personnages, la musique d'ambiance, etc. utilisent des sons pour contribuer à l'immersion du jeu. 
Ces sons doivent être mélangés pour être lus, ceci est effectué par un mixeur tel que celui de `Pygame` que 
nous avons étendu par cette classe qui permet entre autres d'ajuster le niveau du son en fonction de la distance du [`Player`](player.md).

Elle gère la lecture des [`SoundTrack`](sound_track.md) au sein de *channels* (canaux) qui permettent de les isoler.

## Attributs
- `sound_tracks` : *`list[`[`SoundTrack`](sound_track.md)`]`*
- `channels` : *`list`*
- `musics_historics` : *`list`*
- `music_coefficient` : *`float`* **set** \
  Volume de la musique, par défaut 0.25.
- `sound_coefficient` : *`float`* **set** \
  Volume des effets sonores, par défaut 1.0.
- `added_sfx` : *`dict`* \
  Effets sonores supplémentaires.
- `sfx_channel` : *`pygame.mixer.Channel`* \
  Canal utilisé pour les effets sonores supplémentaires.

## Méthodes
- `__init__()` &rarr; `None` \
  Initialise les attributs et charge les effets sonores supplémentaires.
- `add_sound_track(sound_track)` &rarr; `None` \
  Ajoute la [`SoundTrack`](sound_track.md) `sound_track`. \
  Paramètre :
  * `sound_track` : *[`SoundTrack`](sound_track.md)*
- `remove_sound_track(sound_track)` &rarr; `None` \
  Supprime la [`SoundTrack`](sound_track.md) `sound_track`. \
  Paramètre :
  * `sound_track` : *[`SoundTrack`](sound_track.md)*
- `find_channel()` &rarr; `pygame.mixer.Channel` \
  Renvoie un canal audio libre.
- `release_channel(channel)` &rarr; `None` \
  Libère le canal `channel`. \
  Paramètre :
  * `channel` : *`pygame.mixer.Channel`*
- `free_all_channels()` &rarr; `None` \
  Libère tous les canaux.
- `get_index_of_channel(channel)` &rarr; `int` \
  Renvoie l'index du canal `channel`. \
  Paramètre :
  * `channel` : *`pygame.mixer.Channel`*
- `generate_debug_data()` &rarr; `None` \
  Renvoie des données de débogage concernant les canaux occupés et leur contenu, pour [`LogHandler`](log_handler.md).
- `pause_music()` &rarr; `None` \
  Met la musique en pause.
- `unpause_music()` &rarr; `None` \
  Reprend la musique.
- `play_music(music_name)` &rarr; `None` \
  Charge et joue la musique nommée `music_name` indéfiniment. \
  Paramètre :
  * `music_name` : *`str`*
- `play_music_prev()` &rarr; `None` \
  Joue la musique précédente.
- `play_sfx(sfx_name, play_amount=0)` &rarr; `None` \
  Joue un effet sonore supplémentaire nommé `sfx_name`, `play_amount` fois. \
  Paramètres :
  * `sfx_name` : *`str`*
  * `play_amount` : *`int`*
- `update()` &rarr; `None` \
  Met à jour le volume des [`SoundTrack`](sound_track.md)s en fonction de leur distance avec le joueur.