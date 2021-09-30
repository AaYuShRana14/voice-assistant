
import smtplib
import sys
import pyttsx3
import datetime
import speech_recognition as sr
import os
import cv2
import wikipedia
import webbrowser
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0])
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning ")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening ")
    speak("I am jarvis. Please tell me how can I help you")
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('xyz@gmail.com','password')
    server.sendmail('xyz@gmail.com',to,content)
    server.close()
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold=1
        audio=r.listen(source,timeout=1,phrase_time_limit=5)
    try:
        print("Recognizing")
        query=r.recognize_google(audio,language='en-in')
        print("User said ", query)
    except Exception as e:
        # print (e)
        print("Say that again")
        return "None"
    return query
if __name__ == '__main__':
    wishMe()
    while True:
        if 1:
            query=takecommand().lower()
            if 'open notepad' in query:
                speak("opening notepad")
                npath="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad"
                os.startfile(npath)
            elif 'open comand prompt' in query:
                speak("opening comand promt")
                os.startfile("start cmd")
            elif 'open spotify' in query:
                speak("opening spotify")
                spath = "C:\\Users\\Aayush\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Chrome Apps\\Spotify"
                os.startfile(spath)
            elif "camera" in query:
                cap=cv2.VideoCapture(0)
                while True:
                    ret, img=cap.read()
                    cv2.imshow('webcam',img)
                    k=cv2.waitKey(50)
                    if k==5:
                        break
                cap.release()
                cv2.destroyAllWindows()
            elif "play game" in query:
                gpath="C:\\Users\\Desktop\\Counter-Strike Global Offensive.url"
                os.startfile(gpath)
                sys.exit()
            elif "wikipedia" in query:
                speak("Searching wikipedia......")
                query=query.replace("wikipedia","")
                results=wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                print(results)
                speak(results)
            elif 'open youtube' in query:
                speak("opening you tube")
                webbrowser.open("www.youtube.com")
            elif 'open instagram' in query:
                speak("opening instagram")
                webbrowser.open("www.instagram.com")
            elif 'google' in query:
                speak("What should i search on google")
                cm=takecommand().lower()
                webbrowser.open(f"{cm}")
            elif "email" in query:
                try:
                    speak("what should i send sir")
                    content=takecommand().lower()
                    to="xyz@gmail.com"
                    sendEmail(to,content)
                    speak("Email has been sent")
                except Exception as e:
                    speak("Sorry i am not able to send e mail")
            elif "stop" in query:
                speak("Thank you have a great day")
                sys.exit()
            speak("Sir do you have any other work")




