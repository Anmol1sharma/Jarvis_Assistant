import speech_recognition as sr
import pyttsx3

#Firstly we create a recognizer that hears what we say 
r=sr.Recognizer()
#As we recognized the input then we want a engine to say the output
engine=pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
    engine.stop()
def executecommand(c):
    print(c)

if __name__=="__main__":
    
    #Listen for the activation word that is Jarvis
    while True:
        r=sr.Recognizer()
        print("Recognizing....")
        try:
            with sr.Microphone() as source:
                print("Listening")
                audio=r.listen(source,timeout=2,phrase_time_limit=2)
            word=r.recognize_google(audio)
            print(word)
            if(word.lower()=="jarvis"):
                speak("Yes What")
                #Now we are listening for commands
                with sr.Microphone() as source:
                    print("Listening")
                    audio=r.listen(source)
                command=r.recognize_google(audio)
                executecommand(command)

        except Exception as e:
            print(e)

     


