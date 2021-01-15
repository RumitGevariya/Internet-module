Internet module

###PIP is a package manager for Python packages, or modules if you like.

gtts and speech recognition
gtts-cli --all...... print all language
In [ ]:


from gtts import gTTS
from playsound import playsound
playsound()


from gtts import gTTS
a =gTTS("hello Rumit how are you")
a.save("Desktop/gtts/abc.mp3")


from gtts import gTTS
a =gTTS('hello rumit')
a.save('bhai.mp3')

import speech_recognition as sr

#create a object of recognizer
a =sr.Recognizer()
#print("i am your script and listening you....")

with sr.Microphone() as m:
    print("listen")
    a.pause_threshold =0.5
    audio =a.listen(m)
    print("recognition..")
    query =a.recognize_google(audio,language ='eng-in')
    print(query)
    
    
import speech_recognition as sr
a =sr.Recognizer()
#audio ='test.mp3'
with sr.AudioFile('manish.wav') as m:
    audio = a.record(m)
    query =a.recognize_google(audio)
    print(query)
    
    
#task
from gtts import gTTS
from playsound import playsound
from pydub import AudioSegment

import speech_recognition as sr
a =gTTS("how are you?")
a.save("jay2.mp3")

sound = AudioSegment.from_mp3("jay2.mp3")
sound.export("jay2.wav", format="wav")

b =sr.Recognizer()
with sir.AudioFile("jay2.wav") as m:
    audio =b.listen(m)
    quary =b.recognizer_google(audio)
    print(quary)    
