#  virtual enviornment is created , as all the libraires will store in the virtual environment 
# pyttsx3 is the library of speech reg. helps to perform the task 
import speech_recognition as sr

import webbrowser as wb
import pyttsx3 


# song = c.lower().split(" ")[1]

music = {
    "hindi Songs"   : "https://www.youtube.com/watch?v=AgX2II9si7w&list=RDGMEM2j3yRsqu_nuzRLnHd2bMVA&start_radio=1",
    "english songs" : "https://www.youtube.com/watch?v=JGwWNGJdvx8&list=RDQMWX8CN9yq1qI&start_radio=1",
    "lofi Songs"    : "https://www.youtube.com/watch?v=1ItW5nYUidw&pp=ygUKbG9maSBzb25ncw%3D%3D",
    "podcast"       : "https://www.youtube.com/results?search_query=podcast",
    "game "         : "https://www.youtube.com/results?search_query=game+stream",
    
}

recognizer  = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    
    engine.runAndWait()

def processCommand(c): 
    if "open google" in c.lower():
        wb.open("https://google.com")
    elif "open Facebook" in c.lower():
        wb.open("https://facebook.com")
    elif "open chatgpt" in c.lower():
        wb.open("https://chatgpt.com/")
    elif "open youtube" in c.lower(): 
        wb.open("https://youtube.com")
    elif "open whatsapp" in c.lower():
        wb.open("https://whatsapp.com")
    elif "open canva" in c.lower():
        wb.open("https://canva.com")
    elif "open redit" in c.lower():
        wb.open("https://redit.com")
    elif "open instagram" in c.lower():
        wb.open("https://instagram.com")
    elif "open github" in c.lower():
        wb.open("https://github.com")  
    elif "open linkedin" in c.lower():
        wb.open("https://linkedin.com")    
    elif "open naukri" in c.lower():
        wb.open("https://naukri.com")
    elif "play" in c.lower():
        for key in music:
            if key.lower() in c.lower():
                wb.open(music[key])


    # for key in music:
    #     if key.lower() in c.lower():
    #         wb.open(music[key])
    #         break



if __name__ =="__main__":
    speak("Initialiazing jarvis.....")
    while True:

        # listem for the wake word jarvis
        # getting audio form microphone 

        r = sr.Recognizer()
       
        print("recognizing...")
    # recognize speech using google
    
        try:
            with sr.Microphone() as source:
                print("Listning..") 
                audio = r.listen(source, timeout= 2, phrase_time_limit= 1)
                
            
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                 
                speak("ya")
                
                with sr.Microphone( ) as source:
                    r.adjust_for_ambient_noise(source, duration=1)
                    print("jarvis Active")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    
                    processCommand(command)
  
        # except sr.UnknownValueError:
        #     print("i dont understand the command")
        
        # except sr.RequestError as e:
        #     print("Sir i don't know; {0}".format(e))
        except Exception as e:
            print("speak Again sir.. {0}".format(e))

    
