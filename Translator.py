import pyttsx3
import speech_recognition as sr
import os
import googletrans
from googletrans import Translator
from gtts import gTTS
from playsound import playsound
import time

translator = Translator()
def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        import winsound
        duration = 1000  # milliseconds
        freq = 440  # Hz
        winsound.Beep(freq, duration)
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        import winsound
        duration = 1000  # milliseconds
        freq = 440  # Hz
        winsound.Beep(freq, duration)
        return "None"

    return query

def translategl(query):
    speak("SURE SIR")
    print(googletrans.LANGUAGES)
    speak("Choose the language in which you want to translate")
    b = input("To_Lang :- ")
    try:
        result = translator.translate(query, src='en', dest=b)
        text_to_translate = result.text
        speakgl = gTTS(text=text_to_translate, lang=b, slow= False)
        speakgl.save("translated_text.mp3")

        playsound("voice.mp3")
        os.system("start translated_text.mp3")
    except Exception as e:
        print("Unable to translate")

if __name__ == "__main__":
    query = takeCommand()
    translategl(query)