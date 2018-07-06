import sys, pygame
from pygame.locals import *

pygame.init()


FPS = 30

clock = pygame.time.Clock()

white = (255,255,255)

black = (0,0,0)

screen_width = 800

screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

screen.fill(white)

middle_of_screen = (screen_width / 2, screen_height / 2)

crosshair = pygame.image.load("crosshair089.png")

screen.blit(crosshair, middle_of_screen)

gun_sound = pygame.mixer.Sound('gunshot.ogg')

font = pygame.font.Font("freesansbold.ttf", 100)

shots = 0



while True:

	font_surface = font.render("Shots fired: " + str(shots), False, black)

	screen.blit(font_surface, (400, 300))
	pygame.mouse.set_visible(False)

	screen.fill(white)

	mouse_pos = pygame.mouse.get_pos()

	screen.blit(crosshair, mouse_pos)

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

		elif event.type == MOUSEBUTTONDOWN:
			gun_sound.play()
			shots += 1


	pygame.display.update()

	clock.tick(FPS)

