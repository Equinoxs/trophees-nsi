# `Dialog` - dialogue de texte
## Description
Cette classe est nécessaire à l'affichage des fenêtres de dialogue des [`NPC`](../world/specific/npc.md).

Elle permet d'afficher du texte de manière progressive dans une fenêtre en bas de l'écran.

Elle dérive de [`UIElement`](ui_element.md) et affiche le texte de manière autonome d'après une liste de messages.

## Attributs
- `_text_surface` : *`dict`* \
  Stockage interne des surfaces de texte.
- `messages` : *`list[str]`*
- `title` : *`str`*
- `message_id` : *`int`* \
  Identifiant du message en cours d'affichage.
- `text_margin` : *`int`* \
  Marge horizontale du texte.
- `arrow_image` : *`pygame.Image`*
- `wrapped_text_finish` : *`bool`*
- `text_display_duration` : *`float`*
- `chrono_tag_set` : *`bool`* \
  Indique si le `ChronoTag` de début de l'affichage a été initialisé.

## Méthodes
- `__init__(data)` &rarr; `None` \
  Initialise [`UIElement`](ui_element.md) et les attributs. \
  Paramètre :
  * `data` : *`dict`* \
    Données pour configurer l'élément.

- `wrap_text(use_chrono_tag)` &rarr; `str` \
  Scinde le texte en lignes et gère le retour automatique à la ligne. \
  Paramètre :
  * `use_chrono_tag` : *`bool`* \
    Indique s'il faut afficher le texte progressivement ou non.

- `render_text(surface_name='menu')` &rarr; `None` \
  Affiche le texte à l'écran et gère l'entrée utilisateur pour passer au dialogue suivant. \
  Paramètres :
  * `surface_name` : *`str`*

- `set_label(new_label)` &rarr; `None`
- `next_message()` &rarr; `None` \
  Passe au message suivant.
