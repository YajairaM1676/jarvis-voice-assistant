"""
Name: jarvis.py
Author: Juju
Created: 2/22/26
Purpose: Main JARVIS speech recognition program
"""

import speech_recognition as sr
import pyttsx3
from wikipedia_oop import WikipediaApp


# Initialize speech engine
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def get_command():
    """Capture voice command from microphone"""
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening . . .")
        audio = r.listen(source)

        try:
            print("Recognizing . . .")
            command = r.recognize_google(audio)
            print("You said:", command)
            return command.lower()

        except:
            print("Google Speech Recognition could not understand what you said.")
            return ""


def main():
    wiki = WikipediaApp()

    while True:
        print("\n+--------------------+")
        print("|  JARVIS Main Menu |")
        print("+--------------------+")
        print("Commands: wikipedia, exit")

        speak("Say a command")
        command = get_command()

        if "wikipedia" in command:
            speak("What would you like to search for on Wikipedia?")
            print("\n+--------------------+")
            print("| Search Wikipedia  |")
            print("+--------------------+")

            search_term = get_command()

            if search_term:
                result = wiki.get_wikipedia(search_term)
                print("\n" + result)
                speak(result)

        elif "exit" in command:
            speak("Goodbye! Have a good day!")
            print("\nGoodbye!")
            print("Have a good day!")
            break

        else:
            print("Command not recognized.")


if __name__ == "__main__":
    main()
    
