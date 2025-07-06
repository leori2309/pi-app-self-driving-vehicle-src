import RPi.GPIO as GPIO
from DatabaseLogger import DatabaseLogger
from datetime import datetime
import time

SPEED_OF_SOUND_MM_PER_SEC = 343000


class UltraSoundSensor:

    def __init__(self, name: str, pin_trigger: int = 17, pin_echo: int = 27):
        
        self.name: str = name
        self.pin_trigger: int = pin_trigger 
        self.pin_echo: int = pin_echo
        self.database_logger = DatabaseLogger()

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin_trigger, GPIO.OUT)
        GPIO.setup(self.pin_echo, GPIO.IN)

        self._cache = []


    def _set_trigger_low(self) -> None:
        GPIO.output(self.pin_trigger, GPIO.LOW)
        time.sleep(0.1)

    
    def _create_trigger_signal(self) -> None:
        GPIO.output(self.pin_trigger, GPIO.HIGH)
        time.sleep(0.00001)  # 10 Mikrosekunden
        GPIO.output(self.pin_trigger, GPIO.LOW)

    
    def _get_rolling_average(self) -> float:
        if len(self._cache) < 5:
            return round(sum(self._cache) / len(self._cache), 0)
        return round(sum(self._cache[-5:]) / 5, 0)


    def _log_distance(self, distance_mm: float, timestamp: time.time) -> None:
        self.database_logger.log_ultrasound_data(self.name, distance_mm, timestamp)
        

    def measure_distance(self, use_rolling_average: bool) -> float:
        self._set_trigger_low()
        self._create_trigger_signal()

        while GPIO.input(self.pin_echo) == GPIO.LOW:
            pass
        pulse_start = datetime.now()

        while GPIO.input(self.pin_echo) == GPIO.HIGH:
            pass
        pulse_end = datetime.now()

        time_diff = (pulse_end - pulse_start).total_seconds()
        distance_mm = round(time_diff * SPEED_OF_SOUND_MM_PER_SEC / 2, 0)
        self._cache.append(distance_mm)
        self._log_distance(distance_mm, pulse_end)

        return distance_mm, self._get_rolling_average()
