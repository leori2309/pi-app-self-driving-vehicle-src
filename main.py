import sys
sys.path.append('/home/knxpi/I2C-LCD')  # Der Pfad zum I2C-LCD-Verzeichnis

import lcddriver  # Importiere das lcddriver-Modul
import time

# Initialisiere das LCD
lcd = lcddriver.lcd()

# Zeige "Hello World" auf dem LCD an
print('Checkpoint1')
lcd.lcd_display_string("Hello World", 1)  # Zeigt auf der ersten Zeile des LCD an
lcd.lcd_display_string("OK", 2)

# Warte eine Sekunde
print('Checkpoint2')
time.sleep(5)

# Zeige "Raspberry Pi" auf der zweiten Zeile an
print('Checkpoint3')
lcd.lcd_display_string("Raspberry Pi", 2)  # Zeigt auf der zweiten Zeile des LCD an
print('Checkpoint4')
# Warte eine weitere Sekunde
time.sleep(5)

# Lösche das Display
lcd.lcd_clear()
