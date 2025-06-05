import pyttsx3
import datetime
from requests import get
import speech_recognition as sr
import os
import cv2
import random
import webbrowser
import wikipedia
import pywhatkit as kit
import smtplib
import sys
import pyjokes
import pyautogui
import time
from newsapi import NewsApiClient
from email.message import EmailMessage

# Initialize the news API client
newsapi = NewsApiClient(api_key='2d26cd190add4bf28fd06c7571baaa92')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 16:
        speak('Good Afternoon!')
    elif hour >= 16 and hour < 20:
        speak("Good Evening!")
    else:
        speak('Good Night!')
    speak("Hello, I am Jarvis. Please tell me how I can help you.")

def takeCommand():
    """It takes microphone input from the user and returns string output"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')
    except Exception as e:
        print('Say that again please...')
        return 'None'
    return query

def getLatestNews():
    speak("Fetching the latest news...")
    top_headlines = newsapi.get_top_headlines(language='en', country='us', page_size=5)
    articles = top_headlines['articles']
    for i, article in enumerate(articles):
        speak(f"News {i+1}: {article['title']}")
        print(f"News {i+1}: {article['title']}")

def sendEmailWithAttachment(email, password, to_email, subject, message, file_path):
    msg = EmailMessage()
    msg['From'] = email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.set_content(message)

    with open(file_path, 'rb') as f:
        file_data = f.read()
        file_name = f.name
    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(email, password)
        server.send_message(msg)
    speak("Email has been sent with the file.")

if __name__ == "__main__":
    wishMe()
    if 1:
        query = takeCommand().lower()

        if "open code" in query:
            codePath = "C:\\Users\\Hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'close notepad' in query:
            speak('Okay, closing Notepad')
            os.system('taskkill /f /im notepad.exe')
        elif 'set alarm' in query:
            nn = int(datetime.datetime.now().hour)
            if nn == 22:
                music_dir = 'C:\\Users\\Hp\\Music'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))
        elif "open notepad" in query:
            path = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(path)
        elif "open command prompt" in query:
            os.system("start cmd")
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow("webcam", img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()
        elif "play music" in query:
            music_dir = 'C:\\Users\\Hp\\Music'
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"The time is {strTime}")
        elif "ip address" in query:
            ip = get("https://api.ipify.org").text
            speak(f"Your IP address is {ip}")
        elif "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("Sir, what should I search on Google?")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")
        elif "send message" in query:
            speak("Please provide the phone number.")
            phone_number = takeCommand().lower()
            speak("Please provide the message.")
            message = takeCommand().lower()
            kit.sendwhatmsg(phone_number, message, datetime.datetime.now().hour, datetime.datetime.now().minute + 2)
        elif 'email to vaishnavi' in query:
            speak('What should I say?')
            message = takeCommand().lower()
            email = "choudharyvaishnavi312@gmail.com"  # your email id
            password = "iffc zzha ovin dfke"  # your password
            to_email = "manishachoudhary649@gmail.com"
            subject = "Subject of the Email"
            speak("Please enter the file path.")
            file_path = input("Enter the file path: ")  # Using input to get the file path from the user
            sendEmailWithAttachment(email, password, to_email, subject, message, file_path)
        elif 'open facebook' in query:
            webbrowser.open('www.facebook.com')
        elif 'open stackoverflow' in query:
            webbrowser.open('www.stackoverflow.com')
        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)
        elif 'you can sleep' in query:
            speak('Thanks for using me. Have a good day.')
            sys.exit()
        elif "shut down the system" in query:
            os.system("shutdown /s /t 1")
        elif "restart the system" in query:
            os.system("shutdown /r /t 1")
        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        elif "switch the window" in query:
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.keyUp('alt')
        elif "latest news" in query:
            getLatestNews()
