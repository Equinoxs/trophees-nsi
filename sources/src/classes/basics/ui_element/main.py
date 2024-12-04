import pygame
class Menu:
    def __init__(self):
        self.active_buttons = []  # Boutons actuellement affichés

    def set_buttons(self, buttons):
        """Définit quels boutons doivent être affichés."""
        self.active_buttons = buttons

    def draw(self, screen):
        for button in self.active_buttons:
            button.draw(screen)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Clic gauche
            for button in self.active_buttons:
                if button.is_clicked(event.pos):
                    button.click()
pygame.init()
paused = False

def pause_game():
    global paused
    paused = True
    menu.set_buttons([unpause_button, quit_button])  # Affiche le menu de pause

def unpause_game():
    global paused
    paused = False
    menu.set_buttons([pause_button])  # Affiche le bouton pause "I I" uniquement

def quit_game():
    pygame.quit()
    exit()

# Création des boutons
pause_button = Button(1205, 15, 60, 50, "I I", pause_game, (145, 77, 17), font_size=60)
unpause_button = Button(540, 300, 200, 50, "Unpause", unpause_game)
quit_button = Button(540, 400, 200, 50, "Quit", quit_game)

# Création du menu
menu = Menu()
menu.set_buttons([pause_button])  # Commence avec le bouton "I I"

# Boucle principale
running = True
while running:
    screen.fill((30, 30, 30))  # Couleur de fond
    menu.draw(screen)  # Dessine les boutons visibles
    pygame.display.flip()  # Rafraîchit l'écran

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        menu.handle_event(event)
