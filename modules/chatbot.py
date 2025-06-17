import os
import requests
import speech_recognition as sr
import pyttsx3
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for chat input...")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio, language="en-IN").lower()
    except:
        return ""

def chat_with_gemini():
    speak("You can start talking to me. Say 'bye' to end the chat.")
    while True:
        user_input = listen()
        print("You:", user_input)

        if "bye" in user_input:
            speak("Goodbye, exiting chat mode.")
            break

        response = ask_gemini(user_input)
        print("Jarvis:", response)
        speak(response)

def ask_gemini(prompt):
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
    headers = {
        "Content-Type": "application/json"
    }
    params = {
        "key": GEMINI_API_KEY
    }
    data = {
        "contents": [
            {
                "role": "user",
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, params=params, json=data)
        if response.status_code == 200:
            return response.json()['candidates'][0]['content']['parts'][0]['text']
        else:
            print("Error:", response.status_code)
            print("Response:", response.text)
            return "Sorry, I couldn't understand."
    except Exception as e:
        print("Exception:", e)
        return "Sorry, I couldn't understand."

if __name__ == "__main__":
    chat_with_gemini()

