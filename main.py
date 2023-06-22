#Imported libraries

import speech_recognition as sr
from gtts import gTTS
import os
import datetime
import playsound 
import wikipedia
import pyaudio
import webbrowser
import time 
import pyjokes


#get mic audio
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except sr.UnknownValueError:
                speak("I'm sorry i didn't catch that.")
        except sr.RequestError:
                speak("I'm sorry, the service isn't available currently.")
    return said.lower() 

#speaks converted text as audio
def speak(text):
    tts = gTTS(text=text, lang='en')
    filename= "voice.mp3"
    try:
        os.remove(filename)
    except OSError:
        pass
    tts.save(filename)
    time.sleep(1)
    playsound.playsound(filename)

#function to respond to commands for Hera
def respond(text):
     print("Text that is from get audio " + text )
     if 'youtube' in text:
          speak("What am I searching youtube for?")
          keyword = get_audio()
          if keyword!= '':
            url = f"https://www.youtube.com/result?search_query={keyword}"
          webbrowser.get().open(url)
     elif 'search' in text:
        speak("Searching Wikipedia...")
        query = text.replace("search", "")
        result = wikipedia.summary(query, sentences=3)
        speak("According to wikipedia")
        print(result)
        speak(result)
     elif 'joke' in text:
         speak(pyjokes.get_joke())
     elif 'exit' in text:
        speak("Until next time, goodbye")
        exit()

while True:
     speak("I am listening...")
     text = get_audio()
     respond(text)
     