#mgen

Library which generate motivation phrases. ONLY RUSSIAN LANGUAGE.  
Библиотека, которая генерирует мотивирующие цитаты. ТОЛЬКО РУССКИЙ ЯЗЫК


#REQUIREMENTS/ТРЕБОВАНИЯ
You must install PySimpleQui lib for GUI version (MyApp.py)
Вы должны установить библиотеку PySimpleGUI для версии с GUI(MyApp.py)

#HOW TO WORK/КАК РАБОТАТЬ
To work without GUI or make your own project with mgen, you must copy files generator.py and generatorlist.py in project directory. In generator.py there is four functions: generator() opens command-line version, generate() returns random phrase, gettext($ind) returns phrase with index $ind, and getall() returns arrive with phrases.
Чтобы работать без GUI или использовать в вашем проекте, вы дожны скопировать generator.py и generatorlist.py в директорию проекта. В generator.py есть четыре функции: generator() открывает режим командной строки, generate() возвращает рандомную цитату, gettext($ind) возвращает фразу с индексом $ind, и getall() возвращает массив со всеми цитатами.
