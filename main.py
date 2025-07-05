import sys
sys.path.append('/home/knxpi/I2C-LCD')  # Der Pfad zum I2C-LCD-Verzeichnis

import lcddriver  # Importiere das lcddriver-Modul

# Initialisiere das LCD
lcd = lcddriver.lcd()

# Zeige "Hello World" auf dem LCD an
lcd.lcd_display_string("Hello World", 1)  # Zeigt auf der ersten Zeile des LCD an

# Warte eine Sekunde
import time
time.sleep(1)

# Zeige "Raspberry Pi" auf der zweiten Zeile an
lcd.lcd_display_string("Raspberry Pi", 2)  # Zeigt auf der zweiten Zeile des LCD an

# Warte eine weitere Sekunde
time.sleep(10)

# Lösche das Display
lcd.lcd_clear()