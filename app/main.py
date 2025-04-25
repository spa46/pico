# Author: seansc.park

from machine import Pin
import utime
from hal.hal_lcd_i2c import I2cLcd
from app.lcd import Lcd

def initialize():
    lcd = Lcd()
    

def main():
    pass

if __name__ == "__main__": 
    initialize()
    main()