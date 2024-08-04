import pyttsx3

def speak(text):
    #text="I am Monisha"
    engine=pyttsx3.init()
    rate=engine.getProperty('rate')
    engine.setProperty('rate','rate-70')
    engine.say(text)
    engine.runAndWait()
#speak("Hello I am Monisha")

