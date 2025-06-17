import speech_recognition as sr
import pyttsx3
import time

# Importing from your own modules
from modules.app_launcher import open_app
from modules.system_control import handle_system_command
from modules.chatbot import chat_with_gemini
from modules.jokes import tell_joke
from modules.utility_tools import take_screenshot, get_current_datetime, get_weather
from modules.file_manager import create_folder, create_file

# Initialize TTS
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio, language="en-IN").lower()
    except:
        return ""

if __name__ == "__main__":
    speak("Hello, I am Jarvis. How can I help you?")

    while True:
        command = listen()
        print("You said:", command)

        if not command:
            continue

        if "open" in command:
            open_app(command)

        elif any(kw in command for kw in ["volume", "brightness", "battery"]):
            handle_system_command(command)

        elif "joke" in command:
            speak(tell_joke())

        elif "chat" in command:
            speak("Okay, let's chat.")
            chat_with_gemini()

        elif "screenshot" in command:
            msg = take_screenshot()
            speak(msg)

        elif "time" in command or "date" in command:
            msg = get_current_datetime()
            speak(msg)

        elif "weather" in command:
            msg = get_weather()
            speak(msg)

        elif "create folder" in command:
            folder_name = command.replace("create folder", "").strip()
            msg = create_folder(folder_name)
            speak(msg)

        elif "create file" in command:
            file_name = command.replace("create file", "").strip()
            msg = create_file(file_name)
            speak(msg)

        elif "exit" in command or "quit" in command:
            speak("Goodbye!")
            break

        time.sleep(1)
