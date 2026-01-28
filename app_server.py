from flask import Flask, request
from motor_control import forward, backward, left, right, stop
from ir_sensor import ir_triggered
from ultrasonic import get_front_distance, get_rear_distance

STOP_DISTANCE = 30

app = Flask(__name__)

def safe():
    return (
        not ir_triggered()
        and get_front_distance() >= STOP_DISTANCE
        and get_rear_distance() >= STOP_DISTANCE
    )

@app.route("/move")
def move():
    direction = request.args.get("dir")

    if not safe():
        stop()
        return "BLOCKED"

    if direction == "forward":
        forward()
    elif direction == "backward":
        backward()
    elif direction == "left":
        left()
    elif direction == "right":
        right()
    elif direction == "stop":
        stop()

    return "OK"

app.run(host="0.0.0.0", port=5000)
