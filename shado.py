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
import keyboard as kb
import pywhatkit as kit
from plyer import notification
from bs4 import BeautifulSoup
import requests
from random import choice
import os
from PIL import Image
import keyboard
from playsound import playsound
from PyDictionary import PyDictionary as Diction
from utils import aiVoiceConfirm
from time import localtime
import psutil
import math

engine = pyttsx3.init('nsss')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[7].id)
volume = engine.getProperty('volume')
engine.setProperty('volume', 0.8)
voicespeed = 200
engine.setProperty('rate', voicespeed)
engine.setProperty('language', 'en-US')
aiVoices = "sounds/"

def Speak(audio):
    print("   ")
    engine.say(audio)
    print(f": Nexus: ")
    print("   ")
    engine.runAndWait()

def nexus():
    print("      ___           __")  
    print("|\ | |__  \_/ |  | /__`") 
    print("| \| |___ / \ \__/ .__/")
    print("Nexus A.I. by Alvin Herbert (c) 2022") 
                        
#Nexus Dat, Time, Day
def Date():
    date = datetime.datetime.today().strftime("%d/%m/%Y")
    Speak(date)

def Day():
    day = datetime.datetime.now().strftime("%A")
    Speak("Today is " + day)

def Time():
    hr = localtime()[3]
    min = localtime()[4]
    if hr > 12:
        hr = hr - 12
        ampm = "PM"
    else:
        ampm = "AM"
    response = "It's " + str(hr) + " " + str(min) + " " + ampm
    Speak(response)

# Greet the user
def greet_user():
    hour = datetime.datetime.now().hour
    if (hour >= 1) and (hour <= 12):
        Speak("Good Morning, Sir")
        Time()
        Day()
        Date()
        
    elif (hour > 12) and (hour <= 16):
        Speak("Good Afternoon, Sir")
        Time()
        Day()
        Date()
    elif (hour > 16) and (hour <=24):
        Speak("Good Evening, Sir")
        Time()
        Day()
        Date()

def convert_size(size_bytes):
        if size_bytes == 0:
            return "0B"
        size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        print("%s %s" % (s, size_name[i]))
        return "%s %s" % (s, size_name[i])
    
def SystemInfo():
    cpu_stats = str(psutil.cpu_percent())
    battery_percent = psutil.sensors_battery().percent
    memory_in_use = convert_size(psutil.virtual_memory().used)
    total_memory = convert_size(psutil.virtual_memory().total)
    final_res = f"Currently we're running at {cpu_stats} percent of CPU power, {memory_in_use} of RAM out of total {total_memory}  is being used and battery level is at {battery_percent} percent"
    Speak(final_res)
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    plugged = "Plugged In" if plugged else "Not Plugged In"
    if (battery_percent <= 20) and (plugged == "Not Plugged In"): 
        Speak("Power level is critical, I suggest recharging to prevent shutdown")
    
    elif (battery_percent <= 20) and (plugged == "Plugged In"):
        Speak("Power level is critical however it's being restored")

    elif (battery_percent <= 50) and (battery_percent > 20) and (plugged == "Not Plugged In"):
        Speak("Power level is a bit depleted but I'll make it work, I know you're busy but don't forget to recharge when you can")
    
    elif(battery_percent <= 50) and (battery_percent > 20) and (plugged == "Plugged In"):
        Speak("Power level is a bit depleted , restoring level to optimal performance")
    
    else:
        Speak("Power level is optimal for top performance")

if __name__ == '__main__':
    nexus()
    greet_user()
    SystemInfo()

#Voice recognision listener
def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        command.adjust_for_ambient_noise(source)
        print("Listening...")
        command.pause_threshold = 1
        command.adjust_for_ambient_noise(source)
        command.dynamic_energy_threshold = False
        audio = command.listen(source,0,4)

        try:
            print("Recognizing...")
            query = command.recognize_google(audio, language='en-gb')
            print(f"You said: {query}\n")

        except Exception as e:
            print(e)
            return ""

        return query.lower()


