
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import psutil
import pyjokes

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
newVoiceRate = 160
engine.setProperty('rate', newVoiceRate)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("Current Time is ")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is ")
    speak(date)
    speak(month)
    speak(year)


def greetme():
    speak("Welcome Back Sir!")
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <= 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon")
    elif hour >= 18 and hour <= 22:
        speak("Good Evening")
    else:
        speak("Good Night")

    speak("How can i Help You ")


def takeCmd():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        # print(query)
        # speak(query)
    except Exception as e:
        print(e)
        speak("Please say again ...")

        return "None"
    return query

def cpu():
    usage = str(psutil.cpu_percent())
    speak("your cpu is at "+ usage)
    
def battery():
    battery = psutil.sensors_battery()
    speak(battery.percent)

def joke():
    speak(pyjokes.get_joke())
    

if __name__ == "__main__":
    greetme()
    while True:
        query = takeCmd().lower()
        print(query)

        if "time" in query:
            time()
        if "date" in query:
            date()
        if "offline" in query:
            speak("See You Next Time")
            quit()
        if "your name" in query:
            speak("my name is lily")

        if "wikipedia" in query:
            speak("searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak(result)
        if "chrome" in query:
            speak("What Should  i Search ")
            search = takeCmd().lower()
            chromepath = "C:\Program Files\Google\Chrome\Application\chrome.exe %s"
            wb.get(chromepath).open_new_tab(".com")

        if "log out" in query:
            os.system("shutdown -l")
        elif "restart" in query:
            os.system("shutdown /r /t 1")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")

        if "play song" in query:
            files = ("C:\\Users\\adity\\Music")
            songs = os.listdir(files)
            os.startfile(os.path.join(files, songs[0]))
            quit()
        elif "remind me" in query:
            speak("What should i remind you ")
            data = takeCmd()
            speak("you said me to remember "+data)
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()
        elif "my reminders" in query:
            remember = open("data.txt", "r+")
            speak("you said me to remember "+remember.read())
            remember.truncate(0)
            remember.close()
        
        if "cpu uses" in query:
            cpu()
        elif "battery percentage" in query:
            battery()
        if "joke" in query:
            joke()
            
