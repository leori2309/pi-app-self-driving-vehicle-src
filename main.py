import time
from LcdDriver import LcdDriver


if __name__ == "__main__":
    print("Starting main")
    lcdDisplay = LcdDriver()
    lcdDisplay.display_mooving_message("Ein Schuss - Ein Tor - Für Leipzig")
    lcdDisplay.clear_display()
    print("Ending main")
