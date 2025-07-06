import time
from LcdDriver import LcdDriver
from UltraSoundSensor import UltraSoundSensor
from DatabaseLogger import DatabaseLogger
from MotorController import MotorController

if __name__ == "__main__":
    databaseLogger = DatabaseLogger()
    databaseLogger._create_tables()

    lcdDisplay = LcdDriver()

    ultraSoundSensor1 = UltraSoundSensor(
        name="UltrasoundSensor1",
        pin_trigger = 17, 
        pin_echo = 27
    )

    motorController = MotorController(
        in1=16,  # GPIO23
        in2=26,  # GPIO24
        ena=18   # GPIO18 (PWM)
    )

    motorController.stop()

    while True:

        distance_mm = ultraSoundSensor1.measure_distance()
        if distance_mm <= 200:
            motorController.drive_backward(speed=100)
        else:
            motorController.drive_forward(speed=100)
            time.sleep(3)
        
        lcdDisplay.display_message(f"mm: {distance_mm}", "")

    lcdDisplay.clear_display()
    print("Ending main")
