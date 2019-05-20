import pygame
import random

def window():
	pygame.draw.rect(win,(230,203,158),(0,0,900,650))
	pygame.draw.line(win,(0,0,0),(0,50),(900,50),2)
	pygame.draw.line(win,(0,0,0),(550,50),(550,650),2)

	pygame.draw.line(win,(0,0,0),(50,100),(50,550),2)
	pygame.draw.line(win,(0,0,0),(100,100),(100,550),2)
	pygame.draw.line(win,(0,0,0),(150,100),(150,550),2)
	pygame.draw.line(win,(0,0,0),(200,100),(200,550),2)
	pygame.draw.line(win,(0,0,0),(250,100),(250,550),2)
	pygame.draw.line(win,(0,0,0),(300,100),(300,550),2)
	pygame.draw.line(win,(0,0,0),(350,100),(350,550),2)
	pygame.draw.line(win,(0,0,0),(400,100),(400,550),2)
	pygame.draw.line(win,(0,0,0),(450,100),(450,550),2)
	pygame.draw.line(win,(0,0,0),(500,100),(500,550),2)

	pygame.draw.line(win,(0,0,0),(50,100),(500,100),2)
	pygame.draw.line(win,(0,0,0),(50,150),(500,150),2)
	pygame.draw.line(win,(0,0,0),(50,200),(500,200),2)
	pygame.draw.line(win,(0,0,0),(50,250),(500,250),2)
	pygame.draw.line(win,(0,0,0),(50,300),(500,300),2)
	pygame.draw.line(win,(0,0,0),(50,350),(500,350),2)
	pygame.draw.line(win,(0,0,0),(50,400),(500,400),2)
	pygame.draw.line(win,(0,0,0),(50,450),(500,450),2)
	pygame.draw.line(win,(0,0,0),(50,500),(500,500),2)
	pygame.draw.line(win,(0,0,0),(50,550),(500,550),2)

	win.blit(pygame.font.Font(None, 35).render('V1', True, (0, 0, 0)),(115,115))
	win.blit(pygame.font.Font(None, 35).render('V2', True, (0, 0, 0)),(165,115))
	win.blit(pygame.font.Font(None, 35).render('V3', True, (0, 0, 0)),(215,115))
	win.blit(pygame.font.Font(None, 35).render('V4', True, (0, 0, 0)),(265,115))
	win.blit(pygame.font.Font(None, 35).render('V5', True, (0, 0, 0)),(315,115))
	win.blit(pygame.font.Font(None, 35).render('V6', True, (0, 0, 0)),(365,115))
	win.blit(pygame.font.Font(None, 35).render('V7', True, (0, 0, 0)),(415,115))
	win.blit(pygame.font.Font(None, 35).render('V8', True, (0, 0, 0)),(465,115))

	win.blit(pygame.font.Font(None, 35).render('V1', True, (0, 0, 0)),(65,165))
	win.blit(pygame.font.Font(None, 35).render('V2', True, (0, 0, 0)),(65,215))
	win.blit(pygame.font.Font(None, 35).render('V3', True, (0, 0, 0)),(65,265))
	win.blit(pygame.font.Font(None, 35).render('V4', True, (0, 0, 0)),(65,315))
	win.blit(pygame.font.Font(None, 35).render('V5', True, (0, 0, 0)),(65,365))
	win.blit(pygame.font.Font(None, 35).render('V6', True, (0, 0, 0)),(65,415))
	win.blit(pygame.font.Font(None, 35).render('V7', True, (0, 0, 0)),(65,465))
	win.blit(pygame.font.Font(None, 35).render('V8', True, (0, 0, 0)),(65,515))

	if Draw_line:
		pygame.draw.line(win,(0,0,0),(x[0],y[0]),(x[1],y[1]),2)

	pygame.display.update()

pygame.init()

win = pygame.display.set_mode((900,650))

run = True

coldown = 0

col = 1
row = 1
sumbol = 0

key_pressed = False

while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	Draw_line = False
	if coldown < 20:
		Draw_line = True
	if coldown > 40:
		coldown = 0
	coldown+=1


	keys = pygame.key.get_pressed()


	x = [(col+1)*50+10+sumbol*10,(col+1)*50+10+sumbol*10]
	y = [(row+2)*50+10,(row+2)*50+40]

	if keys[pygame.K_0]:
		if not(key_pressed) and sumbol <3:
			sumbol += 1
			key_pressed = True
	elif keys[pygame.K_1]:
		if not(key_pressed) and sumbol <3:
			sumbol += 1
			key_pressed = True
	elif keys[pygame.K_2]:
		if not(key_pressed) and sumbol <3:
			sumbol += 1
			key_pressed = True
	elif keys[pygame.K_3]:
		if not(key_pressed) and sumbol <3:
			sumbol += 1
			key_pressed = True
	elif keys[pygame.K_4]:
		if not(key_pressed) and sumbol <3:
			sumbol += 1
			key_pressed = True
	elif keys[pygame.K_5]:
		if not(key_pressed) and sumbol <3:
			sumbol += 1
			key_pressed = True
	elif keys[pygame.K_6]:
		if not(key_pressed) and sumbol <3:
			sumbol += 1
			key_pressed = True
	elif keys[pygame.K_7]:
		if not(key_pressed) and sumbol <3:
			sumbol += 1
			key_pressed = True
	elif keys[pygame.K_8]:
		if not(key_pressed) and sumbol <3:
			sumbol += 1
			key_pressed = True
	elif keys[pygame.K_9]:
		if not(key_pressed) and sumbol <3:
			sumbol += 1
			key_pressed = True
	elif keys[pygame.K_UP]:
		if not(key_pressed):
			if row > 1:
				row -= 1
				sumbol = 0
			key_pressed = True
	elif keys[pygame.K_DOWN]:
		if not(key_pressed):
			if row < 8:
				row += 1
				sumbol = 0
			key_pressed = True
	elif keys[pygame.K_LEFT]:
		if not(key_pressed):
			if col > 1:
				col -= 1
				sumbol = 0
			key_pressed = True
	elif keys[pygame.K_RIGHT]:
		if not(key_pressed):
			if col < 8:
				col += 1
				sumbol = 0
			key_pressed = True
	else:
		key_pressed = False

	window()
