import pygame
pygame.init()
screen = pygame.display.set_mode((400,400))
run = True
while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	pygame.draw.rect(screen,(125,125,125),(0,0,400,400))
	pygame.draw.circle(screen, (255, 255, 0), (100 + 30, 100 + 30), 25)
	pygame.draw.lines(screen, (0, 0, 0), False, [(100 + 30, 100 + 15), (100 + 30, 100 + 43)], 3)
	pygame.draw.lines(screen, (0, 0, 0), False, [(100 + 15, 100 + 30), (100 + 43, 100 + 30)], 3)
	pygame.draw.lines(screen, (0,0,200),False, [(20,20),(30,30),(40,30),(40,20)],5)
	pygame.display.update()
