import speech_recognition as sr
import webbrowser
import pyttsx3
import datetime
import os
import openai

# Set your OpenAI API key here
openai.api_key = "YOUR_API_KEY"

# Initialize recognizer and speech engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Function for text-to-speech output
def speak(text):
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("Error in speech engine:", e)

# Function to get AI-powered responses from OpenAI
def get_openai_response(prompt):
    try:
        # Call the ChatCompletion API with gpt-3.5-turbo or gpt-4
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if you have access
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        # Extract and return the assistant's response
        answer = response.choices[0].message['content'].strip()
        return answer
    except Exception as e:
        print("Error with OpenAI API:", e)
        return "I'm sorry, I'm unable to process that right now."


# Function to execute various commands
def execute_command(c):
    c = c.lower()
    
   
    # Web-related commands to quickly open the website in browser
    if "google" in c:
        speak("Opening Google")
        webbrowser.open("https://google.com")
    elif "open facebook" in c:
        speak("Opening Facebook")
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    # System commands that uses os library
    elif "open notepad" in c:
        speak("Opening Notepad")
        os.system("notepad")
    elif "what time" in c or "current time" in c:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")
    elif "date" in c:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {current_date}")
    
     # Google Search
    else:
        query = c.replace("search", "").strip()
        speak(f"Searching Google for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")

    # AI-powered response for unrecognized commands
    # else:
    #     speak("Let me think...")
    #     response = get_openai_response(c)
    #     speak(response)
    
# Main function to listen and respond
if __name__ == "__main__":
    while True:
        r = sr.Recognizer()
        print("Recognizing....")
        try:
            with sr.Microphone() as source:
                print("Listening for activation word...")
                audio = r.listen(source, timeout=2, phrase_time_limit=2)
                
            # Recognize the activation word
            word = r.recognize_google(audio)
            print("You said:", word)
            
            # Check if activation word is "Jarvis"
            if word.lower() == "jarvis":
                speak("Yes, what can I do for you?")
                
                # Listen for a command
                with sr.Microphone() as source:
                    print("Listening for command...")
                    audio = r.listen(source, timeout=5, phrase_time_limit=5)
                
                # Recognize and execute the command
                command = r.recognize_google(audio)
                print("Command received:", command)
                execute_command(command)

        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Please repeat.")
        except sr.RequestError:
            print("There seems to be an issue with the speech recognition service.")
        except Exception as e:
            print("An error occurred:", str(e))
