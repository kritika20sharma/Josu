import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia 
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
        print("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   
        print("Good Afternoon!")
    else:
        speak("Good Evening!") 
        print("Good Evening!") 

    print("I am Josu . Please tell me how may I help you?") 
    speak("I am Josu!. Please tell me how may I help you?")      
    

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:    
        print("Say that again please...") 
        speak("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":

    speak("Hello!")
    print("Hello!")
    wishMe()
    

    while True:
    
        query = takeCommand().lower()

    
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            query = query.replace("search youtube for","")
            result=query.split()
            result="+".join(result)
            search_query="https://www.youtube.com/results?search_query="+result
            webbrowser.open(search_query)
        

        elif 'google' in query:
            query = query.replace("search google for","")
            result=query.split()
            result="+".join(result)
            search_query="https://www.google.com/search?q="+result
            webbrowser.open(search_query)


        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'Your songs directory here'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "path of your compiler here"
            os.startfile(codePath)

#add aditional commands        
#        elif "open application name":
#           path = path of the application
#            os.startfile(path)


        elif "exit" in query:
            speak("bye bye Sir")
            exit()
