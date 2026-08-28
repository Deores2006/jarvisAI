
import speech_recognition as sr
import pyttsx3
import sys
import sounddevice as sd
import soundfile as sf
import webbrowser
import subprocess
import os
from urllib.parse import quote_plus


engine = pyttsx3.init()

def speak(text):
    print(f"JARVIS: {text}")
    engine.say(text)
    engine.runAndWait()


def listen_command():

    recognizer = sr.Recognizer()

    filename = "temp_audio.wav"
    fs = 44100
    seconds = 3

    print("\nListening...")

    try:

        recording = sd.rec(
            int(seconds * fs),
            samplerate=fs,
            channels=1,
            dtype="int16"
        )

        sd.wait()

        sf.write(filename, recording, fs)

        with sr.AudioFile(filename) as source:

            audio = recognizer.record(source)

            print("Recognizing...")

            query = recognizer.recognize_google(
                audio,
                language="en-IN"
            )

            print(f"You said: {query}")

        if os.path.exists(filename):
            os.remove(filename)

        return query.lower().strip()

    except sr.UnknownValueError:

        print("I couldn't understand you.")

        if os.path.exists(filename):
            os.remove(filename)

        return "none"

    except sr.RequestError:

        print("Speech recognition service unavailable.")

        if os.path.exists(filename):
            os.remove(filename)

        return "none"

    except Exception as e:

        print("Error:", e)

        if os.path.exists(filename):
            os.remove(filename)

        return "none"


applications = {

    "chrome": "chrome",
    "google chrome": "chrome",

    "edge": "msedge",
    "microsoft edge": "msedge",

    "notepad": "notepad",

    "calculator": "calc",

    "paint": "mspaint",

    "file explorer": "explorer",
    "explorer": "explorer",

    "command prompt": "cmd",
    "cmd": "cmd",

    "powershell": "powershell",

    "task manager": "taskmgr",

    "control panel": "control",

    "settings": "start ms-settings:",

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

    "gmail": "https://mail.google.com",

}


def open_application(app_name):

    try:

        command = applications[app_name]

        subprocess.Popen(command, shell=True)

        speak(f"Opening {app_name}, sir.")

        return True

    except Exception as e:

        print("Application error:", e)

        return False


def open_website(site_name):

    try:

        # Known website
        if site_name in websites:

            url = websites[site_name]

        # User said complete URL
        elif site_name.startswith("http://"):

            url = site_name

        elif site_name.startswith("https://"):

            url = site_name

        # User said something like:
        # "open reddit"
        # "open wikipedia"
        # "open espn"
        else:

            url = "https://www.google.com/search?q=" + quote_plus(site_name)

        webbrowser.open(url, new=2)

        speak(f"Opening {site_name}, sir.")

        return True

    except Exception as e:

        print("Website error:", e)

        return False



def open_anything(name):

    name = name.lower().strip()


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

            subprocess.Popen(name, shell=True)

            speak(f"Opening {name}, sir.")

            return True

    except:

        pass



    speak(
        f"I couldn't find an application called {name}. "
        f"I'll search the web for it."
    )

    return open_website(name)


speak("Online and ready, sir.")

while True:

    command = listen_command()

    if command == "none":
        continue


    if (
        "shutdown" in command
        or
        "exit" in command
        or
        "quit" in command
        or
        "stop" in command
    ):

        speak("Powering down. Goodbye, sir.")

        sys.exit()


    elif command.startswith(" open "):

        target = command.replace(" open ", "", 1).strip()

        if target:

            open_anything(target)

        else:

            speak("What would you like me to open, sir?")


    elif command.startswith("search "):

        search_query = command.replace(
            "search ",
            "",
            1
        ).strip()

        if search_query:

            speak(
                f"Searching Google for {search_query}"
            )

            url = (
                "https://www.google.com/search?q="
                + quote_plus(search_query)
            )

            webbrowser.open(url, new=2)


    else:

        speak(
            "I heard you, but I don't know that command yet."
        )