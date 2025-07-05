import time
from LcdDriver import LcdDriver
from ultra_sound_sensor import UltraSoundSensor

if __name__ == "__main__":
    print("Starting main")
    lcdDisplay = LcdDriver()
    ultraSoundSensor = UltraSoundSensor()

    while True:
        distance = ultraSoundSensor.measure_distance()
        print(f"Distance: {distance:.2f} cm")
        lcdDisplay.display_message(f"Dist: {distance:.2f} cm", "Sensor Active")

    lcdDisplay.clear_display()
    print("Ending main")
