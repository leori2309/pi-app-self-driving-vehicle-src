import time
from LcdDriver import LcdDriver


if __name__ == "__main__":
    print("Starting main")
    lcdDisplay = LcdDriver()
    lcdDisplay.display_message(" Rasenballsport ")
    lcdDisplay.display_message("    LEIPZIG     ")
    time.sleep(10)
    lcdDisplay.clear_display()
    print("Ending main")
