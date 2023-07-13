#Imported libraries

import pytz
import dialogflow_v2beta1 as dialogflow
from Script import *
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
import os.path
import pygame
import threading


#global variables
TALKING = False
SHOW = False
COUNT = 1

#gui info/setup

class imageHandler:
    def __init__(self):
        self.pics = dict()

    def loadFromFile(self, filename, id=None):
        if id == None: id=filename
        self.pics[id]=pygame.image.load(filename).convert()

    def loadFromSurface(self, surface, id):
        self.pics[id]=surface.convert_alpha()

    def render(self,surface,id,position=None,clear=False,size=None):
        if clear == True:
            surface.fill((5,2,23))#

        if position == None:
            picX = int(surface.get_width()/2-self.pics[id].get_width()/2)
        else:
            picX=position[0]
            picY=position[1]

        if size == None:
            surface.blit(self.pics[id],(picX,picY))
        else:
            surface.blit(pygame.transform.smoothscale(self.pics[id],size),(picX,picY))

#initializes display
pygame.display.init()
pygame.display.set_caption("HERA")
screen = pygame.display.set_mode((1000,600),pygame.RESIZABLE)
#screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN) #uncomment this line for fullscreen
handler = imageHandler()

def display():
    #normal orb - not speaking
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/00.jpg","1")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/01.jpg","2")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/02.jpg","3")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/03.jpg","4")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/04.jpg","5")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/05.jpg","6")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/06.jpg","7")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/07.jpg","8")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/08.jpg","9")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/09.jpg","10")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/10.jpg","11")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/11.jpg","12")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/12.jpg","13")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/13.jpg","14")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/14.jpg","15")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/15.jpg","16")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/16.jpg","17")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/17.jpg","18")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/18.jpg","19")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/19.jpg","20")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/20.jpg","21")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/21.jpg","22")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/22.jpg","23")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/23.jpg","24")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/24.jpg","25")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/25.jpg","26")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/26.jpg","27")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/27.jpg","28")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/28.jpg","29")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/29.jpg","30")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/30.jpg","31")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/31.jpg","32")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/32.jpg","33")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/33.jpg","34")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/34.jpg","35")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/35.jpg","36")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/36.jpg","37")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/37.jpg","38")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/38.jpg","39")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/39.jpg","40")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/40.jpg","41")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/41.jpg","42")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/42.jpg","43")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/43.jpg","44")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/44.jpg","45")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/45.jpg","46")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/46.jpg","47")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/47.jpg","48")

    #lighter orb for when hera is speaking
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/100.gif","101")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/101.gif","102")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/102.gif","103")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/103.gif","104")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/104.gif","105")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/105.gif","106")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/106.gif","107")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/107.gif","108")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/108.gif","109")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/109.gif","110")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/110.gif","111")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/111.gif","112")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/112.gif","113")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/113.gif","114")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/114.gif","115")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/115.gif","116")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/116.gif","117")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/117.gif","118")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/118.gif","119")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/119.gif","120")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/120.gif","121")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/121.gif","122")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/122.gif","123")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/123.gif","124")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/124.gif","125")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/125.gif","126")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/126.gif","127")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/127.gif","128")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/128.gif","129")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/129.gif","130")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/130.gif","131")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/131.gif","132")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/132.gif","133")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/133.gif","134")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/134.gif","135")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/135.gif","136")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/136.gif","137")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/137.gif","138")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/138.gif","139")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/139.gif","140")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/140.gif","141")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/141.gif","142")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/142.gif","143")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/143.gif","144")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/144.gif","145")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/145.gif","146")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/146.gif","147")
    handler.loadFromFile(r"C:\Users\mysti\OneDrive\Desktop\Hera/147.gif","148")

def faceA():
    A=240 #left and right on screen
    B=-5 #up and down on screen
    x=550 #size width
    y=550 #size length

    COUNT = 1
    global TALKING
    while True:
        if TALKING == False:
            if COUNT >= 49:
                COUNT = COUNT - 100
            img = str(COUNT)
            handler.render(screen,img,(A,B), True,(x,y))
            pygame.display.update(A,B,x,y)
            time.sleep(.03)
            COUNT = COUNT +1
            if COUNT ==49:
                COUNT=1

        elif TALKING == True:
            if COUNT <= 100:
                COUNT = COUNT + 100
            img = str(COUNT)
            handler.render(screen,img,(A,B), True,(x,y))
            pygame.display.update(A,B,x,y)
            time.sleep(.03)
            COUNT = COUNT +1
            if COUNT ==149:
                COUNT=101


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

def Hmain():
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
            global TALKING
            pcm = audio_stream.read(porcupine.frame_length)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

            keyword_index = porcupine.process(pcm)
            if keyword_index >=0:
                TALKING = True
                print("Detected..", end="")
                speak("Hera is listening.")
                text = get_audio()
                respond(text)
                time.sleep(5)
                speak("Request completed")
                TALKING = False
    finally:
        if porcupine is not None:
            porcupine.delete()

        if audio_stream is not None:
            audio_stream.close()

        if pa is not None:
            pa.terminate()

def Main():
    t1 = threading.Thread(target=Hmain)
    t2 = threading.Thread(target=faceA)

    display()
    t1.start()
    t2.start()

Main()        
     