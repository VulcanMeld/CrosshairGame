import os, sys
import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((400,300))

pygame.display.set_caption("Hello World!")

red = (255,0,0)
black = (0,0,0)



while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			if event.key == K_RETURN:
				pygame.draw.rect(screen,red,(20,30,40,40))
			elif event.key == K_ESCAPE:
				pygame.quit()
				sys.exit()
			elif event.key == K_SPACE:
				screen.fill(black)

	pygame.display.update()