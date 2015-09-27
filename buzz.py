import time

import RPi.GPIO as GPIO

from config import PIN_NUMBER, BUZZ_SECS, SECRET_PASSWORD


GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_NUMBER , GPIO.OUT)


def buzz(message):
    if message != SECRET_PASSWORD:
        return "No Buzz"

    GPIO.output(PIN_NUMBER, 1)
    time.sleep(BUZZ_SECS)
    GPIO.output(PIN_NUMBER, 0)
