#Imported libraries

import speech_recognition as sr
from gtts import gTTS
import os
import datetime
import playsound 
import wikipedia
import pyaudio


#get mic audio
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
                print("Exception " + str(e))
    return said 

#speaks converted text as audio
def speak(text):
    tts = gTTS(text=text, lang='en')
    filename= "voice.mp3"
    try:
        os.remove(filename)
    except OSError:
        pass
    tts.save(filename)
    playsound.playsound(filename)

#test number 1
text = get_audio()
speak(text)