# `TimeHandler` - gestion du temps
## Description
Cette classe gère le temps du jeu, à travers les `ChronoTag`, balises temporelles 
permettant de connaître le temps écoulé entre deux actions simplement.

## Attributs
- `clock` : *`pygame.Clock`* **set**
- `dt` : *`float`* \
  Temps écoulé depuis le dernier rafraîchissement en secondes
- `coeff` : *`float`* **set** \
  Coefficient de ralentissement du jeu.
- `running` : *`bool`* \
  Indique si le jeu n'est pas en pause.
- `chrono_tags` : *`dict`*

## Méthodes
- `add_chrono_tag(chrono_tag, reset=False)` &rarr; `float` \
  S'il n'existe pas ou si `reset` vaut `True`, crée un nouveau `ChronoTag`, et renvoie 0, et sinon renvoie 
  le temps écoulé depuis la création du `ChronoTag` nommé `chrono_tag`. \
  Paramètres :
  * `chrono_tag` : *`str`*
  * `reset` : *`bool`*
- `remove_chrono_tag(chrono_tag)` &rarr; `None` \
  Supprime le `ChronoTag` nommé `chrono_tag`. \
  Paramètre :
  * `chrono_tag` : *`str`*
- `update()` &rarr; `None` \
  Met à jour `dt` et les `ChronoTag`s.
- `stop()` &rarr; `None`\
  Arrête le temps (jeu en pause).
- `resume()` &rarr; `None` \
  Redémarre le temps (jeu plus en pause).
- `is_running()` &rarr; `None` \
  Renvoie la valeur de `running`.