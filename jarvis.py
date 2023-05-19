import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib



command_list = ('command list','wikipedia','open youtube','open google','play music','the time','open code','email to mustafa','who are you','quit')




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        # r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.... \n")
        query = r.recognize_google(audio, language='en-in')
        print(f'Command : {query} \n')
    
    except Exception as e:
        # print(e)
        # print("Say that again please...")
        return 'None'
    
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email@gmail.com', 'password')
    server.sendmail('email@gmail.com', to, content)
    server.close()


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 11:
        speak('Good Morning!')
    
    elif hour >=12 and hour <= 17:
        speak('Good Afternoon!')
    
    else:
        speak('Good Evening!')

    speak('I am Jarvis, please tell me how can i help you')





wish()
while True:
    query = command().lower()
    
    if 'command list' in query:
        print(command_list)

    elif 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2) 
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
        
    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'play music' in query:
        song_dir = 'H:\\Audio Song'
        songs = os.listdir(song_dir)
        Nsong = random.randint(0, len(songs))
        print('Playing Music...\n')
        speak('Playing Music')
        os.startfile(os.path.join(song_dir, songs[Nsong]))

    elif 'the time' in query:
        Time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f'Sir, The time is {Time}')
        speak(f'Sir, The time is {Time}')
    
    elif "open code" in query:
        codePad = "C:\\Users\\User\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePad)

    elif 'email to mustafa' in query :
        try:
            speak("What should I say?")
            content = command()
            to = "mostofaEmail@gmail.com"    
            sendEmail(to, content)
            speak("Email has been sent!")
        except Exception as e:
            # print(e)
            speak("Sorry Sir. I am not able to send this email")

    elif 'who are you' in query:
        print('I am Jarvis, I am a simple AI program Developed by MD Mustafa Ahmed')
        speak('I am Jarvis, I am a simple AI program Developed by MD Mustafa Ahmed, please tell me how can i help you')

    elif 'quit' in query:
        speak('Thank you sir, see you soon')
        exit()

    elif 'how are you' in query:
        speak('I am Good , what about you Sir')