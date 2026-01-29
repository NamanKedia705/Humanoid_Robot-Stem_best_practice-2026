from motor_control import forward, backward, left, right, stop
from ir_sensor import ir_triggered
from ultrasonic import get_front_distance, get_rear_distance
from speech_output import speak

STOP_DISTANCE = 30

def safe_for(command):
    if ir_triggered():
        return False

    if command == "forward":
        return get_front_distance() >= STOP_DISTANCE

    if command == "back":
        return get_rear_distance() >= STOP_DISTANCE

    if command in ["left", "right"]:
        return get_front_distance() >= STOP_DISTANCE

    return True

def route_command(source, command):
    print(f"[{source}] -> {command}")

    # Log EVERYTHING
    with open("command_log.txt", "a") as f:
        f.write(f"{source},{command}\n")

    if command == "stop":
        stop()
        speak("Stopping")
        return
