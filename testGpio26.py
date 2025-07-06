import RPi.GPIO as GPIO
import time
 
# Pin Definitionen
IN1 = 26  # GPIO26

# Reset GPIO pins
GPIO.cleanup()

GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)

while True:
    GPIO.output(IN1, GPIO.HIGH)
    print("HIGH")
    time.sleep(5)
    GPIO.output(IN1, GPIO.LOW)
    print("LOW")
    time.sleep(5)
