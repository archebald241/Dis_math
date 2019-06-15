import pygame
import random
import theory
import practicece

#Обьявление класса вершин графа
class Circle():
    def __init__(self,x,y,v):
        self.x = x
        self.y = y
        self.v = v
        self.color = (120,120,120)
    def draw(self,root):
        pygame.draw.circle(root,self.color,(self.x,self.y),20)
        root.blit(pygame.font.Font(None, 22).render('V'+str(self.v), True, (0, 0, 0)),(self.x-7,self.y-7))


#Функция отрисовки объектов в окне
def window():
    root.blit(pygame.image.load('sprites/main_background.png'),(0,0))
    root.blit(headline,(150,50))
    
    root.blit(theoryr,(500,200))
    if posM[0]>=500 and posM[0]<=585 and posM[1]>=200 and posM[1]<=220:
        pygame.draw.line(root,(255,255,255),(500,220),(587,220),2)
    root.blit(demo, (500, 250))
    if posM[0]>=500 and posM[0]<=675 and posM[1]>=250 and posM[1]<=270:
        pygame.draw.line(root,(255,255,255),(500,270),(677,270),2)
    root.blit(practice, (500, 300))
    if posM[0]>=500 and posM[0]<=615 and posM[1]>=300 and posM[1]<=320:
        pygame.draw.line(root,(255,255,255),(500,320),(612,320),2)
    pygame.display.update()


pygame.init()

#Создание главного окна
root = pygame.display.set_mode((800,600)) 
pygame.display.set_caption('Алгоритм нахождения остовного дерева неорентированного графа')
	
run = True

circles = []
line = []

headline = pygame.font.Font(None, 40).render('Алгоритм нахождения остовного дерева', True, (255, 253, 208))
theoryr = pygame.font.Font(None, 35).render('Теория', True, (255, 253, 208))
demo = pygame.font.Font(None, 35).render('Демонстрация', True, (255, 253, 208))
practice = pygame.font.Font(None, 35).render('Практика', True, (255, 253, 208))

pressed_mouse = False


#Создание вершин гарфа
circles.append(Circle(160,200,3))
circles.append(Circle(240,200,2))
circles.append(Circle(80,300,4))
circles.append(Circle(320,300,1))
circles.append(Circle(80,400,5))
circles.append(Circle(320,400,8))
circles.append(Circle(160,500,6))
circles.append(Circle(240,500,7))

#Основной цикл работы приложения
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    posM = pygame.mouse.get_pos()
    presM = pygame.mouse.get_pressed()
    if posM[0]>=500 and posM[0]<=585 and posM[1]>=200 and posM[1]<=220 and presM[0]==1:
        if theory.theorys():
            break
    if posM[0]>=500 and posM[0]<=615 and posM[1]>=300 and posM[1]<=320 and presM[0]==1:
    	if practicece.practices(circles):
    		break
    window()
pygame.quit()





