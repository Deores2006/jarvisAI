import speech_recognition as sr
import pyttsx3
import sys
import sounddevice as sd
import soundfile as sf
import webbrowser
import subprocess
import os
from urllib.parse import quote_plus


# Optional voice settings
engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)


def speak(text):
    """Make JARVIS speak and also print the response."""
    print(f"JARVIS: {text}")

    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("TTS Error:", e)


def listen_command():
    """Record microphone input and convert speech to text."""

    recognizer = sr.Recognizer()

    filename = "temp_audio.wav"
    fs = 44100
    seconds = 3

    print("\nListening...")

    try:

        # Record audio
        recording = sd.rec(
            int(seconds * fs),
            samplerate=fs,
            channels=1,
            dtype="int16"
        )

        sd.wait()

        # Save recording
        sf.write(filename, recording, fs)

        # Read audio file
        with sr.AudioFile(filename) as source:

            audio = recognizer.record(source)

        print("Recognizing...")

        # Convert speech to text
        query = recognizer.recognize_google(
            audio,
            language="en-IN"
        )

        print(f"You said: {query}")

        return query.lower().strip()

    except sr.UnknownValueError:

        print("I couldn't understand you.")
        return "none"

    except sr.RequestError:

        print("Speech recognition service unavailable.")
        return "none"

    except Exception as e:

        print("Microphone / Audio Error:", e)
        return "none"

    finally:

        # Always remove temporary audio file
        if os.path.exists(filename):

            try:
                os.remove(filename)

            except Exception:
                pass



applications = {

    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",

    "google chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",

    "edge": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",

    "microsoft edge": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",

    "notepad": "notepad.exe",

    "calculator": "calc.exe",

    "paint": "mspaint.exe",

    "file explorer": "explorer.exe",

    "explorer": "explorer.exe",

    "command prompt": "cmd.exe",

    "cmd": "cmd.exe",

    "powershell": "powershell.exe",

    "task manager": "taskmgr.exe",

    "control panel": "control.exe",
}


websites = {

    "youtube": "https://www.youtube.com",

    "google": "https://www.google.com",

    "wikipedia": "https://www.wikipedia.org",

    "chatgpt": "https://chatgpt.com",

    "github": "https://github.com",

    "instagram": "https://www.instagram.com",

    "facebook": "https://www.facebook.com",

    "whatsapp": "https://web.whatsapp.com",

    "amazon": "https://www.amazon.in",

    "flipkart": "https://www.flipkart.com",

    "linkedin": "https://www.linkedin.com",

    "gmail": "https://mail.google.com"
}


def open_application(app_name):

    app_name = app_name.lower().strip()

    try:

        command = applications[app_name]

        subprocess.Popen(
            command,
            shell=True
        )

        speak(f"Opening {app_name}, sir.")

        return True

    except Exception as e:

        print("Application error:", e)

        speak(
            f"Sorry sir, I couldn't open {app_name}."
        )

        return False


def open_website(site_name):

    site_name = site_name.lower().strip()

    try:

        # Known website
        if site_name in websites:

            url = websites[site_name]

        # Complete HTTP URL
        elif site_name.startswith("http://"):

            url = site_name

        # Complete HTTPS URL
        elif site_name.startswith("https://"):

            url = site_name

        # www.example.com
        elif site_name.startswith("www."):

            url = "https://" + site_name

        # Unknown website
        else:

            # Search Google
            url = (
                "https://www.google.com/search?q="
                + quote_plus(site_name)
            )

        webbrowser.open(url, new=2)

        speak(f"Opening {site_name}, sir.")

        return True

    except Exception as e:

        print("Website error:", e)

        speak("Sorry sir, I couldn't open that website.")

        return False



def open_anything(name):

    name = name.lower().strip()

    if not name:

        speak("Please tell me what you want me to open, sir.")

        return False


    

    if name in applications:

        return open_application(name)


    
    if name in websites:

        return open_website(name)



    if (
        name.startswith("http://")
        or
        name.startswith("https://")
        or
        name.startswith("www.")
    ):

        return open_website(name)


    

    try:

        result = subprocess.run(
            ["where", name],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:

            subprocess.Popen(
                name,
                shell=True
            )

            speak(f"Opening {name}, sir.")

            return True

    except Exception as e:

        print("Windows search error:", e)


   

    speak(
        f"I couldn't find an application called {name}. "
        f"I'll search the web for it."
    )

    return open_website(name)



def google_search(search_query):

    search_query = search_query.strip()

    if not search_query:

        speak("What should I search for, sir?")

        return

    speak(
        f"Searching Google for {search_query}."
    )

    url = (
        "https://www.google.com/search?q="
        + quote_plus(search_query)
    )

    webbrowser.open(
        url,
        new=2
    )


def process_command(command):

    command = command.lower().strip()


    if not command or command == "none":

        return True


    exit_commands = [
        "shutdown",
        "exit",
        "quit",
        "stop",
        "goodbye",
        "power down",
        "power off"
    ]

    for word in exit_commands:

        if word in command:

            speak(
                "Powering down. Goodbye, sir."
            )

            return False



    if command.startswith("open "):

        target = command[5:].strip()

        if target:

            open_anything(target)

        else:

            speak(
                "What would you like me to open, sir?"
            )

        return True


    if command.startswith("search "):

        search_query = command[7:].strip()

        google_search(search_query)

        return True


    if command.startswith("google "):

        search_query = command[7:].strip()

        google_search(search_query)

        return True



    if command.startswith("youtube "):

        search_query = command[8:].strip()

        if search_query:

            speak(
                f"Searching YouTube for {search_query}."
            )

            url = (
                "https://www.youtube.com/results?search_query="
                + quote_plus(search_query)
            )

            webbrowser.open(
                url,
                new=2
            )

        return True


    if command.startswith("open the "):

        target = command[9:].strip()

        if target:

            open_anything(target)

        return True


    # --------------------------------------------------------
    # UNKNOWN COMMAND
    # --------------------------------------------------------

    speak(
        "I heard you, but I don't know that command yet."
    )

    return True


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    speak("Online and ready, sir.")

    while True:

        command = listen_command()

        should_continue = process_command(command)

        if not should_continue:

            break


    sys.exit()


# ============================================================
# START JARVIS
# ============================================================

if __name__ == "__main__":

    main()