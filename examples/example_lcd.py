# Author: seansc.park

from machine import SoftI2C, Pin
import utime
from hal.hal_lcd_i2c import I2cLcd

i2c = SoftI2C(sda=Pin(21), scl=Pin(20))
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)
lcd.clear()

lcd.putstr("hello PICO!")
utime.sleep(5)
lcd.clear()
lcd.backlight_off()