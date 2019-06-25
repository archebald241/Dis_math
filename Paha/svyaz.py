import pygame
import random
pygame.init()

okno = pygame.display.set_mode((600,600))
class Vershini():
	def __init__(self,x,y,color,v):
		self.x = x
		self.y = y
		self.v = v
		self.color = color
	def draw(self,okno):
		pygame.draw.circle(okno,self.color,(self.x,self.y),25)
		okno.blit(pygame.font.Font(None, 22).render('V'+str(self.v), True, (0, 0, 0)),(self.x-7,self.y-7))
class Lines():
	def __init__(self,x,y,color,v):
		self.x = x
		self.y = y
		self.color = color
		self.v = v
	def draw(self,okno):
		if self.v[0] != self.v[1]:
			pygame.draw.line(okno,self.color,(self.x[0],self.y[0]),(self.x[1],self.y[1]),5)
		else:
			pygame.draw.circle(okno,self.color,(self.x[0],self.y[0]+25),25,2)
def kolvo_ver():
	pass

def window():
	pygame.draw.rect(okno,(220,170,235),(0,0,600,600))
	pygame.draw.line(okno,(0,0,0),(0,400),(600,400),2)
	pygame.draw.line(okno,(0,0,0),(200,400),(200,600),2)
	
	pygame.draw.rect(okno,(125,125,125),(10,410,180,50))
	pygame.draw.rect(okno,(0,0,0),(10,410,180,50),2)
	okno.blit(pygame.font.Font(None,25).render('Показать',True,(0,0,0)),(20,415))
	okno.blit(pygame.font.Font(None,25).render('компоненты',True,(0,0,0)),(40,428))
	okno.blit(pygame.font.Font(None,25).render('связности',True,(0,0,0)),(60,440))
	
	pygame.draw.rect(okno,(125,125,125),(10,470,180,50))
	pygame.draw.rect(okno,(0,0,0),(10,470,180,50),2)
	okno.blit(pygame.font.Font(None,25).render('Перестроить граф',True,(0,0,0)),(20,480))
	
	pygame.draw.rect(okno,(125,125,125),(10,530,180,50))
	pygame.draw.rect(okno,(0,0,0),(10,530,180,50),2)
	okno.blit(pygame.font.Font(None,25).render('Выход',True,(0,0,0)),(20,540))
	
	okno.blit(pygame.font.Font(None,25).render('Компоненты связности:',True,(0,0,0)),(210,410))
	
	
	for lin in lines:
		lin.draw(okno)
	for ver in versh:
		ver.draw(okno)
	
	pygame.display.update()

run = True
m_pres = False

versh = []
lines = []
versh.append(Vershini(480,150,(125,125,125),1))
versh.append(Vershini(360,50,(125,125,125),2))
versh.append(Vershini(240,50,(125,125,125),3))
versh.append(Vershini(120,150,(125,125,125),4))
versh.append(Vershini(120,250,(125,125,125),5))
versh.append(Vershini(240,350,(125,125,125),6))
versh.append(Vershini(360,350,(125,125,125),7))
versh.append(Vershini(480,250,(125,125,125),8))

komp_svyaz = [[1]]
while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
			
	keyM = pygame.mouse.get_pressed()
	posM = pygame.mouse.get_pos()
	if keyM[0]:
		if not(m_pres):
			if posM[0]>10 and posM[0]<190 and posM[1]>410 and posM[1]<460:
				pass
			if posM[0]>10 and posM[0]<190 and posM[1]>470 and posM[1]<520:
				lines = []
			if posM[0]>10 and posM[0]<190 and posM[1]>530 and posM[1]<580:
				break
		m_pres = True
	else:
		m_pres = False
	if len(lines) == 0:
		for i in range(len(versh)):
			for j in range(i,len(versh)):
				if random.randint(0,5)==1:
					lines.append(Lines((versh[i].x,versh[j].x),(versh[i].y,versh[j].y),(0,0,0),[versh[i].v,versh[j].v]))
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	window()
pygame.quit()
