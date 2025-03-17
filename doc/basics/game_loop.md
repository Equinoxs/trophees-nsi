# `GameLoop`
## Description
Cette classe est nécessaire à l'exécution du jeu en étant exécutée continuellement.

Elle coordonne les différents composants du jeu comme tous les `Handler`, `Camera`, `Player` etc.

Elle appelle une méthode `update()` de chacun de ces composants régulièrement pour leur permettre de se mettre à jour.

## Attributs
- `running` : *`bool`* 
  Indique si la boucle de jeu est en cours d'exécution.
- `paused` : *`bool`* 
  Indique si le jeu est en pause.
- `fullscreen` : *`bool`* 
  Indique si le jeu est en mode plein écran.
- `screen` : *`pygame.Surface`* 
  Surface d'affichage du jeu.
- `time_handler` : *`TimeHandler`* **get**
- `data_handler` : *`DataHandler`* **get**
- `saved_data` : *`dict`*
- `player` : *`Player`* **get**
- `camera` : *`Camera`* **get**
- `control_handler` : *`ControlHandler`* **get**
- `sound_mixer` : *`SoundMixer`* **get**
- `mission_handler` : *`MissionHandler`* **get**
- `menu_handler` : *`MenuHandler`* **get**
- `log_handler` : *`LogHandler`* **get**

## Méthodes
- `__init__(screen, control_handler, time_handler, data_handler, player, sound_mixer, camera, mission_handler, 
  menu_handler, log_handler)` &rarr; `None` \
  Initialise les attributs et lance la boucle infinie appellant `update()`. \
  Paramètres :
  * `screen` : `pygame.Surface`
  * `control_handler` : `ControlHandler`
  * `time_handler` : `TimeHandler`
  * `data_handler` : `DataHandler`
  * `player` : `Player`
  * `sound_mixer` : `SoundMixer`
  * `camera` : `Camera`
  * `mission_handler` : `MissionHandler`
  * `menu_handler` : `MenuHandler`
  * `log_handler` : `LogHandler`

- `is_game_paused()` &rarr; `bool` \
  Renvoie `True` si le jeu est en pause, sinon `False`.

- `quit_game()` &rarr; `None` \
  Arrête la boucle de jeu.

- `pause_game()` &rarr; `None` \
  Met le jeu en pause.

- `unpause_game()` &rarr; `None` \
  Retire la pause du jeu.

- `throw_event(event)` &rarr; `None` \
  Transmet un événement à la `Map`. \
  Paramètre :
  * `event` : `dict`

- `toggle_fullscreen()` &rarr; `None` \
  Bascule entre le mode plein écran et le mode fenêtré.

- `update()` &rarr; `None` \
  Met à jour tous les composants du jeu : `ControlHandler`, `TimeHandler`, `SoundMixer`, 
  `Player`, `MissionHandler`, `MenuHandler`, `Camera`, gère les évènements d'entrée de l'utilisateur.