# `SoundTrack` - piste audio
## Description
Cette classe représente les sons joués dans le jeu, s'agissant de la musique ou bien d'effets sonores,
avec une instance par "type" de son, par exemple les bruits de pas,
et contenant tous les fichiers sonores correspondant à ceux-ci.

Elle contient une référence vers un fichier et étend les fonctionnalités de la classe `Sound` de `Pygame.mixer`, 
en l'initialisant à partir des données fournies par [`DataHandler`](data_handler.md).

## Attributs
- `sounds` : *`dict[str, pygame.mixer.Sound]`*
- `current_sound_name` : *`str`
- `position` : *[`Vector2`](vector_2.md)* **get**
- `channel` : *`pygame.mixer.Channel`*
- `paused` : *`bool`* **get**
- `play_amount` : *`int`* **get** \
  Nombre de lectures.
- `data` : *`dict`* \
  Fournies par [`DataHandler`](data_handler.md).

## Méthodes
- `__init__(position, data, sound_paths)` &rarr; `None` \
  Initialise les attributs, instancie les `sounds` à partir des `sound_paths`, trouve un canal et s'enregistre auprès 
  de [`SoundMixer`](sound_mixer.md). \
  Paramètres :
  * `position` : *`Vector2`*
  * `data` : *`dict`*
  * `sound_paths` : *`list[str]`*
- `contains(sound_name)` &rarr; `bool` \
  Renvoie `True` si le son nommé `sound_name` fait partie de cette instance. \
  Paramètres :
  * `sound_name` : *`str`*
- `play(sound_name, loop)` &rarr; `None` \
  Joue le son nommé `sound_name` indéfiniment si `loop` vaut `True` et une fois sinon. \
  Paramètres :
  * `sound_name` : *`str`*
  * `loop` : *`bool`*
- `get_sound_coef(sound_name)` &rarr; `None` \
  Renvoie le coefficient du son nommé `sound_name`, c'est-à-dire le volume absolu, qui sera ensuite ajusté en fonction
  de la distance du joueur. \
  Paramètre :
  * `sound_name` : *`str`*
- `stop(sound_name)` &rarr; `None` \
  Arrête le son nommé `sound_name`. \
  Paramètres :
  * `sound_name` : *`str`*
- `pause(sound_name)` &rarr; `None` \
  Met le son nommé `sound_name` en pause. \
  Paramètres :
  * `sound_name` : *`str`*
- `unpause(sound_name)` &rarr; `None` \
  Reprend le son nommé `sound_name`. \
  Paramètres :
  * `sound_name` : *`str`*
- `set_volume(volume)` &rarr; `None` \
  Met le volume à `volume`. \
  Paramètre :
  * `volume` : *`float`*
- `get_busy()` &rarr; `bool` \
  Renvoie `True` si une lecture est en cours et `False` sinon.
- `release_channel()` &rarr; `None` \
  Libère le canal utilisé.
- `get_debug_string()` &rarr; `str` \
  Renvoie des données de débogage concernant cette instance, pour [`LogHandler`](log_handler.md).
- `remove()` &rarr; `None` \
  Se supprime.
- `distance_to(vector2)` &rarr; `None` \
  Renvoie la distance jusqu'à `vector2`, pour calculer le volume ajusté. \
  Paramètre :
  * `vector2` : *[`Vector2`](vector_2.md)*
- `get_loop()` &rarr; `bool` \
  Renvoie `True` si le son se joue en boucle et `False` sinon.

