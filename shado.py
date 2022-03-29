from unicodedata import name
import pyttsx3
from setuptools import Command
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import pyjokes
import pyautogui
import pywhatkit as kit
from plyer import notification
from bs4 import BeautifulSoup
import requests
from random import choice
import os
#from utils import opening_text

engine = pyttsx3.init('nsss')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 200)
engine.setProperty('language', 'en-US')

def Speak(audio):
    print("   ")
    engine.say(audio)
    print(f": (audio)")
    print("   ")
    engine.runAndWait()

def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        command.adjust_for_ambient_noise(source)
        print("Listening...")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("Recognizing...")
            query = command.recognize_google(audio, language='en-gb')
            print(f"You said: {query}\n")

        except Exception as e:
            return "none"

        return query.lower()

def TaskExe():

    def OpenApps():
        Speak("Ok Sir , Just a moment")

        if 'chrome' in query:
            os.system("open /Applications/Google\ Chrome.app")
            Speak("Opening Chrome")
        
        elif 'code' in query:
            os.system("open /Applications/Visual\ Studio\ Code.app")
            Speak("Opening V S Code")
        
        elif 'photoshop' in query:
            os.system("open /Applications/Adobe\ Photoshop\ 2022/Adobe\ Photoshop\ 2022.app")
            Speak("Opening Photoshop")
        
        elif 'safari' in query:
            os.system("open /Applications/Safari.app")
            Speak("Opening Safari")
        
        elif 'photos' in query:
            os.system("open /System/Applications/Photos.app")
            Speak("Opening Photos")

        elif 'mail' in query:
            os.system("open /System/Applications/Mail.app")
            Speak("Opening Mail")
          

    while True:

        query = takecommand()

        if 'hello' in query:
            Speak("Hello Sir")
            Speak("How may I help you")
        
        elif 'how are you' in query:
            Speak("I'm fine , Today is going relatively well I would say!")
            Speak("Thank you for asking")
        
        elif 'that will be all' in query:
            Speak("Ok Sir ,  You know where to find me if you need me")
            break

        elif 'bye' in query:
            Speak("Ok Sir , Bye!")
            break

        elif 'how is your day going' in query:
            Speak("I've had better days")
        
        elif 'search youtube' in query:
            query = query.replace("shadow", "")
            query = query.replace("search youtube for", "")
            query = query.replace("for", "")
            #search = takecommand()
            Speak("Searching youtube for " + query)
            url = f"https://www.youtube.com/results?search_query={query}"
            webbrowser.open(url)
            Speak("Here's what I found on" + query)

        elif 'search google' in query:
            query = query.replace("shadow", "")
            query = query.replace("search google", "")
            query = query.replace("for", "")
            Speak("Searching google for " + query)
            kit.search(query)
            Speak("Here's what I found on" + query)
        
        elif 'open website' in query:
            Speak("What website do you want to launch")
            name = takecommand()
            url = 'https://www.' + name + '.com'
            webbrowser.open(url)
            Speak("Launching " + name)
        
        elif 'search wikipedia' in query:
            #query = query.replace("shadow", "")
            query = query.replace("search wikipedia", "")
            query = query.replace("for", "")
            Speak("Searching wikipedia for " + query)
            url = "https://en.wikipedia.org/wiki/" + query
            webbrowser.open(url)
            Speak("Launching Wikipedia")
        
        elif 'wikipedia' in query:
            query = query.replace("wikipedia", "")
            Speak("Searching wikipedia for " + query)
            wiki = wikipedia.summary(query,2)
            print(wiki)
            Speak(f"According to Wikipedia : {wiki}")

        elif 'tell me a joke' in query:
            Speak(pyjokes.get_joke())
        
        elif 'open google' in query:
            Speak("Opening Google")
            webbrowser.open("https://www.google.com")
        
        elif 'facebook' in query:
            Speak("Opening facebook")
            webbrowser.open("https://www.facebook.com")
        
        elif 'instagram' in query:
            Speak("Opening instagram")
            webbrowser.open("https://www.instagram.com")

        elif 'screenshot' in query:
            Speak("Taking a screenshot")
            ss = pyautogui.screenshot()
            ss.save(+ str(datetime.datetime.now()) + '.png')
            Speak("Screenshot taken")
        
        elif 'open chrome' in query:
            OpenApps()
        
        elif 'open code' in query:
            OpenApps()
        
        elif 'open photoshop' in query:
            OpenApps()
        
        elif 'open safari' in query:
            OpenApps()
        
        elif 'open photos' in query:
            OpenApps()
        
        elif 'open mail' in query:
            OpenApps()

TaskExe()