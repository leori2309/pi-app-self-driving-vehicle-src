import time
from LcdDriver import LcdDriver
from ultra_sound_sensor import UltraSoundSensor

if __name__ == "__main__":
    print("Starting main")
    lcdDisplay = LcdDriver()
    ultraSoundSensor = UltraSoundSensor()

    i = 0
    while i < 10:
        distance = ultraSoundSensor.measure_distance()
        print(f"Distance: {distance:.2f} cm")
        lcdDisplay.display_message(f"Dist: {distance:.2f} cm", "Sensor Active")
        time.sleep(1)
        i += 1

    lcdDisplay.clear_display()
    print("Ending main")
