# `PatternEvents` - Les évènements des PNJ

## Description

Cette classe est nécessaire pour fournir aux PNJ les pattern events dont ils ont besoin.

C'est un singleton dont les méthodes sont crées au besoin.

Ces méthodes retournent *`True`* si elles doivent être exécutées à la prochaine frame, et *`False`* sinon.

> ```python
> def npc_event_test(_, host, delta_time):
> 	if delta_time == 0 :
> 		first_time = True  # la fonction s'éxecute pour la première fois
> 	if delta_time <= 2: # en secondes
> 		return True  # la fonction sera réappelé à la prochaine frame
> 	else:
> 		return False  # la fonction ne sera pas réappelée
> ```
> Exemple d'une telle méthode : faire attendre le PNJ 2 secondes.

## Attributs
> aucun

## Méthodes
- `__init__()` &rarr; `None`
  > pass

- `do(pattern_event_name, host, delta_time)` &rarr; `bool`
  Appelle la méthode de l'event correspondant à `pattern_event_name`, et lui passe en paramètre `host` et `delta_time`, retourne ce que retourne la méthode.
  Paramètres :
  * `pattern_event_name` : *`str`*
  Le nom du pattern event.
  * `host` : *`NPC`*
  Le PNJ à l'origine de cet évènement.
  * `delta_time` : *`float`*
  La durée en secondes à partir de laquelle l'évènement a commencé.