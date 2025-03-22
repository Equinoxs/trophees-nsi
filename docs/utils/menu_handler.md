# `MenuHandler` - gestion des [`Menu`](../ui/menu.md)
Cette classe gère le chargement, la création, la destruction et l'affichage et des [`Menu`](../ui/menu.md).

Elle charge les données des menus depuis un fichier JSON. Un système de classes similaire à celui de CSS,
permettant d'attribuer des propriétés par défaut à un [`UIElement`](../ui/ui_element.md) par la simple inclusion de celle-ci.

>```json
>"close_button": {
>	"class": "interactive_button",
>	"label": "Close",
>	"color": [61, 53, 39],
>	"font_size": 50,
>	"x": 50,
>	"y": 40,
>	"width": 140,
>	"height": "auto",
>	"action": "focus_on_game"
>}
>```
>*Exemple de JSON décrivant un élément de menu*

>```json
>"interactive_button": {
>	"border_radius": 4,
>	"border_length": 2,
>	"border_color": [46, 34, 9],
>	"color": [125, 113, 89],
>	"text_color": [204, 174, 114]
>},
>```
>*Exemple de JSON décrivant une classe*

Dans l'exemple ci-dessus, l'[`UIElement`](../ui/ui_element.md) `close_button` se verra attribuer les propriétés 
`border_radius`, `border_length` etc.

## Attributs
- [`menus`](../ui/menu.md) : *`dict`*
- `menus_historics` : *`array`* \
  Historique des menus.
- `classes` : *`dict`* \
  Classes *type-CSS*.
- [`markers`](../ui/marker.md) : *`list`*
- [`dialogs`](../ui/dialog.md) : *`dict`*
- `current_menu` : *`dict`* **get**
- `current_menu_name` : *`str`* **get**
- [`button_actions`](../ui/button_actions.md) : *[`ButtonActions`](../ui/button_actions.md)* **get**
- `fps_toggled` : *`bool`* **get**

## Méthodes
- `get_menu(menu_name)` &rarr; [`Menu`](../ui/menu.md) \
  Renvoie le [`Menu`](../ui/menu.md) nommé `menu_name`. \
  Paramètre :
  * `menu_name` : *`str`*
- `get_class(class_name)` &rarr; *`dict`* \
  Renvoie la classe nommée `class_name`. \
  Paramètre :
  * `class_name` : *`str`*
- `load_menus()` &rarr; `None` \
  Charge les menus depuis le JSON récupéré par [`DataHandler`](data_handler.md) et les instancie.
- `add_marker(marker_data)` &rarr; [`Marker`](../ui/marker.md) \
  Ajoute un [`Marker`](../ui/marker.md) instancié avec `marker_data`. \
  Paramètre :
  * `marker_data` : *`dict`* \
    Données d'initialisation du [`Marker`](../ui/marker.md).
- `remove_marker(marker_ref)` &rarr; `None` \
  Supprime le [`Marker`](../ui/marker.md) instancié en tant que `marker_ref`. \
  Paramètre :
  * `marker_ref` : [`Marker`](../ui/marker.md)
- `add_dialog(dialog_name, dialog_data)` &rarr; `None` \
  Ajoute un [`Dialog`](../ui/dialog.md) instancié avec `dialog_data`. \
  Paramètres :
  * `dialog_name` : *`str`*
  * `dialog_data` : *`dict`* \
    Données d'initialisation du [`Dialog`](../ui/dialog.md).
- `remove_dialog(dialog_name)` &rarr; `None` \
  Supprime le [`Dialog`](../ui/dialog.md) nommé `dialog_name`. \
  Paramètre :
  * `dialog_name` : *`str`*
- `is_dialog(dialog_name)` &rarr; `bool` \
  Renvoie `True` si le [`Dialog`](../ui/dialog.md) nommé `dialog_name` existe. \
  Paramètre :
  * `dialog_name` : *`str`*
- `toggle_fps()` &rarr; `None` \
  Bascule l'état de l'affichage de [`FPSHelper`](../ui/fps_helper.md).
- `set_current_menu(menu_name, force_render=False, update=True)` &rarr; `None` \
  Remplace le [`Menu`](../ui/menu.md) en cours d'affichage par le [`Menu`](../ui/menu.md) nommé `menu_name`. \
  Paramètres :
  * `menu_name` : *`str`*
  * `force_render` : *`bool`* \
    Indique si le menu doit être rendu.
  * `update` : *`bool`* \
    Indique si le menu doit être mis à jour.
- `get_last_menu()` &rarr; [`Menu`](../ui/menu.md) \
  Renvoie le dernier [`Menu`](../ui/menu.md) affiché à l'écran avant celui en cours d'affichage.
- `set_last_menu()` &rarr; [`Menu`](../ui/menu.md) \
  Remplace le [`Menu`](../ui/menu.md) en cours d'affichage par le dernier [`Menu`](../ui/menu.md) affiché à l'écran avant celui en cours d'affichage.
- `update()` &rarr `None` \
  Met à jour le [`Menu`](../ui/menu.md) en cours d'affichage.
- `render()` &rarr; `None` \
  Affiche le menu en cours à l'écran.
