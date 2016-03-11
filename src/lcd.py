import lcddriver
from time import *

lcd = lcddriver.lcd()

while True:
        lcd.backlightOn()
	lcd.lcd_display_string("Hello world", 1)
	lcd.lcd_display_string("My name is", 2)
	sleep(3)
        lcd.backlightOff()
        sleep(2)
        lcd.backlightOn()
        sleep(2)
        lcd.backlightOff()
        sleep(2)
	lcd.lcd_display_string("All glory to", 1)
	lcd.lcd_display_string("Hyptnotoad", 2)
	sleep(3)
#lcd.lcd_display_string("picorder", 3)
#lcd.lcd_display_string("I am a Raspberry Pi", 4)