import time
from LcdDriver import LcdDriver
from UltraSoundSensor import UltraSoundSensor
from DatabaseLogger import DatabaseLogger

if __name__ == "__main__":
    databaseLogger = DatabaseLogger()
    databaseLogger._create_tables()

    lcdDisplay = LcdDriver()

    ultraSoundSensor1 = UltraSoundSensor(
        name="UltrasoundSensor1",
        pin_trigger = 17, 
        pin_echo = 27
    )

    while True:
        distance_mm, rolling_average_distance_mm = ultraSoundSensor1.measure_distance(use_rolling_average=True)
        lcdDisplay.display_message(f"mm: {distance_mm}", f"ra: {rolling_average_distance_mm}")
        time.sleep(2)

    lcdDisplay.clear_display()
    print("Ending main")
