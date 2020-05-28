import generatorlist as gl #цитаты
import random
random.seed() #инициализируем библиотеку random
s=0 #создаём переменную s
def generator():
	while True: #вечный цикл
	    print(gl.text[random.randint(0, 19)] + "\n") #рандомизируем цитату
	    s=input('Введите "выход" для выхода из программы или нажмите Enter для продолжения \n')
	    if s=="Выход" or s=="выход" or s=="exit":
	        break #выходим, если написанно "выход"
def generate():
	return gl.text[random.randint(0, 29)] + "\n"
def gettext(ind):
	return gl.text[ind]
def getall():
		return gl.text
   

