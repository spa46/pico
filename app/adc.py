# Author: seansc.park

from hal.hal_mq135 import MQ135
from hal.hal_pinout import mq135
import time


class Mq135:
    def __init__(self) -> None:
        self.mq135 = MQ135(mq135)

    def measure(self, temperature, humidify):
        rzero = self.mq135.get_rzero()
        corrected_rzero = self.mq135.get_corrected_rzero(temperature, humidify)
        resistance = self.mq135.get_resistance()
        ppm = self.mq135.get_ppm()
        corrected_ppm = self.mq135.get_corrected_ppm(temperature, humidity)

        time.sleep(0.3)

