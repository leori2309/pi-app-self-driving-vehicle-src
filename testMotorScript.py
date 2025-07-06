import RPi.GPIO as GPIO
import time
 
# Pin Definitionen
IN1 = 23  # GPIO23
IN2 = 24  # GPIO24
ENA = 18  # GPIO18 (PWM)
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)
 
pwm = GPIO.PWM(ENA, 1000)  # PWM mit 1kHz
pwm.start(0)
 
try:
    # Motor vorwärts mit 75% Geschwindigkeit
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    pwm.ChangeDutyCycle(75)
    time.sleep(5)
 
    # Motor rückwärts mit 75% Geschwindigkeit
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    pwm.ChangeDutyCycle(75)
    time.sleep(5)
 
    # Motor stoppen
    pwm.ChangeDutyCycle(0)
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
 
finally:
    pwm.stop()
    GPIO.cleanup()