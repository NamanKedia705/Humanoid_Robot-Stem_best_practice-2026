from motor_control import forward, stop
from ir_sensor import ir_triggered
from ultrasonic import get_front_distance, get_rear_distance
import time

STOP_DISTANCE = 30  # cm

print("IR + Dual Ultrasonic safety running")

while True:
    front_dist = get_front_distance()
    rear_dist = get_rear_distance()

    if ir_triggered():
        stop()
        print("IR TRIGGERED → STOP")

    elif front_dist < STOP_DISTANCE or rear_dist < STOP_DISTANCE:
        stop()
        print(
            f"US STOP → Front: {front_dist} cm | Rear: {rear_dist} cm"
        )

    else:
        forward()
        print(
            f"SAFE → Front: {front_dist} cm | Rear: {rear_dist} cm"
        )

    time.sleep(0.1)
