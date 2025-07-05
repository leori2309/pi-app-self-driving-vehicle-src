# lcd_display.py
import sys
sys.path.append('/I2C-LCD')
import lcddriver

#import I2C_LCD_driver
from time import sleep

mylcd = lcddriver.lcd()

def display_hello_world():
    while True:
        mylcd.lcd_display_string("Hello, World!!!!", 1)
        mylcd.lcd_display_string("RPi + LCD", 2)

        sleep(1)
        mylcd.lcd_clear()
        sleep(1)

if __name__ == "__main__":
    print("Start Script")
    display_hello_world()
