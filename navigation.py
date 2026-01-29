"""
navigation.py
Assisted navigation routines using existing safety + router.
"""

import time
from command_router import route_command
from ultrasonic import get_front_distance
from speech_output import speak

STOP_DISTANCE = 30
NAV_STEP_DELAY = 0.3

def navigate_forward():
    speak("Starting assisted navigation forward.")

    while True:
        if get_front_distance() < STOP_DISTANCE:
            route_command("nav", "stop")
            speak("Obstacle detected. Navigation stopped.")
            break

        route_command("nav", "forward")
        time.sleep(NAV_STEP_DELAY)
