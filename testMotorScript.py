import RPi.GPIO as GPIO
import time
 
# Pin Definitionen
IN1 = 16  # GPIO23
IN2 = 26  # GPIO24
ENA = 18  # GPIO18 (PWM)
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)
 
pwm = GPIO.PWM(ENA, 1000)  # PWM mit 1kHz
pwm.start(0)
 
try:
    for i in range(10):
        GPIO.output(IN1, GPIO.HIGH)
        GPIO.output(IN2, GPIO.LOW)
        pwm_speed = 80
        # pwm_speed = (i + 1) * 10
        pwm.ChangeDutyCycle(pwm_speed)
        print(f"Motor at {pwm_speed} speed")
        time.sleep(2)
 
    # Motor rückwärts mit 75% Geschwindigkeit
    # GPIO.output(IN1, GPIO.LOW)
    # GPIO.output(IN2, GPIO.HIGH)
    # print("Starting motor backward")
    # pwm.ChangeDutyCycle(100)
    # time.sleep(5)
 
    # Motor stoppen
    pwm.ChangeDutyCycle(0)
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    print("Stopping motor")
 
finally:
    print("Cleaning up GPIO")
    pwm.stop()
    GPIO.cleanup()