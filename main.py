import speech_recognition as sr
import webbrowser
import pyttsx3 #text to speech
import musiclibrary
import requests 
# import pygame  //to play mp3
# recognizer = sr.Recognizer()  #speech recognition
engine= pyttsx3.init()
newsapi="9f73362b75e34b23a7456d721264f7e8"
url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}'


def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():   
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musiclibrary.music[song]  
        webbrowser.open(link)
    elif "news" in c.lower():
        response = requests.get(url)
        data = response.json()

      # Display top 5 headlines
        print("📢 Latest Headlines:\n")
        for article in data['articles'][:5]:
          speak(f"📰 {article['title']}")
          print(f"🔗 {article['url']}\n")
    
    else:
        # let OpenAI handle request
        pass










if __name__=="__main__":
     speak("Initializing bittu...")
     while True:
          #listen for the wake work "bittu"
           # obtain audio from microphone
            r=sr.Recognizer()


            
        
            print("recognizing")

            # recognize speech using sphinx
            try:
                with sr.Microphone() as source:
                   print("Listening")
                   audio=r.listen(source, timeout=2, phrase_time_limit=1)
                word=r.recognize_google(audio)
                
                if(word.lower() == "bittu"):
                   speak ("hi this is Bittoo. ji maalik boliya ")
                   #listin for command
                   with sr.Microphone() as source:
                       print("bittu active...")
                       audio=r.listen(source)
                       command=r.recognize_google(audio)

                       processCommand(command)
            
            except Exception as e:
                print("google error; {0}".format(e))      

