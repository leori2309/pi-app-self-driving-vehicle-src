import sys
sys.path.append('/home/knxpi/I2C-LCD')  # Der Pfad zum I2C-LCD-Verzeichnis
import lcddriver  # Importiere das lcddriver-Modul


class LcdDriver:
    def __init__(self):
        lcd = lcddriver.lcd()

    def display_message(self, message_1, message_2) -> None:
        if message_1 is None:
            message_1 = "Message 1 empty"
        if message_2 is None:
            message_2 = "Message 2 empty"
        lcd.lcd_display_string(message_1, 1)
        lcd.lcd_display_string(message_2, 2)

    def clear_display(self) -> None:
        lcd.lcd_clear()
