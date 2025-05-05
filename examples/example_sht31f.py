from hal.hal_sht31 import SHT3X
from machine import I2C

class SHT31(SHT3X):

    def __init__(self, bus_obj:I2C):
        self.sensor_name = 'SHT31'
        super().__init__(bus_obj, i2c_addr=68) # 0x44


# class SHT35(SHT3X):

#     def __init__(self, bus_obj:I2C):
#         self.sensor_name = 'SHT35'
#         super().__init__(bus_obj, address=69) # 0x45