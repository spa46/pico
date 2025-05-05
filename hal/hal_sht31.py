from ubinascii import hexlify
from time import sleep
from machine import I2C


class SHT3X:
    def __init__(self, i2c, i2c_addr):
        self.i2c_addr = i2c_addr
        self.i2c = i2c

    def get_temperature_in_celsius(self, data:int) -> float:
        #   Temperature conversion formula (Celsius)
        #   T[C] = -45 + (175 * (raw_temp_data / (2^16 - 1)))
        return round(-45 + (175 * (data / ((2**16) - 1))), 2)    

    def get_temperature_in_fahrenheit(self, data:int) -> float:
        #   Temperature conversion formula (Fahrenheit)
        #   T[F] = -49 + (315 * (raw_temp_data / (2^16 - 1)))
        return round(-49 + (315 * (data / ((2**16) - 1))), 2)

    def get_relative_humidity(self, data:int) -> float:
        #   Relative humidity conversion formula
        #   RH = 100 * (raw_humidity_data / (2^16 - 1))
        return round(100 * (data/ ((2**16) - 1)), 2)

    def get_measurement(self):

        try:
            sleep(0.05)
            self.i2c.writeto(self.i2c_addr, b'\x2c\x06')
            sleep(0.05)
            data = hexlify(self.i2c.readfrom(self.i2c_addr, 6))
            temp_data = int(data[0:4], 16)
            humi_data = int(data[6:10], 16)
            sleep(0.05)

            temperature = self.get_temperature_in_celsius(temp_data)
            humidity = self.get_relative_humidity(humi_data)
            
            return temperature, humidity
            
        
        except Exception as e:
            print("Failed to read temperature and humidity value")
            print(e)

            return None, None