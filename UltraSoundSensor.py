import RPi.GPIO as GPIO
import time

SPEED_OF_SOUND_CM_PER_SEC = 34300

class UltraSoundSensor:

    def __init__(self, pin_trigger: int = 17, pin_echo: int = 27):
        GPIO.setmode(GPIO.BCM)

        self.pin_trigger = pin_trigger 
        self.pin_echo = pin_echo

        GPIO.setup(self.pin_trigger, GPIO.OUT)
        GPIO.setup(self.pin_echo, GPIO.IN)


    def _set_trigger_low(self) -> None:
        GPIO.output(self.pin_trigger, GPIO.LOW)
        time.sleep(0.1)

    
    def _create_trigger_signal(self) -> None:
        GPIO.output(self.pin_trigger, GPIO.HIGH)
        time.sleep(0.00001)  # 10 Mikrosekunden
        GPIO.output(self.pin_trigger, GPIO.LOW)

    def measure_distance(self) -> float:
        self._set_trigger_low()
        self._create_trigger_signal()

        while GPIO.input(self.pin_echo) == GPIO.LOW:
            pass
        pulse_start = time.time()

        while GPIO.input(self.pin_echo) == GPIO.HIGH:
            pass
        pulse_end = time.time()
        
        return (pulse_end - pulse_start) * SPEED_OF_SOUND_CM_PER_SEC / 2
