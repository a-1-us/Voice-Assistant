import webbrowser
import time
import speech_recognition as sr

class Music:
    def play(self, query):
        try:
            # Create YouTube search URL
            url = f"https://www.youtube.com/results?search_query={query}"
            
            # Open the URL in default browser
            webbrowser.open(url)
            
            print("YouTube search opened in your browser!")
            
        except Exception as e:
            print(f"An error occurred: {str(e)}")

def get_voice_query():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say the song name...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I could not understand your speech.")
    except sr.RequestError as e:
        print(f"Could not request results from the speech recognition service; {e}")
    return None


from yt_web import Music, get_voice_query

music = Music()
query = get_voice_query()
if query:
    music.play(query)