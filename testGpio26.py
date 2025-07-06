import RPi.GPIO as GPIO
import time
 
# Pin Definitionen
IN1 = 26  # GPIO26
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
 
 
try:
    # Motor vorwärts mit 75% Geschwindigkeit
    GPIO.output(IN1, GPIO.HIGH)
    # pwm.ChangeDutyCycle(100)
    print("Starting motor forward")
    time.sleep(1000)
except KeyboardInterrupt:
    print("Motor stopped by user")
finally:
    GPIO.output(IN1, GPIO.LOW)
    print("Stopping motor")
    GPIO.cleanup()