import pyautogui
import psutil
import ctypes
import time
import wmi
import pyttsx3

# Initialize speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# ------------------- Volume Control -------------------
def control_volume(command):
    if "mute" in command:
        pyautogui.press("volumemute")
        speak("Volume muted.")
    elif "volume up" in command or "increase volume" in command:
        pyautogui.press("volumeup")
        speak("Volume increased.")
    elif "volume down" in command or "decrease volume" in command:
        pyautogui.press("volumedown")
        speak("Volume decreased.")

# ------------------- Brightness Control -------------------
def set_brightness(level):
    try:
        wmi_obj = wmi.WMI(namespace='wmi')
        methods = wmi_obj.WmiMonitorBrightnessMethods()[0]
        methods.WmiSetBrightness(level, 0)
        speak(f"Brightness set to {level} percent.")
    except Exception as e:
        print("Brightness not supported:", e)
        speak("Brightness control is not supported on this device.")

# ------------------- Battery Check -------------------
def battery_check():
    battery = psutil.sensors_battery()
    if battery is None:
        print("Battery info not available.")
        speak("Battery information is not available on this device.")
        return

    percent = battery.percent
    plugged = battery.power_plugged
    status = "plugged in" if plugged else "on battery"

    message = f"Battery is at {percent} percent and is {status}."
    print(message)
    speak(message)

    if not plugged and percent < 20:
        ctypes.windll.user32.MessageBoxW(0, "Battery Low", "Plug in your charger", 1)

# ------------------- Optional Command Router -------------------
def handle_system_command(command):
    if "battery" in command:
        battery_check()
    elif "volume" in command:
        control_volume(command)
    elif "brightness" in command:
        # Example: set to 50%
        set_brightness(50)  # You can parse % from voice command
    else:
        speak("I did not understand the system command.")

