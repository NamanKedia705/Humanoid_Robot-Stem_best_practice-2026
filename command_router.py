from motor_control import forward, backward, left, right, stop
from ir_sensor import ir_triggered
from ultrasonic import get_front_distance, get_rear_distance
from speech_output import speak

STOP_DISTANCE = 30

def safe():
    if ir_triggered():
        return False
    if get_front_distance() < STOP_DISTANCE:
        return False
    if get_rear_distance() < STOP_DISTANCE:
        return False
    return True

def route_command(source, command):
    print(f"[{source}] -> {command}")

    if command == "stop":
        stop()
        speak("Stopping")
        return

    if not safe():
        stop()
        speak("Obstacle detected. Please clear the path.")
        return

    if command == "forward":
        forward()
        speak("Moving forward")

    elif command == "back":
        backward()
        speak("Moving backward")

    elif command == "left":
        left()
        speak("Turning left")

    elif command == "right":
        right()
        speak("Turning right")
