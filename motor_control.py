##Python with Raspi 4
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Motor driver pins
MA1= 17   # Left motor forward
MA2= 18   # Left motor backward
MB3= 22   # Right motor forward
MB4= 23   # Right motor backward

GPIO.setup(MA1, GPIO.OUT)
GPIO.setup(MA2, GPIO.OUT)
GPIO.setup(MB3, GPIO.OUT)
GPIO.setup(MB4, GPIO.OUT)

def stop():
    GPIO.output(MA1, 0)
    GPIO.output(MA2, 0)
    GPIO.output(MB3, 0)
    GPIO.output(MB4, 0)

def forward():
    stop()
    GPIO.output(MA1, 1)
    GPIO.output(MB3, 1)

def backward():
    stop()
    GPIO.output(MA2, 1)
    GPIO.output(MB4, 1)

def left():
    stop()
    GPIO.output(MA2, 1)
    GPIO.output(MB3, 1)

def right():
    stop()
    GPIO.output(MA1, 1)
    GPIO.output(MB4, 1)
