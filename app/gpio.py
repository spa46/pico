# Author: seansc.park

from hal.hal_pinout import sys_led
from time import sleep

class Led:
  def __init__(self) -> None:
    sys = sys_led

  def system_led_on(self) -> None:
    pass

  def system_led_off(self) -> None:
    pass