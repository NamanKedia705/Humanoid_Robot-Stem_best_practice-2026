from motor_control import forward, stop
from ir_sensor import ir_triggered
import time

print("IR safety test running")

while True:
    if ir_triggered():
        stop()
        print("IR TRIGGERED → STOP")
    else:
        forward()
        print("SAFE → FORWARD")

    time.sleep(0.1)
