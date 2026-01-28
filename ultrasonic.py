import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 20
ECHO = 21

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def get_distance():
    GPIO.output(TRIG, False)
    time.sleep(0.05)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    start = time.time()
    while GPIO.input(ECHO) == 0:
        start = time.time()

    end = time.time()
    while GPIO.input(ECHO) == 1:
        end = time.time()

    distance = (end - start) * 17150
    return round(distance, 2)
