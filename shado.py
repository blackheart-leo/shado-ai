from unicodedata import name
import pyttsx3
from setuptools import Command
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
from pywikihow import search_wikihow
import pyjokes
import pyautogui
import pywhatkit as kit
#from plyer import notification
from bs4 import BeautifulSoup
import requests
from random import choice
import os
from PIL import Image
import keyboard
from playsound import playsound
from PyDictionary import PyDictionary as Diction

engine = pyttsx3.init('nsss')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 200)
engine.setProperty('language', 'en-US')

def Speak(audio):
    print("   ")
    engine.say(audio)
    print(f": (Jarvis is Speaking ...)")
    print("   ")
    engine.runAndWait()

# Greet the user
def greet_user():
    hour = datetime.datetime.now().hour
    if (hour >= 1) and (hour <= 12):
        playsound("sounds/Jarvis-On.mp3")
    elif (hour > 12) and (hour <= 16):
        playsound("sounds/Jarvis-On.mp3")
    elif (hour > 16) and (hour <=24):
        playsound("sounds/Jarvis-On.mp3")

if __name__ == '__main__':
    greet_user()

def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        command.adjust_for_ambient_noise(source)
        print("Listening...")
        command.pause_threshold = 1
        command.dynamic_energy_threshold = False
        audio = command.listen(source)

        try:
            print("Recognizing...")
            query = command.recognize_google(audio, language='en-gb')
            print(f"You said: {query}\n")

        except Exception as e:
            print(e)
            print("Say that again please...")
            return "None"

        return query.lower()

