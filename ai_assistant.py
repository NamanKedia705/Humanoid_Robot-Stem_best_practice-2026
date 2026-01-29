"""
ai_assistant.py
Handles AI-style voice interaction and intent routing for Jarvis.
"""

import datetime
from speech_output import speak
from llm_client import ask_llm
from command_router import route_command
from navigation import navigate_forward

def get_time():
    return datetime.datetime.now().strftime("%H:%M")

def handle_ai_command(command: str) -> bool:
    """
    Handles AI + intent-based commands.
    Returns True if handled.
    """

    command = command.lower()

    # 🛑 Highest priority: STOP (always override)
    if "stop" in command:
        route_command("jarvis", "stop")
        speak("Stopping.")
        return True

    # 🧭 Navigation intents
    if "navigate" in command and "forward" in command:
        speak("Starting assisted navigation.")
        navigate_forward()
        return True

    # 🕹️ Movement intents
    if "forward" in command:
        route_command("jarvis", "forward")
        return True

    if "back" in command or "backward" in command:
        route_command("jarvis", "back")
        return True

    if "left" in command:
        route_command("jarvis", "left")
        return True

    if "right" in command:
        route_command("jarvis", "right")
        return True

    # 🤖 Conversational / AI queries
    reply = ask_llm(command)
    speak(reply)
    return True
