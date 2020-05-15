import speech_recognition as sr
from time import ctime
import time
import webbrowser
import os
import playsound
import random
from gtts import gTTS

r = sr.Recognizer()

def get_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
           # print(ask)
           yoyo_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        
        try:
            voice_data = r.recognize_google(audio)
            #print('You said:',text)
            
        except sr.UnknownValueError:
            #print("Sorry, I coudn't understand")
            yoyo_speak("Sorry, I coudn't understand")
            

        except sr.RequestError:
            #print('Service down')
            yoyo_speak('Service down')
            
        
        return voice_data


def yoyo_speak(audio_string):
    tts = gTTS(text=audio_string,lang='en')
    r = random.randint(1,10000)
    audio_file = 'audio_'+str(r)+'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)




def respond(voice_data):
    
    if 'what is your name' in voice_data:
        name='Yoyo'
        #print('My name is:',name)
        yoyo_speak('My name is:'+name)
        
    if 'what is the time ' in voice_data:
        time = ctime()
        #print('The time is:'+time)
        yoyo_speak('The time is:'+time)
        
    if 'search' in voice_data:
        search = get_audio('What do you want search for?')
        url = 'https://www.google.com/search?q=' +search
        webbrowser.get().open(url)
        #print('Here is what i found for:'+search)
        yoyo_speak('Here is what i found for:'+search)
        
    if 'find location' in voice_data:
        location = get_audio('What is the location name?')
        url = 'https://www.google.nl/maps/place/' +location+'/&amp;'
        webbrowser.get().open(url)
        #print('Here is the location of:'+location)
        yoyo_speak('Here is the location of:'+location)
        
    if 'exit' or 'stop' or 'quit' in voice_data:
        exit()
    


#print('How can I help you..')   

time.sleep(1)
yoyo_speak('How can I help you..') 
while 1:
    voice_data = get_audio()
    respond(voice_data)