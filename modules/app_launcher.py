import os
import webbrowser

def open_app(command):
    command = command.lower()

    if "chrome" in command:
        os.system("start chrome")
    elif "vs code" in command or "visual studio code" in command:
        os.system("code")
    elif "word" in command:
        os.system("start winword")
    elif "settings" in command:
        os.system("start ms-settings:")
    elif "mail" in command or "outlook" in command:
        os.system("start outlook")
    elif "brave" in command:
        os.system("start brave")
    elif "notepad" in command:
        os.system("notepad")
    elif "calculator" in command:
        os.system("calc")
    elif "file explorer" in command:
        os.system("explorer")
    elif "paint" in command:
        os.system("mspaint")
    elif "command prompt" in command or "cmd" in command:
        os.system("start cmd")
    elif "task manager" in command:
        os.system("taskmgr")
    
    # Web-based apps
    elif "youtube" in command:
        webbrowser.open("https://www.youtube.com")
    elif "whatsapp" in command:
        webbrowser.open("https://web.whatsapp.com")
    elif "spotify" in command:
        webbrowser.open("https://open.spotify.com")
    elif "gmail" in command:
        webbrowser.open("https://mail.google.com")
    elif "google" in command:
        webbrowser.open("https://www.google.com")
    elif "github" in command:
        webbrowser.open("https://github.com")
    else:
        print("App not recognized or not supported.")

