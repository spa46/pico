# Author: seansc.park

import time
from hal.hal_pinout import i2c0, i2c1
from hal.hal_lcd_i2c import I2cLcd
from hal.hal_sht31 import SHT3X


class Lcd:
    def __init__(self) -> None:
        I2C_ADDR = i2c1.scan()[0]
        self.lcd = I2cLcd(i2c1, I2C_ADDR, 2, 16)
        self.lcd.clear()


    def hello_world(self) -> None:
        self.lcd.putstr("Hello World")
        time.sleep(5)
        self.lcd.clear()
        self.lcd.backlight_off()

class TemperatureHumidity:
    '''
        SHT31
    '''
    def __init__(self) -> None:
        # I2C_ADDR = i2c0.scan()[0]
        I2C_ADDR = 68
        self.sht31 = SHT3X(i2c0, I2C_ADDR) # addr: 0x44

    def measure(self):
        temperature, humidity = self.sht31.get_measurement()
        
        return temperature, humidity
