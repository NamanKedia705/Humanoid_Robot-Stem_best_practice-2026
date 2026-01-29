import speech_recognition as sr
from command_router import route_command
from ai_assistant import handle_ai_command
from navigation import navigate_forward
from command_router import route_command

recognizer = sr.Recognizer()
WAKE_WORD = "jarvis"

def listen_and_route():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("Heard:", command)

        # WAKE WORD CHECK
        if WAKE_WORD not in command:
            return  # ignore everything else

        # Strip wake word
        command = command.replace(WAKE_WORD, "").strip()

        if command == "":
            speak("Yes?")
            return
        # 1️⃣ Navigation commands
        if "navigate forward" in command:
            speak("Starting navigation.")
            navigate_forward()
            return

        # 2️⃣ Movement commands
        if command in ["forward", "back", "left", "right", "stop"]:
            route_command("jarvis", command)
            return

        # 3️⃣ AI / assistant commands
        handled = handle_ai_command(command)
        if handled:
            return

        speak("Sorry, I did not understand that.")

    except:
        print("Voice not understood")
