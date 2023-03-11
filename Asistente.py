from speech_recognition import Recognizer
from speech_recognition import Microphone
from playsound import playsound
from pyttsx3 import init
import subprocess
from os import system  
import datetime as dt
from time import sleep
from pywhatkit import playonyt 
import platform as os
from pyautogui import hotkey as hk,click  
from webbrowser import open as wb
from builtins import exit as ex

name=os.node()
name=name.lower()
#global condition
condition=False
listener=Recognizer()
listener.dynamic_energy_threshold=False
engine=init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.say("Hola, Buen día, Soy "+name+" tu asistente Virtual, fuí creado por JAKKOB, ¿en que te puedo ayudar?")
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()
    

def listen():
    try: 
        #listener=sr.Recognizer()
        with Microphone() as source:
            
            
            print("Escuchando....")
            print(name)
            listener.adjust_for_ambient_noise(source,duration=0.1)
           #
           #  playsound('export.mp3')
            voice =listener.listen(source, timeout=15)
            
            rec= listener.recognize_google(voice,language='es-PE')
            
            rec=rec.lower()
            
            
            if name in rec:
                rec=rec.replace(name,'')
                print(rec)
                return rec
            else :
                return None
                
    except :
        pass
    

def listenShutdown():
    try:
        with Microphone() as source:
            
            
            
            print("Escuchando....")
            listener.adjust_for_ambient_noise(source,duration=0.2)
            playsound('export.mp3')
            voice =listener.listen(source,timeout=8)
            
            recs= listener.recognize_google(voice,language='es-PE')
            
            recs=recs.lower()
            if recs in recs:
             return recs
            else:
                return None
            
    except:
        pass
    
    

def goToMeet():
   
    
    wb("https://meet.google.com/tzg-bqom-jgx")
    sleep(20)
    hk('ctrlleft','d')#desactivar o activar microfono de meet
    hk('ctrlleft','e')#desactivar o activar camara de meet
    sleep(1)
    click(1277,556)

    


def run():
    
    rec=listen()
    if rec==None :
        Start()
    else:
        if "reproduce"in rec:
            music=rec.replace("reproduce",'')
            talk('reproduciendo'+music)
            playonyt(music)
        elif "hora" in rec:
            hora=dt.datetime.now().strftime("%I:%M %p")
            talk("son las "+hora)
        elif "apagar" in rec or "apaga" in rec:
            
            
            talk("¿Seguro que quieres apagar la pc?")
            
            res=listenShutdown()
            if "sí" in res or "si" in res :
                talk("ok, Apanagado pc, hasta luego! ")
                subprocess.run("shutdown -s -t 4")
                exit(1)
            elif "no" in res:
                talk("Ok, esta bien")
            else:
                talk("lo siento, no te entendí")
                
        elif "word" in rec:
            talk("abriendo word....")
            system("start winword.exe")
        elif "excel" in rec or "exel" in rec:
            talk("Abriendo excel...")
            system("start excel")
        elif "poin" in rec or "point" in rec:
            talk("Abriendo Power point...")
            system("start powerpnt")
        elif "busca" in rec:
            buscar=rec.replace("busca",'')
            url="https://www.google.com/search?q="
            talk(" buscando "+buscar)
            search_url=url+buscar
            wb(search_url)
        elif "asistencia" in rec:
            talk("entrando a la asistencia")
            goToMeet()
        else:
            
            if "duerme" not in rec and "dormir" not in rec:
                talk("Lo siento, no te entendí")
            
            return rec
    return None
              
            
    
            
def Start():
    flag=True
    
    while flag:
        recw =run()
        if recw ==None:
            Start()

        elif "duerme" in recw or "dormir" in recw : 
            flag=False
            talk("Hasta luego, estoy apagándome...")
            ex(1)

Start()