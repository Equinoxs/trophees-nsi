# `Menu` - menu
## Description
Cette classe est nécessaire à l'affichage des menus, les regroupements d'[`UIElement`](ui_element.md).

Elle permet de regrouper des [`UIElement`](ui_element.md) au sein d'une surface unique rendue à l'écran.

Elle fournit des méthodes pour ajouter des [`UIElement`](ui_element.md), les retirer.

## Attribut
- `ui_elements` : *`list[`[`UIElement`](ui_element.md)`]`*

## Méthodes
- `__init__(menu_data)` &rarr; `None` \
  Initialise les attributs et charge les [`UIElement`](ui_element.md) de `menu_data`. \
  Paramètre :
  * `menu_data` : *`list[`[`UIElement`](ui_element.md)`]`*
- `get_elements(event)` &rarr; `list[`[`UIElement`](ui_element.md)`]` \
  Renvoie les [`UIElement`](ui_element.md) enregistrés dans le menu. 
  Si `event` est initialisé, renvoie seulement les [`TextInput`](text_input.md) dont l'attribut `event_name` correspond. \
  Paramètre : 
  * `event` : *`str`* 
- `get_element_by_id(id)` &rarr; [`UIElement`](ui_element.md) \
  Renvoie l'élément dont l'`id` correspond au paramètre `id`. \
  Paramètres :
  * `id` : *`str`*
- `add_element_ref(element_ref)` &rarr; `None` \
  Ajoute un élément par référence, c'est-à-dire un [`UIElement`](ui_element.md) déjà défini. \
  Paramètre :
  * `element_ref` : *[`UIElement`](ui_element.md)*
- `add_element(element_data)` &rarr; [`UIElement`](ui_element.md) \
  Ajoute un élément à partir de ses données, en instanciant une classe enfant de [`UIElement`](ui_element.md
  précisée dans le champ `type` de `element_data`. \
  Paramètre : 
  * `element_data` : *`dict`*
- `delete_element_by_id(id)` &rarr; `None` \
  Supprime l'élément dont l'`id` correspond au paramètre `id` de `ui_elements`. \
  Paramètres :
  * `id` : *`str`*
- `delete_element(element)` &rarr; `None` \
  Supprime un élément de `ui_elements`. \
  Paramètre :
  * `element` : *[`UIElement`](ui_element.md)*
- `load_ui_elements(ui_elements_data)` &rarr; `None` \
  Charge des [`UIElement`](ui_element.md) depuis `ui_elements_data`. \
  Paramètre :
  * `ui_elements_data` : *`list[`[`UIElement`](ui_element.md)`]`*
- `update()` &rarr; `None` \
  Met à jour chacun des [`UIElement`](ui_element.md) de `ui_elements` et affiche un curseur "doigt" si l'un d'eux est survolé.
- `render()` &rarr; `None` \
  Affiche chacun des [`UIElement`](ui_element.md)` de `ui_elements` à l'écran.