import os
os.chdir(os.path.join('Моя папка','Dis_math'))
import pygame
import random
import theory_stapping_tree
import practicece_stapping_tree

#Обьявление класса вершин графа
class Circle():
    def __init__(self,x,y,v):
        self.x = x
        self.y = y
        self.v = 'V'+str(v)
    def draw(self,root):
        pygame.draw.circle(root,(120,120,120),(self.x,self.y),20)
        root.blit(pygame.font.Font(None, 22).render(self.v, True, (0, 0, 0)),(self.x-7,self.y-7))


#Функция отрисовки объектов в окне
def window():
    root.blit(pygame.image.load('sprites/main_background.png'),(0,0))
    root.blit(headline1_stapping_tree,(425,110))
    root.blit(headline2_stapping_tree,(550,135))
    root.blit(headline1_min_edge ,(15,110))
    root.blit(headline2_min_edge ,(40,135))
    
    root.blit(theoryr,(500,250))
    if posM[0]>=500 and posM[0]<=585 and posM[1]>=250 and posM[1]<=270:
        pygame.draw.line(root,(255,255,255),(500,270),(587,270),2)
    root.blit(demo, (500, 300))
    if posM[0]>=500 and posM[0]<=675 and posM[1]>=300 and posM[1]<=320:
        pygame.draw.line(root,(255,255,255),(500,320),(677,320),2)
    root.blit(practice, (500, 350))
    if posM[0]>=500 and posM[0]<=615 and posM[1]>=350 and posM[1]<=370:
        pygame.draw.line(root,(255,255,255),(500,370),(612,370),2)
    root.blit(task_min_edge, (60, 300))
    if posM[0]>=60 and posM[0]<=300 and posM[1]>=300 and posM[1]<=320:
        pygame.draw.line(root,(255,255,255),(60,320),(300,320),2)
    pygame.display.update()


pygame.init()

root = pygame.display.set_mode((800,600)) #Создание главного окна
pygame.display.set_caption('Алгоритм нахождения остовного дерева неорентированного графа')
	
run = True

circles = []
line = []

headline1_stapping_tree = pygame.font.Font(None, 37).render('Алгоритм нахождения', True, (255, 253, 208))
headline2_stapping_tree = pygame.font.Font(None,37).render('остовного дерева',True,(255, 253, 208))
theoryr = pygame.font.Font(None, 35).render('Теория', True, (255, 253, 208))
demo = pygame.font.Font(None, 35).render('Демонстрация', True, (255, 253, 208))
practice = pygame.font.Font(None, 35).render('Практика', True, (255, 253, 208))

headline1_min_edge = pygame.font.Font(None,37).render('Нахождение минимального ',True,(255, 253, 208))
headline2_min_edge = pygame.font.Font(None,37).render('ребра в нагруженном графе',True,(255, 253, 208))
task_min_edge = pygame.font.Font(None,35).render('Переход к заданию',True,(255, 253, 208))

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
        if theory_stapping_tree.theorys():
            break
    if posM[0]>=500 and posM[0]<=615 and posM[1]>=300 and posM[1]<=320 and presM[0]==1:
    	if practicece_stapping_tree.practices(circles):
    		break
    window()
pygame.quit()





