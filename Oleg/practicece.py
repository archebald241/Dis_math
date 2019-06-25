import pygame
import random

class Lines():
	def __init__(self,x,y,color,v):
		self.x = x
		self.y = y
		self.color = color
		self.v = v
	def draw(self,root):
		pygame.draw.line(root,self.color,(self.x[0],self.y[0]),(self.x[1],self.y[1]),5)
def sort_line(line):
	return line.v
def lines(circles):
	line = []
	prov = True
	prov1 = False
	delete_line = []
	ind = 0
	for i in range(len(circles)):
		for j in range(len(circles)):
			if random.randint(0,5)==1 and i!=j:
				line.append(Lines((circles[i].x,circles[j].x),(circles[i].y,circles[j].y),(200,200,200),[circles[i].v,circles[j].v]))
	for lin1 in range(len(line)-1):
		for lin2 in range(lin1,len(line)):
			if line[lin1].v[0]==line[lin2].v[1] and line[lin1].v[1]==line[lin2].v[0]:
				delete_line.append(lin2)
				prov1 = True
	if prov1:
		for delete in delete_line:
			del line[delete-ind]
			ind+=1
		ind = 0
		delete_line = []
		prov1 = False
	for cir in circles:
		c = 0
		for lin in line:
			if not((cir.x == lin.x[0] and cir.y == lin.y[0]) or (cir.x == lin.x[1] and cir.y == lin.y[1])):
				c +=1
		if c == len(line):
			line = []
			break
	if len(line)<7:
		line = []
	for lin in line:
		lin.v.sort()
	line.sort(key=sort_line)
	for lin in line:
		print(lin.v)
	print(' ')
	return line
	
def practices(circles):
	pygame.init()
	root = pygame.display.set_mode((800,600))
	pygame.display.set_caption('Алгоритм нахождения остовного дерева неорентированного графа')

	run = True

	line = []

	back = pygame.font.Font(None, 25).render('<- Назад |', True, (255,255,255))
	refresh = pygame.font.Font(None,25).render('Новый граф | Начать практику',True,(255,255,255))
	headline = pygame.font.Font(None, 40).render('Алгоритм нахождения остовного дерева', True, (255, 255, 255))
	graph = pygame.font.Font(None,30).render('Основной граф',True,(255,255,255))
	ost_tr_graph = pygame.font.Font(None,30).render('Остовное дерево',True,(255,255,255))
	
	v = 0
	use_v = []
	unuse_line = []
	start_practice = False
	pressed_mouse = False
	
	ostovn_tree = []
	
	vert_ost_tr = []
	
	all_vert = False

	while run:
		root.blit(pygame.image.load('sprites/main_background.png'),(0,0))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				return True
		posM = pygame.mouse.get_pos()
		presM = pygame.mouse.get_pressed()
		#create way in graph
		if len(line)==0:
			line = lines(circles)

		if posM[0]>=10 and posM[0]<=90 and posM[1]>=110 and posM[1] <= 130 and presM[0]==1:
			return False
			break
		if posM[0]>=100 and posM[0]<=210 and posM[1]>=110 and posM[1] <= 130 and presM[0]==1 and not(start_practice):
			line = []

		if posM[0]>=220 and posM[0]<=370 and posM[1]>=110 and posM[1] <= 130 and presM[0]==1 and not(start_practice):
			start_practice = True
			
		if start_practice:
			if presM[0]:
				if not(pressed_mouse):
					for lin in range(len(line)):
						sl1 = (posM[0]-line[lin].x[0])*(line[lin].y[1]-line[lin].y[0])
						sl2 = (line[lin].x[1]-line[lin].x[0])*(posM[1]-line[lin].y[0])
						yr = sl1 - sl2
						if (yr>-500 and yr<500 and 
							line[lin].color==(200,200,200) and posM[0]>60 and 
							posM[0]<340 and posM[1]>180 and posM[1]<520 and 
							len(ostovn_tree)<7):
							line[lin].color=(255,100,100)
							ostovn_tree.append(
								Lines([line[lin].x[0]+400,line[lin].x[1]+400],[line[lin].y[0],line[lin].y[1]],(255,100,100),line[lin].v))
							for vert in vert_ost_tr:
								if vert == line[lin].v[0]:
									all_vert = True
									break
							if not(all_vert):
								vert_ost_tr.append(line[lin].v[0])
							all_vert = False
							for vert in vert_ost_tr:
								if vert == line[lin].v[1]:
									all_vert = True
									break
							if not(all_vert):
								vert_ost_tr.append(line[lin].v[1])
							all_vert = False
							break
						 
				pressed_mouse = True
			else:
				pressed_mouse = False
			if len(ostovn_tree)==7 and len(vert_ost_tr)==8:
				end_text = pygame.font.Font(None,30).render('Остовное дерево найдено верно',True,(255,255,255))
			elif len(ostovn_tree)==7 and len(vert_ost_tr)!=8:
				end_text = pygame.font.Font(None,30).render('Остовное дерево найдено неверно',True,(255,255,255))
			
		for lin in line:
			lin.draw(root)
		for ost_tr in ostovn_tree:
			ost_tr.draw(root)
		for cir in circles:
			cir.draw(root)
		root.blit(back,(10,110))
		if not(start_practice):
			root.blit(refresh,(100,110))
		if len(ostovn_tree)==7:
			root.blit(end_text,(430,550))
		root.blit(graph,(120,140))
		root.blit(ost_tr_graph,(520,140))
		root.blit(headline,(150,50))

		pygame.display.update()
