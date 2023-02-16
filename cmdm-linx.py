import random
import time
import webbrowser
import os
import getpass
import requests
from pytube import YouTube

from colorama import Fore, Style , Back

USER_NAME = getpass.getuser()

os.system('clear')

name = getpass.getuser()


a = os.path.basename(__file__)
b = os.path.abspath(__file__).replace(a, '')

print(Fore.RED + "версия r1.4-linux")
print(Fore.GREEN + "если нужна помощь ведите help"+ Style.RESET_ALL)
i = 10
for i in range(1,100):
    
    print(Fore.BLUE + name+":",b)
    comand = input(Fore.GREEN + "$ " + Style.RESET_ALL)

    if "close" in comand:
        break

    elif "clear" in comand:
        os.system('clear')

    elif comand == "rename":
        name = input("Ведите новое имя: ")
            

    elif "fw" in comand:
        os.system("firefox")
        
    

    elif "help" in comand:
        print("random - генератор числа от нуля до квадриллиона")
        print("rename - переимевать ваше имя")
        print('help - подксазка')
        print("import - импортирование компонентов")
        print("close - закрыть кмд")
        print("calc - калькулятор")
        print("youtube - скачать видео с youtube")
        print("echo - спамит в терменал")
        print('clear - очистка терминала')
        print("cmd - команда от cmd linux")
        print("fw - запуск firefox")
        print("pack install - установка приложений на ваш пк")


    elif "random" in comand:
        rend = random.randint(0,1000000000000000)
        print(rend)
        


    
    elif "calc" in comand:
      print(eval(input("ведите пример: ")))
    
    elif "echo" in comand:
        ioa = input("enter text: ")
        sd = 50
        for y in range(1, sd+1):
            time.sleep(0.1)
            print(ioa)



    elif "youtube" in comand:
            

            yt = YouTube(input("ведите ссылку на видео (youtube): "))
            stream = yt.streams.get_by_itag(22) 
            stream.download()


    
    elif "cmd" in comand:
        cmds = input("команда: ")
        os.system(cmds)

    elif "browser" in comand:
        web = input("ссылка на сайт: ")
        webbrowser.open_new_tab(web)
    # импорт



    elif "import" in comand:
        print("доступные пакеты: python")
        input()
        
    elif comand == "import python":
        h = 1
        for h in range(1, 101):
            time.sleep(0.1)
            os.system('clear')
            print(h)
            h+1
        os.system('clear')
        os.system('python3')
        print("загрузка завершена")

    elif "pack install" in comand:
        def save_from_site(link,namefile):
            r = requests.get(link, allow_redirects=True)
            open(namefile, "wb").write(r.content)
            print(f"загрузка завершена Путь: {os.getcwd()}\{namefile}")
        print('доступные пакеты:')
        print('blot - блокнот')
        pack = input('Название пакета: ')
        if pack == 'blot':
            save_from_site('https://raw.githubusercontent.com/mine-fert228/dhdonlineshop/main/ea3a5b32bf2688fd.uto','блокнот.pyw')
        else:
            print(Fore.RED + f"Нет пакета по имени {pack}")

    else:
        print(Fore.RED + "'",comand,"'",'не является внутренней или внешней')
        print('командой, исполняемой программой или пакетным файлом.' + Style.RESET_ALL)
