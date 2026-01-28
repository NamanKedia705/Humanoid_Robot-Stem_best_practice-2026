from motor_control import forward, backward, left, right, stop
from ir_sensor import ir_triggered
from ultrasonic import get_front_distance, get_rear_distance
from voice_control import get_voice_command
import time

STOP_DISTANCE = 30

print("Voice control + safety running")

while True:
    command = get_voice_command()

    front = get_front_distance()
    rear = get_rear_distance()

    if ir_triggered() or front < STOP_DISTANCE or rear < STOP_DISTANCE:
        stop()
        print("SAFETY STOP")
        continue

    if "forward" in command:
        forward()
    elif "back" in command:
        backward()
    elif "left" in command:
        left()
    elif "right" in command:
        right()
    elif "stop" in command:
        stop()

    time.sleep(0.1)
