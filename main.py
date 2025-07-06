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
        distance = ultraSoundSensor1.measure_distance(use_rolling_average=True)
        lcdDisplay.display_message(f"Dist: {distance:.2f} cm", "Sensor Active")
        time.sleep(2)

    lcdDisplay.clear_display()
    print("Ending main")
