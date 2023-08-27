import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
engine=pyttsx3.init('sapi5') # windows api for voices
voices=engine.getProperty('voices')
# print (voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Namaste,good morning Bhhai")
    elif hour>=12 and hour<18:
        speak("Namaste,good afternoon Bhhai")
    else:
        speak("Namaste,Good evening Bhhai")
    
    speak("I am AryaMate. Please tell me how can I help you bhhai?")

def takeCommand():
    # it takes microphone input from the user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n") 

    except Exception as e:
        print("say that again please...")
        return "None"
    return query



if __name__=="__main__":
    speak("Aryansh is a good guy")
    wishMe()
    while True:
        query=takeCommand().lower() #logic for executing tasks in query
        if 'wikipedia' in query:
            speak('searching Wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com") 
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open cricbuzz' in query:
            webbrowser.open("cricbuzz.com") 
        elif 'play paris ka trip' in query:
            webbrowser.open("https://youtu.be/zM6s3JgF9_0?si=D-9rmuS2Tmu20yMJ")
        elif 'play on top' in query:
            webbrowser.open("https://youtu.be/aFWDOFg7X2A?si=4pSadNMBO1jXqv13")
        elif 'play still rollin' in query:
            webbrowser.open("https://youtu.be/0mCVpUDCkEk?si=PZWYXSW_a_orNeAH")  
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"bhhai,the time is {strTime}") 
        elif 'open arena' in query:
            codePath="C:\\Users\\Aryansh Shukla\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)  
        elif 'stop' in query:
            break           

             


