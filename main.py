#Imported libraries

import speech_recognition as sr
from gtts import gTTS
import os
from datetime import datetime
import playsound 
import wikipedia
import pyaudio
import webbrowser
import time 
import pyjokes
import sys
from tkinter import *
import subprocess
import wolframalpha
import requests
import json 
import pvporcupine
import struct
import winsound

#get mic audio
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        readySound()
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

def readySound():
    winsound.Beep(600,250)

#function to respond to commands for Hera
def respond(text):
     if 'youtube' in text:
          speak("What am I searching youtube for?")
          keyword = get_audio()
          if keyword!= '':
            url = f"https://www.youtube.com/results?search_query={keyword}"
          webbrowser.get().open(url)
          speak(f"Here is what i found for {keyword} on youtube.")
     elif 'search' in text:
        speak("What would you like me to search Wikipedia for?")
        query = get_audio()
        if query != '':
            result = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            print(result)
            speak(result)
     elif 'open sound pad' in text:
         speak("time to troll")
         try:
            os.startfile("E:\Steam\steamapps\common\Soundpad\Soundpad.exe")
         except:
             speak("Error opening the program sir.")
             pass   
     elif 'joke' in text:
         speak(pyjokes.get_joke())
     elif 'what time' in text:
         strTime = datetime.today().strftime("%H:%M %p")
         speak(strTime)
     elif 'map' in text:
         speak("Where would you like me to look on the map today?")
         keyword = get_audio()
         if keyword != '':
            url = f"https://www.google.com/maps/place/" + str(keyword)
            speak("Give me just a few seconds as i locate where " + keyword + " is.")
            webbrowser.get().open(url)
            speak(f"Here is where i found {keyword} on the map.")
     elif 'directions' in text:
         speak("Where do you need directions from?")
         keyword = get_audio()
         speak("Where are you headed to?")
         query = get_audio()
         if keyword != '':
             url = f"https://www.google.com/maps/dir/" + str(keyword) + "/" + str(query)
             speak("Ok, now locating directions to " + query + ".")
             webbrowser.get().open(url)
             speak(f"Here are your directions to {query}. I hope this helps.")
     elif 'weather' in text:
         #api_key = " dba892a3bd240e50139b6fd2bcfc766b"
         url =  "https://api.open-meteo.com/v1/forecast?latitude=38.8114&longitude=-91.1415&current_weather=True&temperature_unit=fahrenheit&"
         speak("Here is the weather in Warrenton, Missouri")
         
         
         response = requests.get(url)
         x = response.json()

         print(x['current_weather'])
         #speak(x['current_weather'])  
     elif 'stop listening' in text:
        speak("Until next time, goodbye")
        exit()

def main():
    porcupine = None
    pa = None
    audio_stream = None
    
    try:
        porcupine =  pvporcupine.create(
        keywords=['computer', 'terminator']
        )
        pa = pyaudio.PyAudio()
        audio_stream = pa.open(
            rate=porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine.frame_length
        )

        while True:
            pcm = audio_stream.read(porcupine.frame_length)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

            keyword_index = porcupine.process(pcm)
            if keyword_index >=0:
                print("Detected..", end="")
                speak("Hera is listening.")
                text = get_audio()
                respond(text)
                time.sleep(5)
                speak("Request completed")
    finally:
        if porcupine is not None:
            porcupine.delete()

        if audio_stream is not None:
            audio_stream.close()

        if pa is not None:
            pa.terminate()

main()        
     