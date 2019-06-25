import pygame


def n_o_v():
	win = pygame.display.set_mode((500,300))
	run = True
	text = 2
	mouse_pr = False
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				return 8
				break
		
		
		main_text = pygame.font.Font(None,30).render('Введите количество вершин от 2 до 8: ',True,(0,0,0)) #Верхний текст
		text_v = pygame.font.Font(None,60).render(str(text),True,(0,0,0))	#Текст количества вершин
		vvod = pygame.font.Font(None,40).render('Ввести',True,(0,0,0))	#Текст ввода
		
		
		pygame.draw.rect(win,(230,203,158),(0,0,500,300))	#Отрисовка фона
		pygame.draw.rect(win,(0,0,0),(200,100,34,49))	#Отрисовка окна вывода количества вершин
		pygame.draw.rect(win,(125,125,125),(202,102,30,45))
		pygame.draw.rect(win,(0,0,0),(240,95,19,24))	#Отрисовка кнопок
		pygame.draw.rect(win,(125,125,125),(242,97,15,20))
		pygame.draw.line(win,(0,0,0),(249,100),(247,112),2)
		pygame.draw.line(win,(0,0,0),(249,100),(251,112),2)
		pygame.draw.rect(win,(0,0,0),(240,130,19,24))
		pygame.draw.rect(win,(125,125,125),(242,132,15,20))
		pygame.draw.line(win,(0,0,0),(249,147),(247,135),2)
		pygame.draw.line(win,(0,0,0),(249,147),(251,135),2)
		
		posM = pygame.mouse.get_pos()
		presM = pygame.mouse.get_pressed()
		
		if presM[0]: 	#Взаимодействия с кнопками
			if posM[0]>240 and posM[0]<259 and posM[1]>95 and posM[1]<115 and text<8:
				if not(mouse_pr):
					text+=1 
			if posM[0]>240 and posM[0]<259 and posM[1]>130 and posM[1]<150 and text>2:
				if not(mouse_pr):
					text-=1  
			if posM[0]>190 and posM[0]<280 and posM[1]>200 and posM[1]<220:
				if not(mouse_pr):
					run = False
			mouse_pr = True
		else:
			mouse_pr = False
		
		win.blit(main_text,(50,50))	#Вывод текста на экран
		win.blit(text_v,(205,105))
		win.blit(vvod,(190,200))
		pygame.display.update()
	return text
	
	
