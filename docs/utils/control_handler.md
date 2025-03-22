# `ControlHandler` - gestion des contrôles
## Description
Cette classe est nécessaire pour interagir avec le jeu à travers des contrôles.

Ce singleton permet d'interpréter les actions du clavier et de la souris du joueur dans le jeu et d'effectuer les actions appropriées.

Elle récupère la liste des évènements à chaque rafraîchissement de l'écran et permet aux autres classes de récupérer leur état.

C'est un singleton par lequel passe la plupart des contrôles utilisateurs.

## Attributs
- `events` : *`dict`*
  Les différentes actions du jeu.
- `mouse_position` : *`tuple(int)`*
  La position de la souris.
- `pygame_events` : *`list`* **get**
  Une sauvegarde des évènements pygame depuis la dernière frame pour y ravoir accès.
- `consumed_events` : *`set`*
  Permet d'empêcher la réactivation d'une touche jusqu'à ce que celle ci soit relachée.
- `disabled_actions` : *`list`*
  Les actions qui ne s'activent pas, qui sont bloquées, c'est pratique pour certaines missions où on ne veut pas que le joueur ne bouge par exemple.
- `settings_initialized` : *`bool`*
  Indique si le menu des settings a été initialisé.
- `keybinds` : *`dict`* **get** \
  Les différents évènements associés à leur touche respective comme définis dans la sauvegarde du jeu.

## Méthodes
- `__init__(saved_data)` &rarr; `None` \
  Initialise les attributs et les `keybinds` en fonction de `saved_data`. \
  Paramètre :
  * `saved_data` : *`dict`*

- `load_keybinds(keybinds_data)` &rarr; `None` \
  Récupère les associations de touches et les stocke dans `keybinds`. \
  Paramètre :
  * `keybinds_data` : *`dict`*

- `get_pygame_key_name(key)` &rarr; `str` \
  Renvoie le nom d'une touche en fonction de son code. \
  Paramètres :
  * `key` : *`int`*

- `disable_actions(actions)` &rarr; `None` \
  Paramètres :
  * `actions` : *`list[str]`*

- `disable_all_actions()` &rarr; `None`
- `enable_all_actions()` &rarr; `None`

- `handle_events()` &rarr; `None` \
  Méthode exécutée à chaque rafraîchissement du jeu qui récupère les touches appuyées et le mouvement de la souris pour 
  mettre à jour `events`.

- `is_activated(event_name)` &rarr; `bool` \
  Renvoie l'état de l'évènement `event_name`. \
  Paramètre :
  * `event_name` : *`str`*

- `is_clicked(button)` &rarr; `bool` \
  Renvoie `True` si le bouton est cliqué et `False` sinon.
  Paramètre :
  * `button` : *`Button`*

- `activate_event(event_name)` &rarr; `None` \
  Paramètre :
  * `event_name` : *`str`*

- `finish_event(event_name)` &rarr; `None` \
  Paramètre :
  * `event_name` : *`str`*

- `reset_keybinds()` &rarr; `None` \
  Remet à zéro les associations de touches depuis le fichier de sauvegarde original.

- `consume_event(event_name)` &rarr; `None` \
  Termine l'évènement et l'ajoute à la liste des évènements consommés. \
  Paramètres :
  * `event_name` : *`str`*

- `get_key_letter(event_name)` &rarr; `None` \
  Retourne le nom de la touche associée à un événement. \
  Paramètre :
  * `event_name` : *`str`*

- `set_keybind(event_name, key)` &rarr; `None` \
  Associe une touche à un évènement.
  Paramètres :
  * `event_name` : *`str`*
  * `key` : *`str`*

- `initialize_settings_inputs()` &rarr; `None` \
  Initialise les cases de texte associées aux touches des paramètres du jeu.
