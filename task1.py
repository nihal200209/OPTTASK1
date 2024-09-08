import speech_recognition as sr
import pyttsx3
import requests

# Initialize speech recognition and text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("Speech recognition service is unavailable.")
            return ""

def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

def process_command(command):
    if "weather" in command:
        city = command.split("in")[-1].strip()
        weather = get_weather(city)
        speak(weather)
    elif "email" in command:
        send_email("Test Subject", "This is a test email", "recipient@example.com")
        speak("Email sent.")
    else:
        speak("I can do that later.")

# Main loop
while True:
    command = listen().lower()
    process_command(command)
