# Author: seansc.park

from machine import Pin
import time

from app.i2c import Lcd
from app.gpio import Dht, WaterTemperature
from app.adc import Mq135
from app.relay import Relay


def initialize_gpio():
    dht = Dht()
    wt = WaterTemperature()

    return dht, wt

def initialize_relay():
    relay = Relay()

def initialize_i2c():
    lcd = Lcd()

    return lcd

def initialize_adc():
    mq = Mq135()

    return mq

def main():
    dht, wt = initialize_gpio()
    lcd = initialize_i2c()
    mq = initialize_adc()

    # lcd.hello_world()
    # dht.measure()
    # print('hello')
    mq.measure(temperature=0, humidity=0) # ToDo: temporary temperature and humidity
    


if __name__ == "__main__": 
    main()
