import pygame
import random
pygame.init()

okno = pygame.display.set_mode((870,600))
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
	def __init__(self,x,y,color,v,znach):
		self.x = x
		self.y = y
		self.color = color
		self.v = v
		self.znach = znach
	def draw(self,okno):
		if self.v[0] != self.v[1]:
			pygame.draw.line(okno,self.color,(self.x[0],self.y[0]),(self.x[1],self.y[1]),5)
		else:
			pygame.draw.circle(okno,self.color,(self.x[0],self.y[0]+25),25,2)
def lines(circles):
	line = []
	prov = True
	prov1 = False
	delete_line = []
	ind = 0
	for i in range(len(circles)):
		for j in range(len(circles)):
			if random.randint(0,3)==1 and i!=j:
				line.append(Lines((circles[i].x,circles[j].x),(circles[i].y,circles[j].y),(0,0,0),
					[circles[i].v,circles[j].v],random.randint(1,10)))
	
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
	return line
def kolvo_ver():
	pass

def window():
	pygame.draw.rect(okno,(220,170,235),(0,0,1200,600))
	pygame.draw.line(okno,(0,0,0),(0,400),(600,400),2)
	pygame.draw.line(okno,(0,0,0),(200,400),(200,600),2)
	pygame.draw.line(okno,(0,0,0),(600,0),(600,600),2)
	pygame.draw.line(okno,(0,0,0),(600,270),(870,270),2)
	
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
	
	
	for i in range(8):
		pygame.draw.line(okno,(0,0,0),((i*30)+630,0),((i*30)+630,270),2)
		
	for i in range(8):
		pygame.draw.line(okno,(0,0,0),(600,(i*30)+30),(870,(i*30)+30),2)
		
	for i in range(8):
		okno.blit(pygame.font.Font(None, 30).render('V'+str(i+1), True, (0,0,0)),((i*30)+635,5))
		okno.blit(pygame.font.Font(None, 30).render('V'+str(i+1), True, (0,0,0)),(605,(i*30)+35))
	
	for i in range(8):
		for j in range(8):
			sush = False
			for lin in line:
				if lin.v[0]==i+1 and lin.v[1]==j+1:
					sush = True
					zn = lin.znach
					break
			if sush:
				okno.blit(pygame.font.Font(None, 30).render(str(zn), True, (200,100,100)),((i*30)+635,(j*30)+35))
			else:
				okno.blit(pygame.font.Font(None, 30).render('-', True, (100,100,200)),((i*30)+635,(j*30)+35))
	
	
	for lin in line:
		lin.draw(okno)
	for ver in versh:
		ver.draw(okno)
	
	
	
	if F_v_p:
		okno.blit(pygame.font.Font(None,25).render('Начальная вершина:'+str(F_v),True,(0,0,0)),(210,410))
		okno.blit(pygame.font.Font(None,25).render('Выбирете множество R(v): ',True,(0,0,0)),(210,430))
		for i in range(len(R_v)):
			okno.blit(pygame.font.Font(None,25).render('V'+str(R_v[i]),True,(0,0,0)),(435+25*i,430))
	else:
		okno.blit(pygame.font.Font(None,25).render('Начальная вершина:',True,(0,0,0)),(210,410))	
	if R_v_p:
		okno.blit(pygame.font.Font(None,25).render('Выбирете множество Q(v): ',True,(0,0,0)),(210,450))
		for i in range(len(Q_v)):
			okno.blit(pygame.font.Font(None,25).render('V'+str(Q_v[i]),True,(0,0,0)),(435+25*i,450))
	if Q_v_p:
		okno.blit(pygame.font.Font(None,25).render('Выбирете множество C(v): ',True,(0,0,0)),(210,470))
		for i in range(len(C_v)):
			okno.blit(pygame.font.Font(None,25).render('V'+str(C_v[i]),True,(0,0,0)),(435+25*i,470))
	if len(K_S)!=0:
		okno.blit(pygame.font.Font(None,25).render('Компоненты связности: ',True,(0,0,0)),(605,275))
		for i in range(len(K_S)):
			okno.blit(pygame.font.Font(None,25).render(str(i+1)+')',True,(0,0,0)),(615,300+i*20))
			for j in range(len(K_S[i])):
				okno.blit(pygame.font.Font(None,25).render('V'+str(K_S[i][j]),True,(0,0,0)),(630+j*25,300+i*20))
	pygame.display.update()

run = True
m_pres = False

