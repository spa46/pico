# Author: seansc.park

from machine import Pin
import utime

from app.i2c import Lcd
from app.gpio import Dht


def initialize():
    lcd = Lcd()
    dht = Dht()
    return lcd, dht
    

def main():
    lcd, dht = initialize()
    lcd.hello_world()
    dht.measure()


if __name__ == "__main__": 
    main()
