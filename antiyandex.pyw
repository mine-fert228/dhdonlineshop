import psutil
import os
while True:
    for proc in psutil.process_iter():
        name = proc.name()
        if name == "browser.exe":
            os.system('taskkill /f /IM browser.exe')