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

def get_audio():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
        said=""
        try:
            said=r.recognize_google(audio)
            print(said)
        except Exception as e:
            print(str(e))
    return said



speak("hey nisarg")
tm=get_audio()
no=random.randint(0,2)
if(no==0):
    tc="stone"
elif no==1:
    tc="paper"
else:
    tc="scissor"

print("computer has choose {}".format(tc))

if tm=="stone" and tc=="stone":
    print("its a tie")
elif tm=="paper" and tc=="paper":
    print("its a tie")
elif tm=="scissor" and tc=="scissor":
    print("its a tie")
elif tm=="stone" and tc=="paper":
    print("computer win !!!")
elif tm=="stone" and tc=="scissor":
    print("nisarg win !!!")
elif tm=="paper" and tc=="stone":
    print("nisarg win !!!")
elif tm=="paper" and tc=="scissor":
    print("computer win !!!")
elif tm=="scissor" and tc=="stone":
    print("computer win !!!")
else:
    print("nisarg win")