versh = []
line = lines(versh)
versh.append(Vershini(480,150,(125,125,125),1))
versh.append(Vershini(360,50,(125,125,125),2))
versh.append(Vershini(240,50,(125,125,125),3))
versh.append(Vershini(120,150,(125,125,125),4))
versh.append(Vershini(120,250,(125,125,125),5))
versh.append(Vershini(240,350,(125,125,125),6))
versh.append(Vershini(360,350,(125,125,125),7))
versh.append(Vershini(480,250,(125,125,125),8))



F_v = 0
F_v_p = False
R_v = []
R_v_1 = []
R_v_p = False
Q_v = []
Q_v_1 = []
Q_v_p = False
C_v = []
C_v_1 = []
C_v_p = False
K_S = []


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
				line = []
				F_v = 0
				F_v_p = False
				R_v = []
				R_v_1 = []
				R_v_p = False
				Q_v = []
				Q_v_1 = []
				Q_v_p = False
				C_v = []
				C_v_1 = []
				C_v_p = False
				K_S = []
			if posM[0]>10 and posM[0]<190 and posM[1]>530 and posM[1]<580:
				break
				
				
			if not(F_v_p):
				for ver in versh:
					if ((posM[0]-ver.x)**2 + (posM[1]-ver.y)**2)<625:
						prov = False
						if len(K_S)!=0:
							for K_s in K_S:
								for k_s in K_s:
									if k_s==ver.v:
										prov = True
										break
						if not(prov):
							F_v = ver.v
							F_v_p = True
							R_v.append(ver.v)
							R_v_1.append(ver.v)
							Q_v.append(ver.v)
							Q_v_1.append(ver.v)
							C_v.append(ver.v)
							C_v_1.append(ver.v)
							break
			elif not(R_v_p):
				for lin in line:
					prov = False
					if F_v == lin.v[1]:
						for r_v in R_v_1:
							if lin.v[0] == r_v:
								prov = True
								break
						if not(prov):
							R_v_1.append(lin.v[0])
				for ver in versh:
					if ((posM[0]-ver.x)**2 + (posM[1]-ver.y)**2)<625:
						prov1 = False
						prov2 = False
						for r_v_1 in R_v_1:
							if r_v_1 == ver.v:
								prov1 = True
								break
						for r_v in R_v:
							if r_v == ver.v:
								prov2 = True
								break
						if prov1 and not(prov2):
							R_v.append(ver.v)
				if len(R_v)==len(R_v_1):
					R_v_p = True
			elif not(Q_v_p):
				for lin in line:
					prov = False
					if F_v == lin.v[0]:
						for q_v in Q_v_1:
							if lin.v[1] == q_v:
								prov = True
								break
						if not(prov):
							Q_v_1.append(lin.v[1])
				for ver in versh:
					if ((posM[0]-ver.x)**2 + (posM[1]-ver.y)**2)<625:
						prov1 = False
						prov2 = False
						for q_v_1 in Q_v_1:
							if q_v_1 == ver.v:
								prov1 = True
								break
						for q_v in Q_v:
							if q_v == ver.v:
								prov2 = True
								break
						if prov1 and not(prov2):
							Q_v.append(ver.v)
				if len(Q_v)==len(Q_v_1):
					Q_v_p = True
			elif not(C_v_p):
				for i in range(len(R_v)):
					for j in range(len(Q_v)):
						if R_v[i]==Q_v[j]:
							prov = False
							for c_v_1 in C_v_1:
								if R_v[i]==c_v_1:
									prov = True
									break
							if not(prov):
								C_v_1.append(R_v[i])
				for ver in versh:
					if ((posM[0]-ver.x)**2 + (posM[1]-ver.y)**2)<625:
						prov1 = False
						prov2 = False
						for c_v_1 in C_v_1:
							if c_v_1 == ver.v:
								prov1 = True
								break
						for c_v in C_v:
							if c_v == ver.v:
								prov2 = True
								break
						if prov1 and not(prov2):
							C_v.append(ver.v)
				if len(C_v)==len(C_v_1):
					C_v_p = True
					K_S.append(C_v)
					F_v = 0
					F_v_p = False
					R_v = []
					R_v_1 = []
					R_v_p = False
					Q_v = []
					Q_v_1 = []
					Q_v_p = False
					C_v = []
					C_v_1 = []
					C_v_p = False
				
		m_pres = True
	else:
		m_pres = False
	if len(line) == 0:
		line = lines(versh)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	window()
pygame.quit()
