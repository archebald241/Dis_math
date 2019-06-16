import pygame


class Matr():
	def __init__(self,text,col,row):
		self.text = text		#Текст вводимый пользователем
		self.col = col			#Столбцы V1-V8
		self.row = row			#Строки V1-V8
	def blit(self):
		win.blit(pygame.font.Font(None, 33).render(self.text, True, (0, 0, 0)),((self.col+1)*50+10,(self.row+2)*50+10)) #Отрисовка текста в ячейках
def sort_m(matr):
	return matr.row
def window():
	pygame.draw.rect(win,(230,203,158),(0,0,900,650)) #Фон
	pygame.draw.line(win,(0,0,0),(0,50),(900,50),2)
	pygame.draw.line(win,(0,0,0),(550,50),(550,650),2)

	win.blit(pygame.font.Font(None,40).render('Нахождение минимального ребра в нагруженном графе',True,(0,0,0)),(70,10))

	win.blit(pygame.font.Font(None,30).render('1,2,..,9 на клавиатуре - ввод значений от 1 до 9',True,(0,0,0)),(50,570))
	win.blit(pygame.font.Font(None,30).render('В - бесконечность',True,(0,0,0)),(50,595))

	#Линии столбцов
	for i in range(num_of_vert+2):
		pygame.draw.line(win,(0,0,0),((i*50)+50,100),((i*50)+50,50+((num_of_vert+2)*50)),2)

	#Линии строк
	for i in range(num_of_vert+2):
		pygame.draw.line(win,(0,0,0),(50,(i*50)+100),(50+((num_of_vert+1)*50),(i*50)+100),2)

	if input_matr:
		if sumbol<3:
			pygame.draw.line(win,(0,0,0),(x[0]+sumbol*14,y[0]),(x[1]+sumbol*14,y[1]),2)
		win.blit(pygame.font.Font(None, 40).render('Ввести матрицу', True, (0, 0, 0)),(630,70))
	else:
		strk = 100
		win.blit(pygame.font.Font(None, 40).render('Минимальные ребра: ', True, (0, 0, 0)),(610,70))
		for i in range(len(min_matr)):	#Перебор матрицы минимальных путей
			win.blit(pygame.font.Font(None, 37).render(
				str(i+1)+'. V'+str(min_matr[i].row)+'- V'+str(min_matr[i].col)+' ('+min_matr[i].text+')',
				True, (0, 0, 0)),(620,strk)
				)	#Отрисовка минимальный путей
			strk += 25	#Переход к следующей строке

	
	for i in range(num_of_vert):
		win.blit(pygame.font.Font(None, 35).render('V'+str(i+1), True, (0,0,0)),((i*50)+115,115))#Отрисовка тескта вершин
		win.blit(pygame.font.Font(None, 35).render('V'+str(i+1), True, (0,0,0)),(65,(i*50)+165))
	

	win.blit(pygame.font.Font(None, 33).render(text, True, (0, 0, 0)),(x[0],y[0]))	#Отрисовка вводимого текста

	for mat in matr: #Перебор матрицы путей
		if mat.col!=col or mat.row!=row:
			mat.blit()

	if posM[0]>630 and posM[0]<850 and posM[1]>70 and posM[1]<90:
		pygame.draw.line(win,(0,0,0),(630,95),(840,95),2)	#Подчеркивания текста "Ввести матрицу"

	pygame.display.update()

pygame.init()

num_of_vert = int(input('Введите количество вершин: '))

win = pygame.display.set_mode((900,650))

run = True


col = 1
row = 1
sumbol = 0

key_pressed = False #Отвечает за то, чтобы не повторялось действие при зажатии клавиши

text = ''

matr = []
input_matr = True	#Отвечает за ввод матрицы

result = False

while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	keys = pygame.key.get_pressed() #Отвечает за нажатую клавишу

	x = [(col+1)*50+10,(col+1)*50+10]	#Отвечает за положение "палочки"
	y = [(row+2)*50+10,(row+2)*50+40]	#Отвечает за положение "палочки"

	posM = pygame.mouse.get_pos()	#Позиция мыши
	keyM = pygame.mouse.get_pressed()	#Нажатие клавиши на мыши

	if keyM[0] and posM[0]>630 and posM[0]<850 and posM[1]>70 and posM[1]<90: #Отвечет за кнопку ввода матрицы
		input_matr = False

	if input_matr:
		if keys[pygame.K_UP]:
			if not(key_pressed):
				if row > 1: #Количество строк больше 1
					matr.append(Matr(text,col,row))	#Добавление в список класса значений
					sumbol = 0 #Количество символов = 0
					row -= 1	#От строки отнимается 1
					text = ''	#Переменная текст становится пустой
					key_pressed = True #Кнопка нажата становится правдой
		elif keys[pygame.K_DOWN]:
			if not(key_pressed):
				if row < num_of_vert: #Количество строк меньше 8
					matr.append(Matr(text,col,row))
					sumbol = 0
					row += 1
					text = ''
					key_pressed = True
		elif keys[pygame.K_LEFT]:
			if not(key_pressed):
				if col > 1: #Количество столбцов больше 1
					matr.append(Matr(text,col,row))
					sumbol = 0
					col -= 1
					text = ''
					key_pressed = True
		elif keys[pygame.K_RIGHT]:
			if not(key_pressed):
				if col < num_of_vert:	#Количество столбцов меньше 8
					matr.append(Matr(text,col,row))
					sumbol = 0
					col += 1
					text = ''
					key_pressed = True
		elif keys[pygame.K_BACKSPACE]:
			if not(key_pressed) and sumbol>0: #Если кнопка не нажата и количество символов болье 0
				text = text[0:sumbol-1] #Извеление среза от одного значения до другого
				sumbol -= 1	#Кол-во символов уменьшается
				key_pressed = True
		elif keys[pygame.K_b]:
			if not(key_pressed) and sumbol<1:
				text = '&'
				sumbol = 3
				key_pressed = True
		elif keys[pygame.K_0]:
			if not(key_pressed) and sumbol <3 and sumbol>0:
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
			for i in range(len(matr)): #Перебор элементов списка матрицы
				if matr[i].col==col and matr[i].row==row:	#Если матрица столбца равна столбцу и матрица строки равна строке
					text = matr[i].text #Присваивание текста матрицы в текст
					sumbol = len(matr[i].text) #Присваивание количества символов
					matr.pop(i)	#Удаление итого элеметна матрицы
					break
			key_pressed = False
	elif not(result):
		min = 999
		matr.sort(key=sort_m)
		min_matr = []	#Матрица минимальных путей графа
		for mat in matr:	#Перебор элементов матрицы
			if mat.text != '&' and mat.text !='': #Если текст матрицы не пустой и не равен бесконечности
				if min>int(mat.text):		#Поиск
					min = int(mat.text)		 # минимального пути в графе
		for mat in matr:
			if mat.text != '&' and mat.text!='':
				if min==int(mat.text):
					min_matr.append(Matr(mat.text,mat.col,mat.row))	#Добавление элементов минимального пути
		result = True
	window()	#Обращение к фунции отрисовки
