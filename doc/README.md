# Documentation
## Résumé du projet
Notre projet est un jeu s'inscrivant dans le contexte de la Seconde Guerre mondiale, avec pour but d'instruire à propos de l'utilisation de la cryptographie à cette époque et son fonctionnement. Il est programmé en Python 3, et utilise la bibliothèque [`PyGame`](https://pygame.org/), pour la gestion de l'affichage et du son. 

## Structure du projet
Malgré son absence au programme de première NSI, nous avons choisi de pratiquer la Programmation Orientée Objet (POO) afin de conserver une structure cohérente malgré la taille conséquente du code.

Notre jeu se découpe en trois catégories de classes, les unes interagissant avec les autres :
- les classes de base, constituant la majeure partie des fonctionnalités, mais rarement utilisées directement, par exemple la classe *Sprite* ;
- les classes spécifiques, héritant des classes de base et représentant des éléments concrets du jeu, par exemple la classe *NPC* (Personnage Non Joueur, PNJ) ;
- les classes utilitaires, fonctionnant en arrière-plan et contrôlant le comportement du jeu, par exemple *TimeHandler* (gestion du temps).

*Tous les chemins mentionnés ci-après prennent comme origine le dossier `sources` du dépôt Git.*

## Documentation des classes
- Classes de base (dossier `src/classes/basics`)
    * [`Animatable`](basics/animatable.md) - gestion de l'animation
    * [`BaseObject`](basics/base_object.md) - objet de base
    * [`Collider`](basics/collider.md) - gestion des collisions
    * [`Interactable`](basics/interactable.md) - gestion des interactions avec le joueur
    * [`MapElement`](basics/map_element.md) - éléments visuels de la `Map`
    * [`MapObject`](basics/map_object.md) - éléments "vivants" du jeu
    * [`Mission`](basics/mission.md) - **gestion** des missions
    * [`Missions`](basics/missions.md) - **stockage** des missions
    * [`Movable`](basics/movable.md) - gestion du déplacement
    * [`PillarObject`](basics/pillar_object.md) - pilier
    * [`RidgeObject`](basics/ridge_object.md) - arête de mur
    * [`SideEffectManager`](basics/side_effects_manager.md) - gestion des effets de bord
    * [`SoundMaker`](basics/sound_maker.md) - gestion du son
    * [`Sprite`](basics/sprite.md) - éléments visuels du jeu
    * [`UIElement`](basics/ui_element.md) - éléments de l'interface graphique
    * [`Vector2`](basics/vector_2.md) - représentation des vecteurs et points en 2D