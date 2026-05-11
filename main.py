import speech_recognition as sr
import webbrowser as web
import os
import subprocess
import pyttsx3
import requests
import regex as re
from openai import OpenAI
from musicLibrary import musicLibrary

engine = pyttsx3.init()
r = sr.Recognizer()
newsapi = "YOUR_NEWS_API"
weatherapi = "YOUR_WEATHER_API"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
openai_api = "YOUR_OPENAI_API"
def speak(text):
               print(text)
               engine.say(text)
               engine.runAndWait()

def extract_city(text):
    match = re.search(r"(?:in|at|for)\s+([a-zA-Z\s]+)", text)
    if match:
        return match.group(1).strip()

    ignore_words = ["weather", "what", "is", "the", "today", "like", "of","from"]
    words = [w for w in text.split() if w.lower() not in ignore_words]

    return " ".join(words)
   
def processAI(command):
                client = OpenAI(api_key=openai_api)     
            
           
                try:
                    completion = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=[
                            {"role": "system","content": "You are a virtual assistant named zara skilled in general tasks like Alexa and Google Cloud. Give accurate, to the point and short responses please."},
                            {"role": "user", "content": command}    
                
                        ]
                    )

                    return completion.choices[0].message.content

                except Exception as e:
                    print(f"error: {e}")

def ProcessCommand(c):
    c = c.lower()
    if "open google" in c:
               web.open("https://google.com")
    elif "open instagram" in c:
               web.open("https://www.instagram.com")
    elif "open youtube" in c:
                 web.open("https://www.youtube.com")
    elif "open facebook" in c:
               web.open("https://www.facebook.com")
       
    elif "open snapchat" in c or "snap" in c:
        web.open("https://www.snapchat.com")
      
    elif "open chatgpt" in c or "gpt" in c:
        web.open("https://chat.openai.com")

    elif "open linkedin" in c:
        web.open("https://www.linkedin.com")

    elif "open github" in c:
        web.open("https://www.github.com")

    elif "open stack overflow" in c:
        web.open("https://stackoverflow.com")

    elif "open calculator" in c:
        subprocess.run(["C:\\Windows\\System32\\calc.exe"])

    elif "open paint" in c:
        subprocess.run(["C:\\Windows\\System32\\mspaint.exe"])

    elif "open cmd" in c or "open command prompt" in c:
        subprocess.run(["C:\\Windows\\System32\\cmd.exe"])

    elif "open powershell" in c:
        subprocess.run(["C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe"])

    elif "open edge" in c or "open browser" in c:
        subprocess.run(["start", "msedge"], shell=True)

    elif "open word" in c:
        subprocess.run("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")

    elif "open excel" in c:
        subprocess.run(["C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"])

    elif "open powerpoint" in c:
        subprocess.run(["C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"])

    elif "open notepad" in c:
        subprocess.run(["C:\\Windows\\System32\\notepad.exe"])

    elif "open python website" in c or "open pyweb" in c:
        web.open("https://www.python.org")   
    elif "open python" in c:
               subprocess.run(["python"])
        
   
    elif c.startswith("play"):
        song = c[5:].strip().lower()
        if song in musicLibrary:
         link = musicLibrary[song]
         web.open(link)
         print(f"Playing {song}.")
        else: 
            song = c[5:].strip().lower()
            lin = f"https://www.youtube.com/results?search_query={song}"
            web.open(lin)
            print(f"Playing {song}.")

    elif "search" in c:
               search = c.replace("search"," ").strip()
               google = f"https://www.google.com/search?q={search}"
               web.open(google)


    elif "news" in c:
        r = requests.get(f"https://newsapi.org/v2/top-headlines?q=world&sortBy=publishedAt&language=en&apiKey={newsapi}")
        if r.status_code == 200:
           data = r.json()
           articles = data.get('articles', [])
           for article in articles :
            speak(article['title'])

    elif "weather" in c:
        city = extract_city(c)
        if not city:
            speak("City not found")
            return
        print(city)
        url = f"{base_url}q={city}&appid={weatherapi}&units=metric"
        try:
          response = requests.get(url)
          data = response.json()
        
          if response.status_code == 200:
              main = data['main']
              weather = data['weather'][0]

              speak(f"Temperature of {city} is {main['temp']}°C")
              speak(f"Weather Condition {weather['description'].capitalize()}")
              speak(f"Humidity level is {main['humidity']}%")
          else:
            print(f"Error: {data.get('message', 'City not found')}")
            
        except Exception as e:
         print(f"An error occurred: {e}")
        

                     
    else:
        response = processAI(c)
        speak(response)

        
           
if __name__ == "__main__":
               speak("Zara is loading...!")
               speak("Say Zara clearly to wake me up.")

               while True:
                try:
                  command = ""  
                  print("Zara is listening for wakeup word...!")
                  with sr.Microphone() as source:
                    audio = r.listen(source,timeout=3,phrase_time_limit=5)
                    word =  r.recognize_google(audio)
                    word = word.lower()
                    
                    
                  if "zara" in word:
                            
                              speak("Yes?")
                              with sr.Microphone() as source:
                                       audio = r.listen(source,timeout=3,phrase_time_limit=5)
                                       command = r.recognize_google(audio)
                                       print(command)
                                       speak("Just a moment!")
                                       ProcessCommand(command)
                                    #    speak("Anything else Sir!")

                                       
                  elif command == "stop" or command == "exit":
                    speak("ok bye sir")
                    break
 
               
                except Exception as e:
                   print(f"Something went wrong!")
                   

