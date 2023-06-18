#Imported libraries

import speech_recognition as sr



r = sr.Recognizer()

#Gets the default microphone
with sr.Microphone() as source:
    #listens for voice using the microphone
    audio = r.listen(source)

    text = r.recognize_google(audio)

    print(text)