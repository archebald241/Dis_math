def theorys():
	import os
	import pygame
	pygame.init()
	root = pygame.display.set_mode((800,600))
	pygame.display.set_caption('Алгоритм нахождения остовного дерева неорентированного графа')
	
	run = True
	
	back = pygame.font.Font(None, 25).render('<- Назад', True, (255, 255, 255))
	headline = pygame.font.Font(None, 40).render('Алгоритм нахождения остовного дерева', True, (255, 255, 255))
	
	text = []
	string = 170
	for th_text in open('theory.txt','r'):
		th_text1 = th_text[:len(th_text)-2:1]
		th_text1 = pygame.font.Font(None,30).render(th_text1,True,(255,255,255))
		text.append(th_text1)
	
	while run:
		root.blit(pygame.image.load('sprites/theory_bg.png'),(0,0))
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				return True
		
		posM = pygame.mouse.get_pos()
		presM = pygame.mouse.get_pressed()
		if posM[0]>=10 and posM[0]<=83 and posM[1]>=110 and posM[1]<=130:
			pygame.draw.line(root,(255,255,255),(10,125),(83,125),2)
		if posM[0]>=10 and posM[0]<=83 and posM[1]>=110 and posM[1] <= 130 and presM[0]==1:
			return False
			break
		
		
		for txt in text:
			root.blit(txt,(70,string))
			string += 25
		string = 170	
		root.blit(back,(10,110))
		root.blit(headline,(150,50))
		
		pygame.display.update()
		

