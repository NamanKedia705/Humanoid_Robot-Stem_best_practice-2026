"""
ai_assistant.py
Handles AI-style voice interaction (Q&A, info, help).
Inspired by Gideon-3 but adapted for robot integration.
"""

import datetime
from speech_output import speak

def get_time():
    return datetime.datetime.now().strftime("%H:%M")

def handle_ai_command(command: str) -> bool:
    """
    Handles AI / conversational commands.
    Returns True if command was handled here.
    Returns False if command should be treated as movement/nav.
    """

    command = command.lower()

    if "who are you" in command:
        speak("I am Jarvis, your transportation assistance robot.")
        return True

    if "what can you do" in command:
        speak(
            "I can move using voice, touchscreen, or mobile app, and I prioritize safety."
        )
        return True

    if "help" in command:
        speak("At your service. You can ask me to move or help you navigate.")
        return True

    if "time" in command:
        speak(f"The time is {get_time()}")
        return True

    return False
