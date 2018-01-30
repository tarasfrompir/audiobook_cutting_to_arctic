#!/usr/bin/env python3

import shutil # Подключаем модуль

#Подключаем модуль 
import os 

import speech_recognition as sr

#Каталог из которого будем брать изображения 
directory = './sound/wav'

#Получаем список файлов в переменную files 
files = os.listdir(directory)

arctictxt = open('./sound/myvoice/etc/txt.done.data', 'w')

name = 0
outnomer = 0
for file in files:
    name +=1
    # obtain path to "english.wav" in the same folder as this script
    from os import path
    AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), './sound/wav/'+file)

    # use the audio file as the audio source
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file


    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        answer = r.recognize_google(audio, key="AIzaSyCWzMmYVbQVVP6OKrUkSJicGXtIwFZe544", language="uk-UA")
        #print("GSR.co thinks you said " + answer)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    # recognize speech using Wit.ai
    WIT_AI_KEY = "FGDIOCBONK7QLHMPQHQLOUNS37V6BLMK"  # Wit.ai keys are 32-character uppercase alphanumeric strings
    try:
        answerwit = r.recognize_wit(audio, key=WIT_AI_KEY)
        #print("Wit.ai thinks you said " + answerwit)
    except sr.UnknownValueError:
        print("Wit.ai could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Wit.ai service; {0}".format(e))

    # pechataem nomer fayla
    print(format(name)+' '+file)
    if answer==answerwit:
        shutil.copy(r''+'./sound/wav/'+file, r''+'./sound/myvoice/wav/arctic_'+str(outnomer)+'.wav')
        arctictxt.write('( arctic_'+str(outnomer)+' "'+answer+'" )'+ '\n')
        print ('( arctic_'+str(outnomer)+' "'+answer+'" )'+ '\n')
        outnomer += 1



arctictxt.close()



