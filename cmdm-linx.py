import random
import time
import webbrowser
import os
import getpass
from pytube import YouTube

from colorama import Fore, Style

USER_NAME = getpass.getuser()

os.system('clear')

name = getpass.getuser()


a = os.path.basename(__file__)
b = os.path.abspath(__file__).replace(a, '')

print("версия r1.2-linux")
print("если нужна помощь ведите help")
i = 10
for i in range(1,100):
    
    print(name+":",b)
    comand = input("$ ")

    if comand == "close":
        break

    elif comand == "clear":
        os.system('clear')

    elif comand == "rename":
        name = input("Ведите новое имя: ")
            

    elif comand == "fw":
        os.system("firefox")
        
    

    elif comand == "help":
        print("random - генератор числа от нуля до квадриллиона")
        print("rename - переимевать ваше имя")
        print('help - подксазка')
        print("import - импортирование компонентов")
        print("close - закрыть кмд")
        print("create dir - создать папку")
        print("delete dir - удалить папку")
        print("edit file - редактировать - создать файл")
        print("calc - калькулятор")
        print("youtube - скачать видео с youtube")
        print("echo - спамит в терменал")
        print('clear - очистка терминала')
        print("cmd - команда от cmd linux")
        print("fw - запуск firefox")


    elif comand == "random":
        rend = random.randint(0,1000000000000000)
        print(rend)
        


    
    elif comand == "calc":
      print(eval(input("ведите пример: ")))
    
    elif comand == "echo":
        ioa = input("enter text: ")
        sd = 50
        for y in range(1, sd+1):
            time.sleep(0.1)
            print(ioa)



    elif comand == "youtube":
            

            yt = YouTube(input("ведите ссылку на видео (youtube): "))
            stream = yt.streams.get_by_itag(22) 
            stream.download()


    
    elif comand == "cmd":
        cmds = input("команда: ")
        os.system(cmds)

    elif comand == "browser":
        web = input("ссылка на сайт: ")
        webbrowser.open_new_tab(web)
    # импорт



    elif comand == "import":
        print("доступные пакеты: python")
        input()
        
    elif comand == "import python":
        h = 1
        for h in range(1, 101):
            time.sleep(0.1)
            os.system('cls')
            print(h)
            h+1
        os.system('clear')
        os.system('python')
        print("загрузка завершена")

    

    else:
        print(Fore.RED + "'",comand,"'",'не является внутренней или внешней')
        print('командой, исполняемой программой или пакетным файлом.' + Style.RESET_ALL)
        print("Для помощи ведите help")