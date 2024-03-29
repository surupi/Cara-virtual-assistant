import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import pyjokes

from wikipedia.wikipedia import search


engine= pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
newVoiceRate=200
engine.setProperty('rate',newVoiceRate)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
speak("hi i am jarvis")

def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)

def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

def wishMe():
    speak("welcome")
    

    hour=int(datetime.datetime.now().hour)

    if hour>=6 and hour<=12:
        speak("good morning")
    elif hour>=12 and hour <18:
        speak("good afternoon")
    elif hour>=18 and hour<=24:
        speak("good evening")
    else:
        speak("good night")
    

    speak("how can i help you")


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening......")
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print("Recognising.....")
        query = r.recognize_google(audio, language='en-IN')
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please....")
        return "None"
    return(query)

def sendmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com" , 587)
    server.ehlo()
    server.starttls()
    server.login("jasminethesilentknight1122@gmail.com", "123test")
    server.sendmail("jasminethesilentknight1122@gmail.com",to, content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("E:\\ss.png")

def jokes():
    speak(pyjokes.get_joke())



if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            quit()
        elif "wikipedia" in query:
            speak("Searching....")
            query = query.replace("wikipedia" ,"")
            result = wikipedia.summary(query, sentences=2)
            speak(result)
        elif 'open youtube' in query:
            wb.open("youtube.com")
        elif 'open google' in query:
            wb.open("google.com")
        elif "screenshot" in query:
            screenshot()
            speak("done")
        elif "joke" in query:
            jokes()        