from cProfile import label
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import pywhatkit as kit
import webbrowser
import random
import os
import cv2
from requests import get
import smtplib
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisUi import Ui_MainWindow

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        print("Good Morning sir!")
        speak("Good Morning sir!")
    
    elif hour>=12 and hour<=18:
        print("Good Afternoon sir!")
        speak("Good Afternoon sir!")
        
    else:
        print("good Evening sir!")
        speak("good Evening sir!")

    print("I am jarvis")
    print("how can i help you...")   

    speak("i am jarvis")
    speak("how can i help you")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('mehran8015503307@gmail.com','mehran@+1')
    server.sendmail('mehran8015503307@gmail.com',to, content)
    server.close()


class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExecution()

    def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening...')
            r.pause_threshold = 1
            audio = r.listen(source)
        
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said : {self.query}\n")
        
        except Exception as e:
            print(e)

            print('Say that again please...')
            speak('Say that again please...')
            return "None"
        return query


    def closeapps(self):
        if 'youtube' in self.query:
            webbrowser('TASKKILL /F /im www.youtube.com')
            
        elif 'notepad' in self.query:
            speak('closing notepad')
            os.system('TASKKILL /F /im notepad.exe')
        
        elif 'paint' in self.query:
            speak('closeing paint')
            os.system('TASKKILL /F /im mspaint')

    def TaskExecution(self): 
        wishMe()
        while True:
        
            self.query = self.takeCommand().lower()


            if 'wikipedia' in self.query:
                speak('Searching Wikipedia...')
                self.query = self.query.replace('wikipedia','')
                results = wikipedia.summary(self.query,sentences = 2)
                speak("According to wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in self.query:
                print('opening youtube....')
                speak('opening youtube....')
                webbrowser.open('www.youtube.com')
            
            elif 'play' and 'youtube' in self.query:
                video = self.query.replace('play','')
                speak(f'playing {video} in youtube')
                kit.playonyt(video)
            
            elif 'open google' in self.query:
                speak('opening google')
                webbrowser.open('www.google.com')
            
            elif 'search' and 'in google' in self.query:
                dm = self.takeCommand().lower()
                speak(f'searching {dm} in google')
                webbrowser.open(f'{cm}')

            elif 'who are you' in self.query:
                print('this is advance Jarvis')
                print('Im programmed by mehran and sharib')
                print('Im a virtual assistant i can help by searching playing songs and entertaining for humans')
            
                speak('this is advance Jarvis')
                speak('Im programmed by mehran and sharib')
                speak('Im a virtual assistant i can help by searching playing songs and entertaining for humans')
            
            elif 'how are you' in self.query:
                speak('Im totally fine sir!')
                speak('I wish you too good')
            
            elif 'girlfriend' in self.query:
                speak('No i dont have a girl friend im trying to make please help me')

            elif 'single' in self.query:
                speak('hmmm yes sir im still single')

            elif 'open instagram' in self.query:
                webbrowser.open('www.instagram.com') 
                print('opening instagram...')
                speak('opening instagram...')
                            
            elif 'open facebook' in self.query:
                webbrowser.open('www.facebook.com') 
                print('opening facebook...')
                speak('opening facebook...')
            
            elif 'open linkedin' in self.query:
                webbrowser.open('www.linkedin.com')
                print('opening linkedin...') 
                speak('opening linkedin...')

            elif 'our college' in self.query:
                webbrowser.open('islamiahcollege.edu.in')
                speak('opening the great islamiah college site')

            elif 'show' and 'photo' in self.query:
                path('C:\\Users\\ELCOT\\Pictures\\Camera Roll\\mehran.jpg')
            
            elif 'time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M")
                print(f"{strTime}")
                speak(f"sir, the time is {strTime}") 
            
            elif 'open notepad' in self.query:
                print('opening notepad....')
                speak('opening notepad....')
                path = 'C:\\Windows\\system32\\notepad.exe'
                os.startfile(path)

            elif 'open paint' in self.query:
                print('opening paint....')
                speak('opening paint....')
                path = 'C:\\Windows\\system32\\mspaint.exe'
                os.startfile(path)
            
            elif 'open command prompt' in self.query:
                print('opening command prompt....')
                speak('opening command prompt....')
                os.system('start cmd')
            
            elif 'open camera' in self.query:
                print('opening camera....')
                speak('opening camera....')
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    k = cv2.imshow('webcam', img)
                    k = cv2.waitKey(58)
                    if k==27:
                        break;
                cap.release()
                cv2.destroyAllWindows()
            
            elif 'play songs' in self.query:
                music_dir = 'D:\songs'
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                os.startfile(os.path.join(music_dir, rd))
            
            elif 'ip address' in self.query:
                ip = get('https://api.ipify.org').text
                print(f"your IP address is {ip}")
                speak(f"your IP address is {ip}")
            
            # elif 'send message' in query:
            #     kit.sendwhatmsg('+916381111939','this is testing protocol',2,25)
            
            elif 'send email' in self.query:
                try:
                    speak("what should i say")
                    content = self.takeCommand().lower()
                    to = 'mehranmushrafcon@gmail.com'
                    sendEmail(to,content)
                    speak('Email has been sent successfully')
                except Exception as e:
                    print(e)
                    speak("sorry sir, i am not able to send this email!")    
            
            elif 'speak' in self.query:
                speak('what should i speak')
                cm = self.takeCommand()
                speak(cm)

            elif 'wait' in self.query:
                speak('ok sir take your own time')
                speak('when ever you have any work do not shy to ask me')

            elif 'send message' in self.query:   
                    # Find your Account SID and Auth Token at twilio.com/console
                    # and set the environment variables. See http://twil.io/secure
                    speak("sir what should i say")
                    msz = self.takeCommand()
                    from twilio.rest import Client

                    account_sid = 'AC40fdbd60188b0e47585fba30928466c1'
                    auth_token = '89187423852750ac47aafd538ced167d'
                    
                    client = Client(account_sid, auth_token)

                    message = client.messages \
                        .create(
                            body= msz,
                            from_='+19045130718',
                            to='+919344835171'
                        )

                    print(message.sid)
                    speak('message has been sent successfully')
            
            elif 'close youtube' in self.query:
                self.closeapps()
                
            elif 'close notepad' in self.query:
                self.closeapps()

            elif 'no thanks' in self.query: 
                print('thanks for using me sir , have a good day...!')
                speak('thanks for using me, have a nice day')
                sys.exit()        
            
            elif 'shut down' in self.query:
                os.system('shutdown /s /t 1')

            print('sir, do you have any other work..?')
            speak('sir, do you have any other work')

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
    
    def startTask(self):
        self.ui.movie = QtGui.QMovie("../../Downloads/212508.gif")
        self.ui.jarvisUi.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("../../Downloads/00545cb7179c504433d4c8f5e845f286.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_Date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_Date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)

app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_()) 
        