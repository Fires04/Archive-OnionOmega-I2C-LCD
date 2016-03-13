import lcddriver
from time import *

lcd = lcddriver.lcd(0x27)

lcd.backlightOn()
lcd.lcd_display_string("I2C LCD ONION.IO", 1)
lcd.lcd_display_string(" -davidstein.cz-", 2)
sleep(1)
lcd.backlightOff()
sleep(1)
lcd.backlightOn()