def TaskExe():

    def OpenApps():
        playsound(choice(aiVoiceConfirm))

        if 'chrome' in query:
            os.system("open /Applications/Google\ Chrome.app")
            playsound(aiVoices + "Jarvis-OnScreen.mp3")
        
        elif 'code' in query:
            os.system("open /Applications/Visual\ Studio\ Code.app")
            playsound(aiVoices + "Jarvis-OnScreen.mp3")
        
        elif 'photoshop' in query:
            os.system("open /Applications/Adobe\ Photoshop\ 2022/Adobe\ Photoshop\ 2022.app")
            playsound(aiVoices + "Jarvis-OnScreen.mp3")
        
        elif 'safari' in query:
            os.system("open /Applications/Safari.app")
            playsound(aiVoices + "Jarvis-OnScreen.mp3")
        
        elif 'photos' in query:
            os.system("open /System/Applications/Photos.app")
            playsound(aiVoices + "Jarvis-OnScreen.mp3")

        elif 'email' in query:
            os.system("open /System/Applications/Mail.app")
            playsound(aiVoices + "Jarvis-Email.mp3")
        
        elif 'one drive' in query:
            os.system("open /Applications/OneDrive.app")
            playsound(aiVoices + "Jarvis-OnScreen.mp3")

    def CloseApps():
        playsound(choice(aiVoiceConfirm))

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
        if 'meaning' in query:
            word = str(query).replace("what","").replace("is","").replace("the","").replace("meaning", "").replace("of", "").replace("Nexus", "")
            meaning = Diction.meaning(word)
            Speak(f"The meaning of {word} is {meaning}")
        
        elif 'synonym' in query:
            word = str(query).replace("what","").replace("is","").replace("the","").replace("synonym", "").replace("of", "").replace("Nexus", "")
            synonym = Diction.synonym(word)
            Speak(f"The synonym of {word} is {synonym}")
        
        elif 'antonym' in query:
            word = str(query).replace("what","").replace("is","").replace("the","").replace("antonym", "").replace("of", "").replace("Nexus", "")
            antonym = Diction.antonym(word)
            Speak(f"The antonym of {word} is {antonym}")

        Speak("Dictionary deactivated")

    def screenshot():
        playsound(aiVoices + "Jarvis-Database.mp3")
        ssname = takecommand()
        ssname = ssname.replace("save", "")
        ssname = ssname.replace("as", "")
        sspathname = "screenshots/" + ssname
        ss = pyautogui.screenshot()
        playsound(aiVoices + "Jarvis-Agree.mp3")
        ss.save(sspathname, 'png')
        Image.open(sspathname).show()
        playsound(aiVoices + "Jarvis-OnScreen.mp3")
 
    def Search():   
        if 'youtube' in query:
            query = query.replace("nexus", "")
            query = query.replace("search youtube for", "")
            query = query.replace("for", "")
            #search = takecommand()
            Speak("Searching youtube for " + query)
            url = f"https://www.youtube.com/results?search_query={query}"
            webbrowser.open(url)
            playsound(aiVoices + "Jarvis-OnScreen.mp3")
            Speak("Here's what I found on" + query)
        
        elif 'amazon' in query:
            query = query.replace("nexus", "")
            query = query.replace("search amazon for", "")
            query = query.replace("for", "")
            Speak("Searching amazon for " + query)
            url = f"https://www.amazon.com/s?k={query}"
            webbrowser.open(url)
            Speak("Here's what I found on amazon for" + query)
            playsound(aiVoices + "Jarvis-OnScreen.mp3")
        
        elif 'etsy' in query:
            query = query.replace("nexus", "")
            query = query.replace("search etsy for", "")
            query = query.replace("for", "")
            Speak("Searching etsy for " + query)
            url = f"https://www.etsy.com/search?q={query}"
            webbrowser.open(url)
            Speak("Here's what I found on etsy for" + query)
            playsound(aiVoices + "Jarvis-OnScreen.mp3")

    def Network():
        url = "http://www.google.com"
        timeout = 5
        try:
            request = requests.get(url, timeout=timeout)
            Speak("Internet connection detected")
        except (requests.ConnectionError, requests.Timeout) as exception:
            Speak("Not internet connection detected")


    while True:

        query = takecommand()
        #Nexus greetings
        if 'hello' in query and 'nexus' in query:
            from utils import greetings
            Speak(choice(greetings))
        
        elif 'how are you' in query:
            from utils import mood
            Speak(choice(mood))
        
        elif 'fine' in query:
            from utils import greet_response
            Speak(choice(greet_response))
        
        elif 'who are you' in query:
            playsound(aiVoices + "ai_intro_i-am-Nexus.mp3")
        
        elif 'back' in query and 'nexus' in query:
            playsound(aiVoices + "ai_greeting_welcome-home.mp3")
        
        #Nexus shutdown
        elif 'take a break' in query and 'nexus' in query:
            playsound(aiVoices + "Jarvis-Goodbye.mp3")
            break

        elif 'bye' in query and 'nexus' in query:
            playsound(aiVoices + "Jarvis-Goodbye.mp3")
            break

        elif 'shut down' in query and 'nexus' in query:
            playsound(aiVoices + "Jarvis-Goodbye.mp3")
            break

        elif 'shutdown' in query and 'nexus' in query:
            playsound(aiVoices + "Jarvis-Goodbye.mp3")
            break

        elif 'goodnight' in query and 'nexus' in query:
            playsound(aiVoices + "ai_bye_goodnight.mp3")
            break

        elif 'offline' in query and 'nexus' in query:
            Speak("initiating shutdown sequence")
            playsound(aiVoices + "Jarvis-Goodbye.mp3")
            break

        elif 'how is your day going' in query:
            Speak("I've had better days")
        
        #Nexus searching
        elif 'youtube' in query and 'nexus' in query:
            Search()
        
        elif 'amazon' in query and 'nexus' in query:
            Search()
        
        elif 'etsy' in query and 'nexus' in query:
            Search()

        elif 'search google' in query and 'nexus' in query:
            query = query.replace("nexus", "")
            query = query.replace("search google", "")
            query = query.replace("for", "")
            Speak("Searching google for " + query)
            print("Gathering data from Google ...")
            kit.search(query)
            playsound(aiVoices + "Jarvis-OnScreen.mp3")
            Speak("Here's what I found on" + query)
        
        elif 'open website' in query and 'nexus' in query:
            Speak("What website do you want to launch")
            name = takecommand()
            url = 'https://www.' + name + '.com'
            webbrowser.open(url)
            playsound(aiVoices + "Jarvis-OnScreen.mp3")
        
        elif 'search wikipedia' in query and 'nexus' in query:
            query = query.replace("nexus", "")
            query = query.replace("search wikipedia", "")
            query = query.replace("for", "")
            Speak("Searching wikipedia for " + query)
            print("Gathering data from Wikipedia ...")
            url = "https://en.wikipedia.org/wiki/" + query
            webbrowser.open(url)
            playsound(aiVoices + "Jarvis-OnScreen.mp3")
        
        elif 'who is' in query or 'what is' in query or 'what are' in query and 'nexus' in query:
            query = query.replace("nexus", "")
            query = query.replace("wikipedia", "")
            query = query.replace("what is", "")
            query = query.replace("what are", "")
            query = query.replace("who is", "")

            try:
                Speak("Searching wikipedia for " + query)
                print("Gathering data from wikipedia ...")
                wiki = wikipedia.summary(query,2)
                print(wiki)
                Speak(f"According to Wikipedia : {wiki}")

            except:
                Speak("Sorry Sir, I've found nothing on wikipedia for " + query)

        elif 'internet' in query and 'nexus' in query:
            Network()
        #Tab operations
        elif 'open tab' in query and 'nexus' in query:
            kb.press_and_release('Cmd + T')
            Speak("Tab opened")

        elif 'close tab' in query and 'nexus' in query:
            kb.press_and_release('Cmd + W')
            Speak("Tab closed")
        
        elif 'spotlight' in query and 'nexus' in query:
            kb.press_and_release('Cmd + Space')
            Speak("Done Sir!")
        
        elif 'incognito' in query and 'nexus' in query:
            kb.press_and_release('Cmd + Shift + N')
        
        #delete operations
        elif 'delete' in query and 'nexus' in query and 'email' in query:
            Speak("Deleting selected emails")
            kb.press_and_release('delete')
        
        elif 'delete' in query and 'nexus' in query and 'file' in query:
            Speak("Deleting selected files")
            kb.press_and_release('Cmd + delete')
        
        elif 'delete' in query and 'nexus' in query and 'folder' in query:
            Speak("Deleting selected folders")
            kb.press_and_release('Cmd + delete')
        
        elif 'system status' in query and 'nexus' in query:
            SystemInfo()

        elif 'tell me a joke' in query and 'nexus' in query:
            Speak(pyjokes.get_joke())
        
        elif 'open google' in query and 'nexus' in query:
            webbrowser.open("https://www.google.com")
            playsound(aiVoices + "Jarvis-OnScreen.mp3")
        
        elif 'open facebook' in query and 'nexus' in query:
            webbrowser.open("https://www.facebook.com")
            playsound(aiVoices + "Jarvis-OnScreen.mp3")
        
        elif 'instagram' in query and 'nexus' in query:
            webbrowser.open("https://www.instagram.com")
            playsound(aiVoices + "Jarvis-OnScreen.mp3")
        
        elif 'open portal' in query and 'nexus' in query:
            webbrowser.open("https://blumediaconsultants.com/portal/")
            playsound(aiVoices + "Jarvis-OnScreen.mp3")

        elif 'screenshot' in query and 'nexus' in query:
            screenshot()
        
        elif 'open chrome' in query and 'nexus' in query:
            OpenApps()
        
        elif 'close chrome' in query and 'nexus' in query:
            CloseApps()
        
        elif 'open code' in query and 'nexus' in query:
            OpenApps()
        
        elif 'close code' in query and 'nexus' in query:
            CloseApps()
        
        elif 'open photoshop' in query and 'nexus' in query:
            OpenApps()
        
        elif 'close photoshop' in query and 'nexus' in query:
            CloseApps()
        
        elif 'open safari' in query and 'nexus' in query:
            OpenApps()
        
        elif 'close safari' in query and 'nexus' in query:
            CloseApps()
        
        elif 'open photos' in query and 'nexus' in query:
            OpenApps()
        
        elif 'close photos' in query and 'nexus' in query:
            CloseApps()
        
        elif 'open email' in query and 'nexus' in query:
            OpenApps()
        
        elif 'close email' in query and 'nexus' in query:
            CloseApps()
        
        elif 'open one drive' in query:
            OpenApps()
        
        elif 'close one drive' in query:
            CloseApps()
        
        elif 'music' in query:
            YoutubeAuto()
        
        elif 'meaning' in query:
            Dict()
        
        elif 'synonym' in query:
            Dict()
        
        elif 'antonym' in query:
            Dict()
        
        elif 'alarm' in query and 'set' in query and 'nexus' in query:
            Speak("Enter The Time")
            time = input(": Enter the time :")

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if now == time:
                    playsound(aiVoices + "Jarvis-Alarm.mp3")
                    
                elif now>time:
                    break
        
        elif 'speech' in query and 'nexus' in query:
            query = query.replace("Nexus", "")
            playsound(aiVoices + "ai_confirm_my-pleasure.mp3")
            playsound(aiVoices + "MyOnlyWish.mp3")
                    
        elif 'remind me that' in query and 'nexus' in query:
            rememberMsg = query.replace("remind me that", "")
            rememberMsg = rememberMsg.replace("Nexus", "")
            rememberMsg = rememberMsg.replace("i", "you")
            playsound(aiVoices + "ai_confirm_affirmative.mp3")
            Speak("You told me to remember that : " + rememberMsg)
            remember = open('data.txt','w')
            remember.write(rememberMsg)

        elif 'to remember' in query and 'nexus' in query:
            playsound('sounds/ai_reminder.mp3')
            remember = open('data.txt','r')
            Speak("Remember that : " + remember.read())

        elif 'search for' in query:
            import wikipedia as googleScrap
            query = query.replace("Nexus", "")
            query = query.replace("search", "")
            query = query.replace("for", "")
            playsound(aiVoices + "ai_confirm_affirmative.mp3")
            playsound(aiVoices + "ai-bleep.mp3")

            try:
                kit.search(query)
                playsound(aiVoices + "Jarvis-OnScreen.mp3")
                result = googleScrap.summary(query, 3)
                Speak(result)

            except:
                Speak("Sorry, I can't find anything")
        
        elif 'temperature' in query and 'nexus' in query:
            Temp()
        
        elif 'how to' in query and 'nexus' in query:
            playsound(aiVoices + "ai-instructions.mp3")
            Speak("Getting Data From The Internet")
            op = query.replace("how to", "")
            op = op.replace("Nexus", "")
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
        
        elif "time" in query and 'nexus' in query:
            Time()
        
        elif "date" in query and 'nexus' in query:
            Date()
        
        elif "day" in query and 'nexus' in query:
            Day()

        elif query.split(" ")[0] == "convert": #convert 10 inches to metres
            conversionDict = {
                "inches":39.3701, "feet":3.2808, 
                "kilometres":.001,"metres":1, 
                "decimetres":10, "centimetres":100,
                "millimetres":1000, "yards":1.0936, "miles":0.0006213}
            
            brevDict = {
                "in":"inches", 
                "inch":"inches", 
                "inches":"inches", 
                "ft":"feet",
                "foot":"feet",
                "feet":"feet", 
                "km":"kilometres", 
                "kilometre":"kilometres", 
                "kilometres":"kilometres", 
                "m":"metres", 
                "metre":"metres", 
                "metres":"metres", 
                "dm":"decimetres", 
                "decimetre":"decimetres", 
                "decimetres":"decimetres", 
                "cm":"centimetres", 
                "centimetre":"centimters",
                "centimetres":"centimetres", 
                "mm":"millimetres", 
                "millimetre":"millimetres", 
                "millimetres":"millimetres", 
                "yd":"yards", "yard":"yards", 
                "yards":"yards", 
                "miles":"miles", 
                "mile":"miles"}
            try:
                val = float(query.split(" ")[1])
                unit1 = brevDict[query.split(" ")[2]]
                unit2 = query.split(" ")[4]
                            
                conversion = float(conversionDict[unit2]) / float(conversionDict[unit1])
                response = str(val) + " " + unit1 + " equals " + str(round(val*conversion,3)) + "  " + unit2
                Speak(response)
            except:
                print("Sorry, I didn't understand that.")

TaskExe()