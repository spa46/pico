# Author: seansc.park

import utime
from hal.hal_pinout import i2c
from hal.hal_lcd_i2c import I2cLcd


class Lcd:
    def __init__(self) -> None:
        I2C_ADDR = i2c.scan()[0]
        self.lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)
        self.lcd.clear()


    def hello_world(self) -> None:
        self.lcd.putstr("Hello World")
        utime.sleep(5)
        self.lcd.clear()
        self.lcd.backlight_off()
