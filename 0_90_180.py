import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
sg90_pin = 21
GPIO.setup(sg90_pin, GPIO.OUT)
pwm = GPIO.PWM(sg90_pin, 50)
startPos = 2
endPos = 11
angRange = 180.0

def set_angle(ang):
    pwm.start(startPos + ang/angRange*(endPos - startPos))

for i in range(3):
    set_angle(0)
    time.sleep(1)
    set_angle(90)
    time.sleep(1)
    set_angle(180)
    time.sleep(1)



GPIO.cleanup()