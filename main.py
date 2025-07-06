# =========================
# 📦 IMPORTS
# =========================
import speech_recognition as sr          # For converting speech to text
import pyttsx3                           # For text-to-speech (TTS)
import webbrowser                        # For opening websites
import musicLibrary                      # Custom module: Dictionary of songs and links
import website                           # Custom module: Dictionary of websites and links
from datetime import datetime            # For time and date functions
import jokes                             # For telling jokes from a list of jokes
import pywhatkit                         # For searching and playing YouTube videos
import wikipedia                         # To search from Wikipedia
import time                              # To use delay (in printing mostly)




# =========================
# 🎤 INITIALIZATIONS
# =========================
r = sr.Recognizer()                      # Create recognizer instance
engine = pyttsx3.init()                  # Initialize TTS (text-to-speech) engine

# =========================
# 🗣️ TEXT-TO-SPEECH FUNCTION
# =========================
def speak(text):
    """Makes Nova speak the provided text."""
    engine.say(text)
    engine.runAndWait()

# =========================
# 🗣️ TEXT-AND-SPEECH IN SYNC
# =========================
def print_and_speak(text):
    '''Makes Nova speak and print in sync word by word as if it is typing'''
    words = text.split()
    for word in words:
        print(word, end=" ", flush=True)
        time.sleep(0.3)

    print()                                     # for printing new line
    engine.say(text)
    engine.runAndWait()

# =========================
# 🧠 PROCESS USER COMMAND
# =========================
def processCommand(c):
    """Executes actions based on the user's spoken command."""
    print("\nCommand:", c.upper())
    command = c.lower().strip()  # Normalize command to lowercase and trim whitespace

    # 0. EXIT COMMAND
    if any(word in command for word in 
           ['stop','quit','exit','shutdown','ruk']):            # Check for these words in command to stop Nova
        
        speak("Goodbye. Shutting down Nova...")          
        print("👋 Nova is shutting down...")
        exit()                                                  # Built-in function to stop the program

    # 1. OPEN WEBSITE
    elif 'open' in command:
        site = command.split("open", 1)[1].strip()  # Extract website name after 'open'
        link = website.sites.get(site)              # Use .get() to avoid KeyError

        if link:
            webbrowser.open(link)
            speak(f"Opening {site}")
        else:
            speak("Sorry, I couldn't find the site.")

    # 2. PLAY MUSIC
    elif 'play' in command:
        song = command.split("play", 1)[1].strip()                # Extract song name after 'play' 
        # Remove common YouTube phrases (English + Hindi)
        for key in ["from youtube", "on youtube", "youtube par", "youtube me"]:
            if key in song:
                song = song.split(key, 1)[0].strip()              # Extract song name before these keys 

        # Try from predefined music library first
        link = musicLibrary.music.get(song)                       # Use .get() for safe lookup
        if link:                                                  
            webbrowser.open(link)
            print_and_speak(f"🎧 Playing {song}")
            # speak(f"Playing {song}")
        else:
            try:
                print_and_speak(f"🎧 Playing {song} on youtube")
                # speak(f"Playing {song}")                      # Speak the cleaned song name
                pywhatkit.playonyt(song)                        # pywhatkit.playonyt play the song from youtube 

            except Exception as e:
                # print(f"❌ Couldn't find {song} on YouTube — {e}")
                print_and_speak(f"Sorry Ritesh, I couldn't find {song} on YouTube.")
            
    
    # 3. TELL CURRENT TIME
    elif 'time' in command:
        now = datetime.now()
        current_time = now.strftime("%I:%M %p")             # %I for Hour, %M for Minutes and %p for AM/PM
        print_and_speak(f"The current time is {current_time}")        # prints the current time (3:45 PM)
        # speak(f"The current time is {current_time}")        # speaks the current time (3:45 PM)  
        

    # 4. TELL TODAY"S DATE
    elif 'date' in command:
        today = datetime.now()
        current_date = today.strftime("%A, %d %B %Y")       # %A for Day, %d for date of Month, %B for Month and %Y for year
        print_and_speak(f"Today's date is {current_date}")            # prints today's date (Monday, 30 June 2025)
        # speak(f"Today's date is {current_date}")            # speaks today's date (Monday, 30 June 2025)

    # 5. TELL A JOKE
    elif 'joke' in command:
        joke = jokes.tell_joke()                            # Gets the random joke from jokes.py 
        print_and_speak("🤣 Here's a joke: ",joke)                    # print the joke before telling
        # speak(joke)                                         # speaks up the joke
    
    # 6. SEARCH ON BROWSER
    elif 'search' in command:
        query = command.split("search",1)[1].strip()        # Get everything after 'search'
        print_and_speak(f"Searching {query}")                         
        pywhatkit.search(query)                             # Search query on default browser
    
    # 7. WIKIPEDIA SEARCH
    elif any (kw in command for kw in ['what is', 'who is', 'tell me about']):              
        query = command                                                                      # Start with full command
        for kw in ['what is', 'who is', 'tell me about', 'can you', 'tell me', 'please']:    # known phrases for clean search
            query = query.replace(kw, "").strip()                                            # remove those phrases 

        print_and_speak(f"Searching Wikipedia for {query}")
        try:
            result = wikipedia.summary(query, sentences=2)                      # Fetching 2 line summary from wikipedia
            print_and_speak(result)   
            # speak(result)
        except:
            print_and_speak("Sorry Ritesh! couldn't find anything on Wikipedia")

    else:
        print_and_speak("Ritesh is still working on that...")         #KAAM KARO AUR, ADD MORE FESTURES

# =========================
# 🚀 MAIN LOOP
# =========================
if __name__ == "__main__":
    speak("Initializing Nova...")

    while True:
        try:
            print("\n🔍 Recognizing...")

            # === LISTEN FOR WAKE WORD ===
            with sr.Microphone() as source:
                # Adjust for background noise (helps accuracy)
                r.adjust_for_ambient_noise(source, duration=1)

                print("🎙️ Listening for wake word...")
                audio = r.listen(source, timeout=10, phrase_time_limit=8)

                # Convert spoken audio to text
                word = r.recognize_google(audio)
                trigger = word.lower().strip()

                # === WAKE WORD DETECTED ===
                if "nova" in trigger:
                    print("🟢 Wake word 'Nova' detected.")

                    # === LISTEN FOR USER COMMAND ===
                    with sr.Microphone() as source:
                        print("🔊 Nova heard you! Listening for command...")
                        audio = r.listen(source)

                        # Convert speech to text
                        command = r.recognize_google(audio)

                    # Confirm and execute command
                    speak("Yaa Ritesh")
                    processCommand(command)

                # === WAKE WORD NOT DETECTED ===
                else:
                    print("🚫 No wake word detected. Restarting...")
                    continue

        # =========================
        # ⚠️ EXCEPTION HANDLING
        # =========================
        except sr.WaitTimeoutError:
            print("⏳ Timeout: No speech detected. Try again.")

        except sr.UnknownValueError:
            print("❌ Speech not clear. Could not understand.")

        except sr.RequestError:
            print("⚠️ Could not connect to Google's speech service.")

        except Exception as e:
            print("🚨 Unexpected Error:", e)
