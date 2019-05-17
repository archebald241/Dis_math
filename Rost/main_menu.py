import pygame
import random

class Vertex():
	def __init__(self,X,Y,V):
		self.X = X
		self.Y = Y
		self.V = V
	def draw(self):
		pygame.draw.circle(win,(120,120,120),(self.X,self.Y),30)
		pygame.draw.circle(win,(0,0,0),(self.X,self.Y),30,2)
class Way():
	def __init__(self,x,y,color,v):
		self.x = x
		self.y = y
		self.color = color
		self.v = v
	def draw(self):
		pygame.draw.line(win,self.color,(self.x[0],self.y[0]),(self.x[1],self.y[1]),5)
def ways(vertex):
	way = []
	prov = True
	prov1 = False
	delete_way = []
	ind = 0
	for i in range(len(vertex)):
		for j in range(len(vertex)):
			if random.randint(0,5)==1 and i!=j:
				way.append(Way((vertex[i].X,vertex[j].X),(vertex[i].Y,vertex[j].Y),(10,10,10),[i+1,j+1]))
	for lin1 in range(len(way)-1):
		for lin2 in range(lin1,len(way)):
			if way[lin1].v[0]==way[lin2].v[1] and way[lin1].v[1]==way[lin2].v[0]:
				delete_way.append(lin2)
				prov1 = True
	if prov1:
		for delete in delete_way:
			del way[delete-ind]
			ind+=1
		ind = 0
		delete_way = []
		prov1 = False
	for cir in vertex:
		c = 0
		for lin in way:
			if not((cir.X == lin.x[0] and cir.Y == lin.y[0]) or (cir.X == lin.x[1] and cir.Y == lin.y[1])):
				c +=1
		if c == len(way):
			way = []
			break
	return way


def window():
	pygame.draw.rect(win,(230,203,158),(0,0,800,600))
	pygame.draw.line(win,(0,0,0),(0,100),(800,100),2)
	for wy in way:
		wy.draw()
	for vert in vertex:
		vert.draw()
	pygame.display.update()

pygame.init()

win = pygame.display.set_mode((800,600))

run = True

vertex = []
way = []

vertex.append(Vertex(160,200,3))
vertex.append(Vertex(240,200,2))
vertex.append(Vertex(80,300,4))
vertex.append(Vertex(320,300,1))
vertex.append(Vertex(80,400,5))
vertex.append(Vertex(320,400,8))
vertex.append(Vertex(160,500,6))
vertex.append(Vertex(240,500,7))

while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	if len(way)==0:
		way = ways(vertex)
	window()
