import speech_recognition as sr
from command_router import route_command

recognizer = sr.Recognizer()

def listen_and_route():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("Heard:", command)

        if "forward" in command:
            route_command("voice", "forward")
        elif "back" in command:
            route_command("voice", "back")
        elif "left" in command:
            route_command("voice", "left")
        elif "right" in command:
            route_command("voice", "right")
        elif "stop" in command:
            route_command("voice", "stop")

    except:
        print("Voice not understood")
