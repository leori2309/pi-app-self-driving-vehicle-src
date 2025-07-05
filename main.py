import time
from LcdDriver import LcdDriver


if __name__ == "__main__":
    print("Starting main")
    lcd = LcdDriver()
    lcd.display_message(" Rasenballsport ")
    lcd.display_message("    LEIPZIG     ")
    time.sleep(10)
    lcd.clear_display()
    print("Ending main")
