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
    _dht = Dht()
    print('Temp & Humidity Sensor initialized')
    return _dht



def init_water_temperature():
    wt = WaterTemperature()
    print('Water temperature sensor initialized')
    return wt

def init_relay():
    relay = Relay()
    print('Relay initialized')
    return relay


def init_lcd():
    lcd = Lcd()
    print('LCD initialized')
    return lcd


def init_mq135():
    mq = Mq135()
    print('MQ135 sensor initialized')
    return mq

def init_rotary_encoder():
    encoder = RotaryEncoder()
    print('Rotary encoder initialized')
    return encoder


def main():
    # Initilization
    dht = init_dht()
    water_temperature = init_water_temperature()
    lcd = init_lcd()

    m_ctrl = init_rotary_encoder()

    mq = init_mq135()

    menu = MenuNavigator(lcd, menu_items)
    menu.display()

    # mq.measure(temperature=0, humidity=0) # ToDo: temporary temperature and humidity

    # while True:
    #     menu.display()
        # utime.sleep(0.1)

    def handle_rotary_event(event_type, value):
        if event_type == 'rotate':
            if value == 1:
                menu.display(move=1)  # Right
            elif value == -1:
                menu.display(move=-1)  # Left
        elif event_type == 'short_press':
            menu.enter()
        elif event_type == 'long_press':
            menu.back()


    m_ctrl.on_event = handle_rotary_event


if __name__ == "__main__":
    main()
