import time
from LcdDriver import LcdDriver


if __name__ == "__main__":
    print("Starting main")
    lcdDisplay = LcdDriver()
    lcdDisplay.display_message(
        " Rasenballsport ",
        "    LEIPZIG     ")
    time.sleep(10)
    lcdDisplay.clear_display()
    print("Ending main")
