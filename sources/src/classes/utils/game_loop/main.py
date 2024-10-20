import pygame

class GameLoop:
	def __init__(self, control_handler, time_handler):
		self.running = True
		time_handler.set_clock(pygame.time.Clock())

		pygame.init()
		self.screen = pygame.display.set_mode((1280, 720))

		while self.running:
			self.update(control_handler, time_handler)
			pygame.display.flip() # Rafraîchit l'écran

		pygame.quit()


	def update(self, control_handler, time_handler):
		control_handler.handleEvents(pygame)
  
		if control_handler.is_activated('quit'):
			self.running = False

		time_handler.update()
		# player.update() qui appellerait self.map.update() qui mettrait à jour tout le jeu
