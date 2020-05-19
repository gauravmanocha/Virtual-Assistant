import pyttsx3
from datetime import *
import speech_recognition as sr
import wikipedia
import webbrowser
import os

#Initialization of pyttsx3 module
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

#Creating a function which will speak the given command
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#A function which will greet the user according to time of the system
def wish():
    hour = int(datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Good Morning!")
        speak("Good Morning!")

    elif hour >= 12 and hour < 17:
        print("Good Afternoon!")
        speak("Good Afternoon!")

    else:
        print("Good Evening!")
        speak("Good Evening!")

    print("How may I help you?")
    speak("How may I help you?")

#SpeechRecognition intialization with expection handling
#It will take the input from the user as speech and will store in query
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("say that again please...")
        speak("say that again please!")
        return  "None"
    return query


if __name__ == "__main__":
    wish()
    while True:
        #Converting the input from user in lower so that no problem occurs when matching with query
        query = takeCommand().lower()

        #When the user asks it's name, this condition will execute
        if 'your name' in query:
            print("I am Jarvis. Jarvis stands for Just A Rather Very Intelligent System")
            speak('I am Jarvis!.Jarvis stands for! Just A Rather Very Intelligent System ')
            print()

        #If the input from the user contains "how are you" string, this condition will undergo
        elif 'how are you' in query:
            print("For computer software, I'm living the dream. Thanks for asking")
            speak("For computer software,, I'm living the dream. Thanks for asking")
            print()

        # This command will show wikipedia results
        # You just have to say for example Chris Evans Wikipedia
        # It will search for Chris Evans on wikipedia
        elif 'wikipedia' in query:
            print('Searching Wikipedia...')
            speak('Searching Wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)  # sentences = 2 implies read 2 sentences only from the results
            print('According to wikipedia')
            speak('According to wikipedia')
            print(results)
            speak(results)
            print()

        #Open youtube command will open youtube on your system broswer
        elif 'open youtube' in query:
            print("Opening youtube...")
            speak("Opening youtube")
            webbrowser.open("youtube.com")
            break #As you have opened youtube, the while loop will break

        #Same goes for opening google and email
        elif 'open google' in query:
            print("Opening Google...")
            speak("Opening google")
            webbrowser.open("google.com")
            break #As you have opened google, the while loop will break


        elif 'open email' in query:
            print("Opening Email...")
            speak("Opening E-mail")
            webbrowser.open("gmail.com")
            break #As you have opened email, the while loop will break


        elif 'open spotify' in query:
            musicPath = "C:\\Users\\DELL\\Desktop\\Spotify" #You must add path of spotify in your system.
            print("Opening Spotify...")
            speak("Opening Spotify")
            os.startfile(musicPath)
            break #As you have opened spotify, the while loop will break

        elif 'open twitter' in query:
            print("Opening Twitter...")
            speak("Opening Twitter")
            webbrowser.open("twitter.com")
            break #As you have opened twitter, the while loop will break

        #This command will open whatsapp in web
        elif 'open whatsapp' in query:
            print("Opening Whatsapp...")
            speak("Opening Whatsapp")
            webbrowser.open("web.whatsapp.com")
            break #As you have opened whatsapp, the while loop will break

        #For general talking you can ask it questions
        elif 'What you can do for me' in query:
            print('All that you expect from me')
            speak('All that you expect from me!')
            print()

        elif ('do you have any friend' or 'do you have any friends') in query:
            print("Yeah! Alexa, Google assistant and Siri are my friends and my idols")
            speak("Yeah! Alexa, Google assistant and Siri are my friends and my idols")
            print()

        #This command will give you the current time as per your system timings
        elif 'the time' in query:
            strTime = datetime.now().strftime("%H:%M:%S")
            print("It's", strTime)
            speak(f"It's {strTime}")
            print()

        #For closing the program, Just use close or quit in your input
        elif 'close' in query:
            print("Good-Bye until next time")
            speak("Good-Byeee! until next time")
            break

        elif 'quit' in query:
            print("Quiting...   GoodBye..")
            speak("Quiting!! Goodbyeee")
            break

