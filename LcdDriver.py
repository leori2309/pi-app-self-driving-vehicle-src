import sys
sys.path.append('/home/knxpi/I2C-LCD')  # Der Pfad zum I2C-LCD-Verzeichnis
import lcddriver  # Importiere das lcddriver-Modul
import time


class LcdDriver:
    def __init__(self):
        self.lcd = lcddriver.lcd()

    def display_message(self, message_1, message_2) -> None:
        if message_1 is None:
            message_1 = "Msg 1 empty"
        if message_2 is None:
            message_2 = "Msg 2 empty"
        if len(message_1) > 16:
            message_1 = "Msg 1 too long"
        if len(message_2) > 16:
            message_2 = "Msg 2 too long"

        self.lcd.lcd_display_string(message_1, 1)
        self.lcd.lcd_display_string(message_2, 2)


    def display_mooving_message(self, message: str) -> None:
        message = f"                {message}                "
        for i in range(len(message) - 16):
            self.lcd.lcd_display_string(message[i:i + 16], 1)
            time.sleep(0.25)


    def clear_display(self) -> None:
        self.lcd.lcd_clear()
