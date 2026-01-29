import time
from ir_sensor import ir_triggered
from motor_control import stop

print("Watchdog active")

while True:
    if ir_triggered():
        stop()
    time.sleep(0.05)
