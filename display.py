from machine import I2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from config import *

i2c = I2C(0, scl=Pin(I2C_SCL), sda=Pin(I2C_SDA), freq=400000)
lcd = I2cLcd(i2c, 0x27, 2, 16)  # 16x2 LCD

def update_lcd(ph, ec, temp, humidity, co2, water_status):
    lcd.clear()
    lcd.move_to(0, 0)
    lcd.putstr(f"pH:{ph} EC:{ec}")
    lcd.move_to(0, 1)
    lcd.putstr(f"T:{temp}C H:{humidity}%")
