import pygame
import random

class Matr():
	def __init__(self,text,col,row):
		self.text = text
		self.col = col
		self.row = row
	def blit(self):
		win.blit(pygame.font.Font(None, 33).render(self.text, True, (0, 0, 0)),((self.col+1)*50+10,(self.row+2)*50+10))

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

	if input_matr:
		if sumbol<3:
			pygame.draw.line(win,(0,0,0),(x[0]+sumbol*14,y[0]),(x[1]+sumbol*14,y[1]),2)
		win.blit(pygame.font.Font(None, 40).render('Ввести матрицу', True, (0, 0, 0)),(630,70))
	else:
		strk = 100
		win.blit(pygame.font.Font(None, 40).render('Минимальные ребра: ', True, (0, 0, 0)),(610,70))
		for i in range(len(min_matr)):
			win.blit(pygame.font.Font(None, 37).render(
				str(i+1)+'. V'+str(min_matr[i].row)+'- V'+str(min_matr[i].col)+' ('+min_matr[i].text+')',
				True, (0, 0, 0)),(620,strk)
				)
			strk += 25

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

	win.blit(pygame.font.Font(None, 33).render(text, True, (0, 0, 0)),(x[0],y[0]))



	for mat in matr:
		if mat.col!=col or mat.row!=row:
			mat.blit()

	pygame.display.update()

pygame.init()

win = pygame.display.set_mode((900,650))

run = True

coldown = 0

col = 1
row = 1
sumbol = 0

key_pressed = False

text = ''

matr = []
input_matr = True

result = False

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


	x = [(col+1)*50+10,(col+1)*50+10]
	y = [(row+2)*50+10,(row+2)*50+40]

	posM = pygame.mouse.get_pos()
	keyM = pygame.mouse.get_pressed()

	if keyM[0] and posM[0]>630 and posM[0]<850 and posM[1]>70 and posM[1]<90:
		input_matr = False


	if input_matr:
		if keys[pygame.K_UP]:
			if not(key_pressed):
				if row > 1:
					matr.append(Matr(text,col,row))
					sumbol = 0
					row -= 1
					text = ''
					key_pressed = True
		elif keys[pygame.K_DOWN]:
			if not(key_pressed):
				if row < 8:
					matr.append(Matr(text,col,row))
					sumbol = 0
					row += 1
					text = ''
					key_pressed = True
		elif keys[pygame.K_LEFT]:
			if not(key_pressed):
				if col > 1:
					matr.append(Matr(text,col,row))
					sumbol = 0
					col -= 1
					text = ''
					key_pressed = True
		elif keys[pygame.K_RIGHT]:
			if not(key_pressed):
				if col < 8:
					matr.append(Matr(text,col,row))
					sumbol = 0
					col += 1
					text = ''
					key_pressed = True
		elif keys[pygame.K_BACKSPACE]:
			if not(key_pressed) and sumbol >0:
				text = text[0:sumbol-1]
				sumbol -= 1
				key_pressed = True
		elif keys[pygame.K_b]:
			if not(key_pressed) and sumbol<1:
				text = '&'
				sumbol += 1
				key_pressed = True
		elif keys[pygame.K_0]:
			if not(key_pressed) and sumbol <3:
				sumbol += 1
				text += '0'
				key_pressed = True
		elif keys[pygame.K_1]:
			if not(key_pressed) and sumbol <3:
				sumbol += 1
				text += '1'
				key_pressed = True
		elif keys[pygame.K_2]:
			if not(key_pressed) and sumbol <3:
				sumbol += 1
				text += '2'
				key_pressed = True
		elif keys[pygame.K_3]:
			if not(key_pressed) and sumbol <3:
				sumbol += 1
				text += '3'
				key_pressed = True
		elif keys[pygame.K_4]:
			if not(key_pressed) and sumbol <3:
				sumbol += 1
				text += '4'
				key_pressed = True
		elif keys[pygame.K_5]:
			if not(key_pressed) and sumbol <3:
				sumbol += 1
				text += '5'
				key_pressed = True
		elif keys[pygame.K_6]:
			if not(key_pressed) and sumbol <3:
				sumbol += 1
				text += '6'
				key_pressed = True
		elif keys[pygame.K_7]:
			if not(key_pressed) and sumbol <3:
				sumbol += 1
				text += '7'
				key_pressed = True
		elif keys[pygame.K_8]:
			if not(key_pressed) and sumbol <3:
				sumbol += 1
				text += '8'
				key_pressed = True
		elif keys[pygame.K_9]:
			if not(key_pressed) and sumbol <3:
				sumbol += 1
				text += '9'
				key_pressed = True
		else:
			for i in range(len(matr)):
				if matr[i].col==col and matr[i].row==row:
					text = matr[i].text
					sumbol = len(matr[i].text)
					matr.pop(i)
					break
			key_pressed = False
	elif not(result):
		min = 999
		min_matr = []
		for mat in matr:
			if mat.text != '&' and mat.text !='':
				if min>int(mat.text):
					min = int(mat.text)
		for mat in matr:
			if mat.text != '&' and mat.text!='':
				if min==int(mat.text):
					min_matr.append(Matr(mat.text,mat.col,mat.row))
		result = True
	window()
