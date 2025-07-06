import RPi.GPIO as GPIO


class MotorController:

    def __init__(self, in1: int, in2: int, ena: int):
        
        self.GPIO = GPIO
        self.in1 = in1
        self.in2 = in2
        self.ena = ena

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.in1, GPIO.OUT)
        GPIO.setup(self.in2, GPIO.OUT)
        GPIO.setup(self.ena, GPIO.OUT)

        self.pwm = GPIO.PWM(self.ena, 1000) 
        self.pwm.start(0)

    def drive_forward(self, speed: int) -> None:
        GPIO.output(self.in1, GPIO.HIGH)
        GPIO.output(self.in2, GPIO.LOW)
        self.pwm.ChangeDutyCycle(speed)
        print(f"Motor driving forward at {speed}% speed")

    def drive_backward(self, speed: int) -> None:
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.HIGH)
        self.pwm.ChangeDutyCycle(speed)
        print(f"Motor driving backward at {speed}% speed")

    def stop(self) -> None:
        self.pwm.ChangeDutyCycle(0)
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.LOW)
        print("Motor stopped")
