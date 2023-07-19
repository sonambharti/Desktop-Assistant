import pywintypes
import pyttsx3  #text-to-speech conversion
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib, ssl



"""
pip install wikipedia
pip install SpeechRecognition
pip install pyttsx3
"""

def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[
        0].id)
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon sir")
    else:
        speak("Good Evening")
    speak("I am your assistant here. Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    server.login('s.bharti14021999@gmail.com', 'Google@2020')

    server.sendmail('s.bharti14021999@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query1 = takeCommand().lower()
            query = query.replace("wikipedia", query1)
            # finding result for the search
            # sentences = 2 refers to numbers of line
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("www.google.com")

        elif 'tutorials point' in query:
            webbrowser.open("https://www.tutorialspoint.com")


        elif 'play music' in query:
            music_dir = "C:\\Users\\Sonam\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'tell time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print(strTime)

        elif 'open code' in query:
            codePath = "D:\\Python\\CountSumSubseqArr.py"
            os.startfile(codePath)

        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "subodh9955509176@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")

            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")

        elif 'stop' in query:
            exit()

            '''
                smtp_server = "smtp.gmail.com"
                port = 465 # For starttls
                sender_email = "s.bharti14021999@gmail.com"
                password = input("Type your password and press enter: ")

                # Create a secure SSL context
                context = ssl.create_default_context()

                # Try to log in to server and send email
                try:
                    server = smtplib.SMTP(smtp_server, port)
                    server.ehlo()  # Can be omitted
                    server.starttls(context=context)  # Secure the connection
                    server.ehlo()  # Can be omitted
                    server.login("s.bharti14021999@gmmail.com", "Account@2020")
                    server.sendmail(sender_email, "subodh9955509176@gmail.com", "m")
                    server.close()
                except Exception as e:
                    print (e)
            '''