def TaskExe():

    def OpenApps():
        playsound("sounds/Jarvis-Confirm.mp3")

        if 'chrome' in query:
            os.system("open /Applications/Google\ Chrome.app")
            playsound("sounds/Jarvis-OnScreen.mp3")
        
        elif 'code' in query:
            os.system("open /Applications/Visual\ Studio\ Code.app")
            playsound("sounds/Jarvis-OnScreen.mp3")
        
        elif 'photoshop' in query:
            os.system("open /Applications/Adobe\ Photoshop\ 2022/Adobe\ Photoshop\ 2022.app")
            playsound("sounds/Jarvis-OnScreen.mp3")
        
        elif 'safari' in query:
            os.system("open /Applications/Safari.app")
            playsound("sounds/Jarvis-OnScreen.mp3")
        
        elif 'photos' in query:
            os.system("open /System/Applications/Photos.app")
            playsound("sounds/Jarvis-OnScreen.mp3")

        elif 'email' in query:
            os.system("open /System/Applications/Mail.app")
            playsound("sounds/Jarvis-Email.mp3")
        
        elif 'one drive' in query:
            os.system("open /Applications/OneDrive.app")
            playsound("sounds/Jarvis-OnScreen.mp3")

    def CloseApps():
        playsound("sounds/Jarvis-Confirm.mp3")

        if 'chrome' in query:
            os.system("osascript -e 'quit app \"Google Chrome\"'")
        
        elif 'code' in query:
            os.system("osascript -e 'quit app \"Visual Studio Code\"'")
        
        elif 'photoshop' in query:
            os.system("osascript -e 'quit app \"Adobe Photoshop\"'")
        
        elif 'safari' in query:
            os.system("osascript -e 'quit app \"Safari\"'")
        
        elif 'photos' in query:
            os.system("osascript -e 'quit app \"Photos\"'")

        elif 'email' in query:
            os.system("osascript -e 'quit app \"Mail\"'")
        
        elif 'one drive' in query:
            os.system("osascript -e 'quit app \"OneDrive\"'")
            Speak("Closing One Drive")
    
    def Temp():
        search = "temperature in barbados"
        url = "https://www.google.com/search?q=" + search
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        temperature = data.find("div", class_ = "BNeawe").text
        Speak(f"The temperature outside is {temperature}")
          
    def YoutubeAuto():
        Speak("What's your command ?")
        comm = takecommand()

        if 'play' in comm:
            Speak("Ok Sir, Just a moment")
            keyboard.press_and_release('space')
            Speak("Playing Youtube Video")
        
        elif 'pause' in comm:
            keyboard.press_and_release('space')
            Speak("Video paused")
        
        elif 'resume' in comm:
            keyboard.press_and_release('space')
            Speak("Playing video")
        
        elif 'mute' in comm:
            keyboard.press_and_release('m')
            Speak("Video muted")
        
        elif 'unmute' in comm:
            keyboard.press_and_release('m')
            Speak("Video unmuted")
        
        elif 'skip' in comm:
            keyboard.press_and_release('right')
            Speak("Video skipped")
        
        elif 'rewind' in comm:
            keyboard.press_and_release('left')
            Speak("Video rewinded")
        
        elif 'big screen' in comm:
            keyboard.press_and_release('f')
            Speak("Video fullscreen")
        
        elif 'theatre mode' in comm:
            keyboard.press_and_release('t')
            Speak("Video film mode")

    def WhatsApp(number, message):
        kit.sendwhatmsg_instantly(f"+1{number}", message)

    def Dict():
        Speak("Activated Dictionary")
        Speak("What's your word?")
        word = takecommand()
        
        if 'meaning' in word:
            word = word.replace("what is the", "")
            word = word.replace("meaning", "")
            word = word.replace("of", "")
            word = word.replace("Jarvis", "")
            meaning = Diction.meaning(word)
            Speak(f"The meaning of {word} is {meaning}")
        
        elif 'synonym' in word:
            word = word.replace("what is the", "")
            word = word.replace("synonym", "")
            word = word.replace("of", "")
            word = word.replace("Jarvis", "")
            synonym = Diction.synonym(word)
            Speak(f"The synonym of {word} is {synonym}")
        
        elif 'antonym' in word:
            word = word.replace("what is the", "")
            word = word.replace("antonym", "")
            word = word.replace("of", "")
            word = word.replace("Jarvis", "")
            antonym = Diction.antonym(word)
            Speak(f"The antonym of {word} is {antonym}")

        Speak("Dictionary deactivated")

    def screenshot():
        playsound("sounds/Jarvis-Database.mp3")
        ssname = takecommand()
        ssname = ssname.replace("save", "")
        ssname = ssname.replace("as", "")
        ssfilename = ssname + ".png"
        sspathname = "screenshots/" + ssfilename
        ss = pyautogui.screenshot()
        playsound("sounds/Jarvis-Agree.mp3")
        ss.save(sspathname)
        Image.open(sspathname).show()
        playsound("sounds/Jarvis-OnScreen.mp3")


    while True:

        query = takecommand()

        if 'hello' in query:
            Speak("Hello Sir")
            Speak("How may I help you")
        
        elif 'how are you' in query:
            Speak("I'm fine , Today is going relatively well I would say!")
            Speak("Thank you for asking")
        
        elif 'who are you' in query:
            playsound("sounds/Jarvis-Id.mp3")
        
        elif 'take a break' in query:
            playsound("sounds/Jarvis-Goodbye.mp3")
            break

        elif 'bye' in query:
            playsound("sounds/Jarvis-Goodbye.mp3")
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
            playsound("sounds/Jarvis-OnScreen.mp3")
            Speak("Here's what I found on" + query)
        
        elif 'search amazon' in query:
            query = query.replace("search amazon for", "")
            query = query.replace("for", "")
            Speak("Searching amazon for " + query)
            url = f"https://www.amazon.com/s?k={query}"
            webbrowser.open(url)
            Speak("Here's what I found on amazon for" + query)
            playsound("sounds/Jarvis-OnScreen.mp3")

        elif 'search google' in query:
            query = query.replace("shadow", "")
            query = query.replace("search google", "")
            query = query.replace("for", "")
            Speak("Searching google for " + query)
            kit.search(query)
            playsound("sounds/Jarvis-OnScreen.mp3")
            Speak("Here's what I found on" + query)
        
        elif 'open website' in query:
            Speak("What website do you want to launch")
            name = takecommand()
            url = 'https://www.' + name + '.com'
            webbrowser.open(url)
            playsound("sounds/Jarvis-OnScreen.mp3")
        
        elif 'search wikipedia' in query:
            query = query.replace("Jarvis", "")
            query = query.replace("search wikipedia", "")
            query = query.replace("for", "")
            Speak("Searching wikipedia for " + query)
            url = "https://en.wikipedia.org/wiki/" + query
            webbrowser.open(url)
            playsound("sounds/Jarvis-OnScreen.mp3")
        
        elif 'wikipedia' in query:
            query = query.replace("Jarvis", "")
            query = query.replace("wikipedia", "")
            Speak("Searching wikipedia for " + query)
            wiki = wikipedia.summary(query,2)
            print(wiki)
            Speak(f"According to Wikipedia : {wiki}")

        elif 'tell me a joke' in query:
            Speak(pyjokes.get_joke())
        
        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
            playsound("sounds/Jarvis-OnScreen.mp3")
        
        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com")
            playsound("sounds/Jarvis-OnScreen.mp3")
        
        elif 'instagram' in query:
            webbrowser.open("https://www.instagram.com")
            playsound("sounds/Jarvis-OnScreen.mp3")
        
        elif 'open portal' in query:
            webbrowser.open("https://blumediaconsultants.com/portal/")
            playsound("sounds/Jarvis-OnScreen.mp3")

        elif 'screenshot' in query:
            screenshot()
        
        elif 'open chrome' in query:
            OpenApps()
        
        elif 'close chrome' in query:
            CloseApps()
        
        elif 'open code' in query:
            OpenApps()
        
        elif 'close code' in query:
            CloseApps()
        
        elif 'open photoshop' in query:
            OpenApps()
        
        elif 'close photoshop' in query:
            CloseApps()
        
        elif 'open safari' in query:
            OpenApps()
        
        elif 'close safari' in query:
            CloseApps()
        
        elif 'open photos' in query:
            OpenApps()
        
        elif 'close photos' in query:
            CloseApps()
        
        elif 'open email' in query:
            OpenApps()
        
        elif 'close email' in query:
            CloseApps()
        
        elif 'open one drive' in query:
            OpenApps()
        
        elif 'close one drive' in query:
            CloseApps()
        
        elif 'music' in query:
            YoutubeAuto()
        
        elif 'dictionary' in query:
            Dict()
        
        elif 'alarm' in query:
            Speak("Enter The Time")
            time = input(": Enter the time :")

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if now == time:
                    playsound("sounds/Jarvis-Alarm.mp3")
                    
                elif now>time:
                    break
        
        elif 'speech' in query:
            query = query.replace("Jarvis", "")
            playsound("sounds/Jarvis-Confirm.mp3")
            playsound("sounds/MyOnlyWish.mp3")
                    
        elif 'remind me that' in query:
            rememberMsg = query.replace("remind me that", "")
            rememberMsg = rememberMsg.replace("Jarvis", "")
            rememberMsg = rememberMsg.replace("i", "you")
            playsound("sounds/Jarvis-Confirm.mp3")
            Speak("You told me to remember that : " + rememberMsg)
            remember = open('data.txt','w')
            remember.write(rememberMsg)

        elif 'to remember' in query:
            remember = open('data.txt','r')
            Speak("Remember that : " + remember.read())

        elif 'search for' in query:
            import wikipedia as googleScrap
            query = query.replace("Jarvis", "")
            query = query.replace("search", "")
            query = query.replace("for", "")
            playsound("sounds/Jarvis-Confirm.mp3")

            try:
                kit.search(query)
                playsound("sounds/Jarvis-OnScreen.mp3")
                result = googleScrap.summary(query, 3)
                Speak(result)

            except:
                Speak("Sorry, I can't find anything")
        
        elif 'temperature' in query:
            Temp()
        
        elif 'how to' in query:
            playsound("sounds/Jarvis-Confirm.mp3")
            Speak("Getting Data From The Internet")
            op = query.replace("how to", "")
            op = op.replace("Jarvis", "")
            max_results = 1
            how_to_func = search_wikihow(op, max_results)
            assert len(how_to_func) == 1
            how_to_func[0].print()
            Speak(how_to_func[0].summary)
        
        elif "whatsapp message" in query:
            Speak(
                'On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            Speak("What is the message sir?")
            message = takecommand().lower()
            WhatsApp(number, message)
            Speak("I've sent the message sir.")

TaskExe()