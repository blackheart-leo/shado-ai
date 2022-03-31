from subprocess import call
import speech_recognition as sr

def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        command.adjust_for_ambient_noise(source)
        print("Jarvis is alseep...")
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

while True:

    wake_Up = takecommand()

    if 'wake up' in wake_Up:
        call(["python3", "shado.py"])

    else:
        print("Nothing.......")