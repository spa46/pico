from ssd1306 import SSD1306_I2C
from config import i2c

oled = SSD1306_I2C(128, 64, i2c)

def update_oled(ph, ec, temp, humidity, water_status, co2):
    oled.fill(0)
    oled.text(f"pH: {ph}", 0, 0)
    oled.text(f"EC: {ec}", 0, 10)
    oled.text(f"T: {temp}C H: {humidity}%", 0, 20)
    oled.text(f"Water: {water_status}", 0, 30)
    oled.text(f"CO2: {co2} ppm", 0, 40)
    oled.show()
