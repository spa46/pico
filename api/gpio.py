# Author: seansc.park

# from hal.hal_pinout import sys_led
from time import sleep
from hal.hal_pinout import gpio2, gpio3, gpio4
import dht
import onewire, ds18x20

class Led:
    def __init__(self) -> None:
        pass
    
    def system_led_on(self) -> None:
        pass
    
    def system_led_off(self) -> None:
        pass
    
    
class Dht:
    def __init__(self) -> None:
        self.sensor = dht.DHT22(gpio3)

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


class WaterTemperature:
    '''
    DS18B20 Sensor
    '''
    def __init__(self) -> None:
        self.sensor = ds18x20.DS18X20(onewire.OneWire(gpio2))
        self.roms = self.sensor.scan()

        print('Found DS devices: ', self.roms)

    def measure(self) -> None:
        self.sensor.convert_temp()

        sleep(0.75)

        for rom in self.roms:
            print(rom)
            
            print(self.sensor.read_temp(rom))


class InContactWaterLevel:
    def __init__(self) -> None:
        self.sensor = gpio4
    
    def measure(self):
        self.sensor.value()