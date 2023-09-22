from ctypes import cdll
import pyttsx3#pip install pyttsx3
import self #pip install self
import speech_recognition as sr #pip install speechRecognition
import datetime
import webbrowser
import os
import smtplib
import sys
import urllib.request
import time
from time import sleep
from datetime import timedelta
import operator 
import numpy as nm
import self
from playsound import playsound #if error comes then- pip install --upgrade wheel 
# pip uninstall playsound
# pip install playsound==1.2.2
from googletrans import Translator
import googletrans #pip install googletrans
from gtts import gTTS #pip install gtts
import googletrans
from fnmatch import translate
from bs4 import BeautifulSoup
import pywhatkit #pip install pywhatkit
flag = 0


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
rate = engine.setProperty("rate",160)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source,0,4)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)    
        print("Say that again please...")  
        query=""
    query = query.lower()
    return query

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   
    else:
        speak("Good Evening!")
    speak(" I  am  A  Artificial   intelligence  Personalised  Teacher. ")  
    # speak(" .  Thank you.")    

def autotrans(text):
    translator = Translator()
    b = 'en'  
    text_to_translate = translator.translate(text,src = "auto",dest= b,)
    text = text_to_translate.text
    try : 
        speakgl = gTTS(text=text, lang=b, slow= False)
        speakgl.save("voice.mp3")
        playsound("voice.mp3")
        global flag
        flag=1
    except:
        print("Unable to translate")

if __name__ == "__main__":
    wishMe()
    speak("how can I help you.")
    while True:
        query = takeCommand().lower()        
        if flag==1:
            os.remove("voice.mp3")
            flag=0

        elif "what is interference" in query or "interference" in query:
            speak("Interference  refers   to   the    disruption   or   overlapping   of   waves  , causing  the   amplification,  reduction,  or  cancellation of  certain  wave  patterns.")
            sleep(1)
            speak("watch this video also to clear your doubts")
            webbrowser.open("https://aryantalwar.github.io/EdTech.com/y2mate.com%20-%20Interference%20of%20Waves%20%20Superposition%20and%20Interference%20in%20light%20and%20water%20waves%20%20Physics_480p.mp4")

        elif "what is integration" in query or "integration" in query:
            speak("Integration  refers  to   the   process  of  combining   or   merging  different  elements  into   a   unified  whole ,  often  in  the   context  of  mathematics   or  technology.")
            sleep(1)
            speak("watch this video for better understaning")
            webbrowser.open("https://aryantalwar.github.io/EdTech.com/y2mate.com%20-%20Introduction%20to%20integral%20calculus%20%20Accumulation%20and%20Riemann%20sums%20%20AP%20Calculus%20AB%20%20Khan%20Academy_720p.mp4")