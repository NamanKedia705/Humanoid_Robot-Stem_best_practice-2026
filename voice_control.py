import speech_recognition as sr

recognizer = sr.Recognizer()

def get_voice_command():
    with sr.Microphone() as source:
        print("Listening for command...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("Heard:", command)
        return command
    except:
        return ""
