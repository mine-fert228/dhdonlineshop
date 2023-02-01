import random
import time
import webbrowser
import os
import subprocess
import getpass
from pytube import YouTube

from colorama import Fore, Style

USER_NAME = getpass.getuser()

os.system('cls')

name = getpass.getuser()




print("версия r1.2")
print("если нужна помощь ведите help")
i = 10
for i in range(1,100):

    print("user:",name)
    comand = input(">>")
    
    if comand == "close":
        break

    elif comand == "clear":
        os.system('cls')

    elif comand == "rename":
        name = input("Ведите новое имя: ")
            
    elif comand == "start":
        a = input("Ведите путь: ")
        uds = a.replace('\\', '/')
        os.startfile(uds)
            


    elif comand == "video":
        l = input("Ведите путь к файлу: ")
        o = l.replace('\\', '/')
        subprocess.call(o, shell=True)
        
    

    elif comand == "help":
        print("random - генератор числа от нуля до квадриллиона")
        print("rename - переимевать ваше имя")
        print('help - подксазка')
        print("import - импортирование компонентов")
        print("close - закрыть кмд")
        print("start - запуск приложений")
        print("video - запуск mp3 - mp4")
        print("create dir - создать папку")
        print("delete dir - удалить папку")
        print("edit file - редактировать - создать файл")
        print("calc - калькулятор")
        print("youtube - скачать видео с youtube")
        print("echo - спамит в терменал")
        print('clear - очистка терминала')
        print("ipconfig - Настройка протокола IP для Windows")
        print("osk - активация экранной клавиатуры")
        print("cmd - команда от cmd windows")


    elif comand == "random":
        rend = random.randint(0,1000000000000000)
        print(rend)
        

    elif comand == "create dir":
        gc = input("имя папки: ")
        os.mkdir(gc)

    elif comand == "delete dir":
        gh = input("путь: ")
        nd = gh.replace('\\', '/')
        os.rmdir(nd)

    elif comand =="edit file":
        print("пример prim.txt(если нету этого файла то он создатся)")
        my_cr = input("имя файла: ")
        my_file = open(my_cr, "a+" )
        uyt = input('ведите текст в файле: ')
        my_file.write(uyt +'\n')
        my_file.close()
    
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


    elif comand == "ipconfig":
        os.system('ipconfig')

    elif comand == "osk":
        os.system('osk')
    
    elif comand == "cmd":
        cmds = input("команда: ")
        os.system(cmds)

    elif comand == "browser":
        web = input("ссылка на сайт: ")
        webbrowser.open_new_tab(web)
    # импорт



    elif comand == "import":
        print("доступные пакеты: pass,python,cmd")
        input()
        
    elif comand == "import cmd":
        j = 1
        for j in range(1, 101):
            time.sleep(0.1)
            os.system('cls')
            print(j)
        os.system('cls')
        os.system('cmd')
        
    elif comand == "import python":
        h = 1
        for h in range(1, 101):
            time.sleep(0.1)
            os.system('cls')
            print(h)
            h+1
        os.system('cls')
        os.system('python')
        print("загрузка завершена")
    elif comand == "import pass":
        pss = input("пароль: ")
        if pss == "maksim":
            print("пароль верный")
            name = "Максим"
        else:
            print("пароль неверный")
            name = "хакер"
    

    else:
        print(Fore.RED + "'",comand,"'",'не является внутренней или внешней')
        print('командой, исполняемой программой или пакетным файлом.' + Style.RESET_ALL)
        print("Для помощи ведите help")