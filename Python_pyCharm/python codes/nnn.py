import playsound
import os
import time
import speech_recognition as sr
from gtts import gTTS
import random

def speak(text):
    tts=gTTS(text=text,lang='en')
    file='voice.mp3'
    tts.save(file)
    playsound.playsound(file)

speak("helloooo")
speak("whatttttt")