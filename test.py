import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
sg90_pin = 21
GPIO.setup(sg90_pin, GPIO.OUT)
pwm = GPIO.PWM(sg90_pin, 50)

def test():
        pwm.start(5)
        time.sleep(1)
        pwm.ChangeDutyCycle(7.5)
        time.sleep(1)
        pwm.ChangeDutyCycle(10)
        time.sleep(1)

test()


GPIO.cleanup()