from machine import SoftI2C, Pin
import utime
from hal.hal_lcd_i2c import I2cLcd

i2c = SoftI2C(sda=Pin(21), scl=Pin(20))
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

menu_items = ["hello Test012345", "hello 2", "Test 3", "hello test4", "haha 5"]
page_size = 2
selected = 0
page_start = 0
direction = 1  # 1 for down, -1 for up

while True:
    lcd.clear()
    for line in range(page_size):
        item_index = page_start + line
        if item_index < len(menu_items):
            prefix = "> " if item_index == selected else "  "
            lcd.move_to(0, line)
            lcd.putstr(prefix + menu_items[item_index][:14])
    utime.sleep(5)
    selected += direction
    # Reverse direction at ends
    if selected >= len(menu_items) - 1:
        selected = len(menu_items) - 1
        direction = -1
    elif selected <= 0:
        selected = 0
        direction = 1
    # Adjust page_start to keep selected visible
    if selected < page_start:
        page_start = selected
    elif selected >= page_start + page_size:
        page_start = selected - page_size + 1