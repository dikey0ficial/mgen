import generator as gen
import PySimpleGUI as sg

layout = [
	 [sg.Button('Генерировать')],
     [sg.Output(size=(88, 20))]
]

window = sg.Window('Генератор Мотивации', layout)
while True:
    event, values = window.read()
    #print(event, values) #debug
    if event in (None, 'Exit', 'Cancel'):
        break
    if event == 'Генерировать':
        print(gen.generate())