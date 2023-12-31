import subprocess   # used to turn off or to restart pc
import pyttsx3      # text to speech conversion library 
import speech_recognition as sr     # converts the speech to text
import wikipedia        # extracts data’s required from Wikipedia
import datetime     # inbuilt module to access the date n time 
import webbrowser   # inbuilt module to fetch the data from web
import pyjokes
import time	    # retrieves the current time
import os 
import pyaudio
import tkinter as tk

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:   # from speech recognition module,i have used Microphone module to listen 
        print("Listening...")         # the command given by the user
        r.pause_threshold=1
        audio = r.listen(source,timeout=3, phrase_time_limit=3)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print("command given is:-",query)

    except Exception as e:
        print(e)
        print("Didn't get it..please say that again sir")
        return "None"

    return query

def speak(audio):
    engine=pyttsx3.init()
    voices=engine.getProperty("voices")             # getter method(gets the current value of engine property)

    engine.setProperty("voice",voices[0].id)        # setter method .[0]=male voice and [1]=female voice in set Property.

    engine.say(audio)       # method for speaking of the assistant
    engine.runAndWait()

def tellday():
    day=datetime.datetime.today().weekday()+1   #it will indicate the number or key
	                                            # that will help  in telling the day
    Day_dict = {1: 'Monday', 2: 'Tuesday',
				3: 'Wednesday', 4: 'Thursday',
				5: 'Friday', 6: 'Saturday',
				7: 'Sunday'}
    
    if day in Day_dict.keys():
        day_of_the_week=Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)

def telltime():
    time=str(datetime.datetime.now())       #o/p:   the time will be displayed like
    print(time)                             # this "2021-15-11 17:50:14.582630"
    hr=time[11:13]                          # n then after slicing we can get time
    min=time[14:16]
    speak("the time is"+hr+" hours and "+min+"minutes")

def hello():
    speak("hello sir, i am your desktop assistant. tell me how may i help you")

def take_query():
    hello()         # calling the Hello function for making it more interactive
	            

    while(True):        #this loop will run until unless the exit command is called
        query=takecommand().lower()    

        #1.INTRODUCTION OF THE ASSISTANT AND SOME COMMON TALKS
        if "tell me your name" in query or "what is your name" in query or "who are you" in query:
            speak("i am rio, your desktop assistant")
            continue
        
        elif "how are you" in query or "is everything ok" in query:
            speak("i am fine,thank you")
            speak("how are you sir")
            continue
        elif "fine" in query or "all well" in query:
            speak("thats good to know that you are fine.")
            continue
        elif "who created you" in query or "who made you" in query:
            speak("i am created by amit")
            continue
        elif "you are smart" in query or "you are intelligent rio" in query:
            speak("dont you think its too hurry, you should first take my test.")
            continue

        #2. JOKES
        elif "joke" in query:
            speak("here are some jokes for you sir..")
            speak(pyjokes.get_joke())
            print(pyjokes.get_joke())
            time.sleep(2)
        
        #3. ACCESSING YOUTUBE
        elif "youtube" in query or "play youtube" in query or "open youtube" in query:
            speak("opening youtube")                            # in the open method we just to give the link
            webbrowser.open("http://www.youtube.com")           # of the website and it automatically open
            time.sleep(5)                                              # it in your default browser

        #4. ACCESSING WIKIPEDIA
        elif "from wikipedia" in query:
            speak("checking wikipedia...")      #fetch the data from wikipedia
            query=query.replace("wikipedia","")

            result=wikipedia.summary(query,sentences=4)         #it will give the summary of 4 lines from wikipedia
            speak("according to wikipedia..")
            print(result)
            speak(result)
            time.sleep(2)

        #5. ACCESSING GOOGLE
        elif "google" in query:
            speak("searching in google")
            webbrowser.open("http://www.google.com")
            time.sleep(5)

        #6. ACCESSING TODAY'S DAY
        elif "which day it is" in query or "what is the today" in query or "day" in query:
            tellday()
            time.sleep(2)

        #7. ACCESSING DATE AND INSTANT TIME
        elif "time" in query or "what is the time now" in query or "tell me the time" in query:
            telltime()
            time.sleep(2)
            
        #8. OPENING MY NOTEPAD   
        elif"open notepad" in query:
            speak("opening notepad")
            os.system('notepad')
            time.sleep(5)
            
        
        #9. OPENING MY MAIL
        elif "mail" in query or "open my gmail" in query:
            speak("accessing your mail")
            webbrowser.open("http://www.gmail.com")
            speak("mail is opened in new tab")
            time.sleep(2)

        #10.NEWS HEADLINES
        elif "news" in query:
            webbrowser.open("https://timesofindia.indiatimes.com/home/headlines")
            speak("here are some headlines from times of india")
            time.sleep(2)
            
        #11. OPENING WHATSAPP   
        elif 'whatsapp' in query:
            speak("opening whatsapp") 
            webbrowser.open_new_tab("https://web.whatsapp.com/")
            
        #12.OPENING CAMERA    
        elif "open camera" in query:
            speak("opening camera sir")
            os.system('camera')
        
        #13. PLAYING MUSIC    
        elif "play music" in query:
            speak("playing music") 
            webbrowser.open_new_tab("https://www.jiosaavn.com/")  

        #14. CONCLUDING TIME
        elif "bye" in query or "bye bye" in query or "good bye" in query:
            speak("bye bye sir,have a good day ahead")       # this will exit and terminate the program
            exit()

        #15.SHUTTING DOWN THE SYSTEM
        elif "shutdown system " in query:
            speak("your system is shutting down..")
            subprocess.call(["shutdown","/l"])
            exit()
        #16.
        elif "search"  in query:
            query = query.replace("search", "")
            webbrowser.open_new_tab(query)
            continue


def create_gui():
    window = tk.Tk()
    window.title("Desktop Assistant")

    label = tk.Label(window, text="Desktop Assistant", font=("Helvetica", 16))
    label.pack(pady=10)

    start_button = tk.Button(window, text="Start Assistant", command=take_query)
    start_button.pack(pady=10)

    exit_button = tk.Button(window, text="Exit", command=window.destroy)
    exit_button.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    create_gui()

if __name__=="__main__":
    take_query()        #main method for executing the above functions