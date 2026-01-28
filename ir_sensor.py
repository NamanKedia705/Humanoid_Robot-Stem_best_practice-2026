import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

IR_PINS = [5, 6, 13, 19]  # 4 outer wheels

GPIO.setup(IR_PINS, GPIO.IN)

def ir_triggered():
    for pin in IR_PINS:
        if GPIO.input(pin) == 0:
            return True
    return False
