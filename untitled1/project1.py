import datetime
import webbrowser
import os
import pyttsx3
import speech_recognition as sr


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    speak('Hello Tinku')
    hour = int(datetime.datetime.now().hour)
    if (hour >= 0 and hour < 12):
        speak('good morning!')
    elif (hour >= 12 and hour < 18):
        speak('good afternoon!')
    else:
        speak('good evening!')
    speak('I am Sindhu, Tell me how can I help you')


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # r.pause_threshold=1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"user said: {query}\n")
    except Exception as e:
        print(e)
        print("say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if 'hello' in query:
            wishme()
        elif 'open youtube' in query:
            speak('opening youtube')
            webbrowser.open('https://www.youtube.com/')
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'The time is {strTime}')
        elif 'name' in query:
            speak('My name is Sindhu! Your Personal assistant')
        elif 'who are you' in query:
            speak('I am Sindhu')
        elif 'bye' in query:
            speak('See you later! Bye.')
            break
