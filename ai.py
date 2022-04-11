from subprocess import call
import speech_recognition as sr
from utils import aiVoiceConfirm
import datetime
from playsound import playsound

aiVoices = "sounds/"

def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        command.adjust_for_ambient_noise(source)
        print("Nexus is on standby...")
        command.pause_threshold = 1
        command.dynamic_energy_threshold = False
        audio = command.listen(source)

        try:
            print("Recognizing...")
            query = command.recognize_google(audio, language='en-gb')
            print(f"You said: {query}\n")

        except Exception as e:
            print(e)
            return ""

        return query.lower()

while True:

    wake_Up = takecommand()

    if 'initiate' in wake_Up or 'you there' in wake_Up or 'on' in wake_Up and 'nexus' in wake_Up:
        print("Initiating Nexus...")
        call(["python3", "shado.py"])

    else:
        print("")
    
    if 'kill' in wake_Up or 'shutdown' in wake_Up or 'terminate' in wake_Up or 'shut down' in wake_Up or 'exit' in wake_Up and 'nexus' in wake_Up:
        playsound(aiVoices + "ai-power_down.mp3")
        playsound(aiVoices + "Jarvis-Goodbye.mp3")
        exit()