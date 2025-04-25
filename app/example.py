# Author: seansc.park

from machine import I2C, Pin
import utime
from hal.hal_lcd_i2c import I2cLcd

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)
lcd.clear()

lcd.putstr("hello PICO!")
utime.sleep(5)
lcd.clear()
lcd.backlight_off()