import time
from LcdDriver import LcdDriver
from UltraSoundSensor import UltraSoundSensor

if __name__ == "__main__":
    print("Starting main")
    lcdDisplay = LcdDriver()
    ultraSoundSensor = UltraSoundSensor()

    while True:
        distance = ultraSoundSensor.measure_distance(use_rolling_average=True)
        print(f"Distance: {distance:.2f} cm")
        lcdDisplay.display_message(f"Dist: {distance:.2f} cm", "Sensor Active")
        time.sleep(2)

    lcdDisplay.clear_display()
    print("Ending main")
