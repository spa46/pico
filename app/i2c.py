# Author: seansc.park

from machine import I2C, Pin
import utime
from hal.hal_pinout import i2c
from hal.hal_lcd_i2c import I2cLcd


class Lcd:
    def __init__(self) -> None:
        I2C_ADDR = i2c.scan()[0]
        lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)
        lcd.clear()


    def func() -> None:
        lcd.putstr("hello PICO!")
        utime.sleep(5)
        lcd.clear()
        lcd.backlight_off()
