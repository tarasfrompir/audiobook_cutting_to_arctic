#!/usr/bin/env python3

#Подключаем модуль 
import os

import subprocess

#Каталог из которого будем брать изображения 
directory = './sound/narezka'

#Получаем список файлов в переменную files 
files = os.listdir(directory)

# dlyaskritiya processa
CREATE_NO_WINDOW = 0x08000000


name = 0

for file in files:
    name +=1
    subprocess.call(['ffmpeg', '-i', directory+'/'+file, './sound/wav/output'+str(name)+'.wav'], creationflags=CREATE_NO_WINDOW)



