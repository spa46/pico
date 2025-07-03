# Author: seansc.park

from machine import Pin
import time

from api.i2c import Lcd
from api.gpio import Dht, WaterTemperature
from api.adc import Mq135
from api.relay import Relay
from api.menu_items import menu_items
from api.menu import MenuNavigator

from hal.hal_rotary_encoder import RotaryEncoder


def init_dht():
    return Dht()



def init_water_temperature():
    return WaterTemperature()

    return dht, wt

def init_relay():
    return Relay()


def init_lcd():
    return Lcd()


def init_mq135():
    return Mq135()

def init_rotary_encoder():
    return RotaryEncoder()

def main():
    # Initilization
    dht = init_dht()
    water_temperature = init_water_temperature()
    lcd = init_lcd()

    m_ctrl = init_rotary_encoder()

    mq = init_mq135()

    navigator = MenuNavigator(lcd, menu_items)
    navigator.run()

    # lcd.hello_world()
    # dht.measure()
    # print('hello')
    mq.measure(temperature=0, humidity=0) # ToDo: temporary temperature and humidity
    




if __name__ == "__main__": 
    main()
