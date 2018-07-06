import sys, pygame
from pygame.locals import *

pygame.init()

FPS = 30

clock = pygame.time.Clock()

white = (255,255,255)

screen_width = 800

screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

screen.fill(white)

middle_of_screen = (screen_width / 2, screen_height / 2)

crosshair = pygame.image.load("crosshair089.png")

screen.blit(crosshair, middle_of_screen)

while True:

	mouse_pos = pygame.mouse.get_pos()

	screen.blit(crosshair, mouse_pos)

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.update()

	clock.tick(FPS)