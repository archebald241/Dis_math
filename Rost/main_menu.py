import pygame

class Vertex():
	def __init__(self,X,Y,V):
		self.X = X
		self.Y = Y
		self.V = V
	def draw(self):
		pygame.draw.circle(win,(120,120,120),(self.X,self.Y),30)
		pygame.draw.circle(win,(0,0,0),(self.X,self.Y),30,2)
def window():
	pygame.draw.rect(win,(230,203,158),(0,0,800,600))
	for vert in vertex:
		vert.draw()

	pygame.display.update()

pygame.init()

win = pygame.display.set_mode((800,600))

run = True

vertex = []

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
	window()
