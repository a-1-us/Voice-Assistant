import pyttsx3
import speech_recognition as sr
from yt_web import Music

# Initialize and configure the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Initialize the speech recognizer
r = sr.Recognizer()
speak("Hello Tanu, I am your voice assistant. How are you?")

with sr.Microphone() as source:
    # Adjust for ambient noise and set energy threshold
    print("Adjusting for ambient noise... Please wait...")
    r.adjust_for_ambient_noise(source, duration=2)
    r.energy_threshold = 4000  # Increased threshold for better detection
    r.dynamic_energy_threshold = True
    
    while True:
        print("\nListening...")
        try:
            # Listen for audio with timeout and phrase_time_limit
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            print("Processing...")
            
            # Try to recognize the audio
            text = r.recognize_google(audio)
            print("You said:", text)
            
            # Handle different commands
            if "what about you" in text.lower():
                speak("I am also having a good day, ma'am.")
            
            elif "play music" in text.lower() or "play song" in text.lower():
                speak("Which song would you like to play?")
                try:
                    audio = r.listen(source, timeout=5, phrase_time_limit=5)
                    song = r.recognize_google(audio)
                    print("Playing:", song)
                    speak(f"Playing {song} on YouTube"),
                    music = Music()
                    music.play(song)
                except sr.UnknownValueError:
                    speak("Sorry, I couldn't understand the song name. Please try again.")
            
            elif "stop" in text.lower():
                speak("Goodbye! Have a nice day.")
                break
            
            else:
                speak("What can I do for you?")
        
        except sr.WaitTimeoutError:
            print("No speech detected within timeout")
        except sr.UnknownValueError:
            print("Could not understand audio. Please try again.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
            