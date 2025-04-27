# Author: seansc.park

# from hal.hal_pinout import sys_led
from time import sleep
from hal.hal_pinout import dht22
import dht

class Led:
  def __init__(self) -> None:
    pass
    # sys = sys_led

  def system_led_on(self) -> None:
    pass

  def system_led_off(self) -> None:
    pass

class Dht:
    def __init__(self) -> None:
        self.sensor = dht.DHT22(dht22)
    
    def measure(self) -> None:
        try:
            self.sensor.measure()
            self.temperature()
            self.humidity()
        except OSError as e:
            print('Failed to read sensor.')
    
    def temperature(self) -> None:
        t = self.sensor.temperature()
        print(t)

    def humidity(self) -> None:
        h = self.sensor.humidity()
        print(h)
