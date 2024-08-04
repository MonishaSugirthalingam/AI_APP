import speech_recognition as sr
from requests_html import HTMLSession
import speak

def spech_to_text():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            voice_data=""
            voice_data=r.recognize_google(audio)
            print(voice_data)
            return voice_data
        except sr.UnknownValueError:
            print("sorry")
        except sr.RequestError:
            print("No Internet connect please turn on your internet")
#speech_to_text()