# Author: seansc.park

from machine import Pin
import time

from app.i2c import Lcd
from app.gpio import Dht
from app.adc import Mq135


def initialize():
    lcd = Lcd()
    dht = Dht()
    mq = Mq135()
    
    return lcd, dht, mq
    

def main():
    lcd, dht, mq = initialize()
    # lcd.hello_world()
    # dht.measure()
    # print('hello')
    mq.test() # error


if __name__ == "__main__": 
    main()
