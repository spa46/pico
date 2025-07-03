python
class MenuNavigator:
    def __init__(self, lcd, menu_items, page_size=2, delay=5, sleep_fn=None):
        self.lcd = lcd
        self.menu_items = menu_items
        self.page_size = page_size
        self.selected = 0
        self.page_start = 0
        self.direction = 1
        self.delay = delay
        self.sleep_fn = sleep_fn if sleep_fn else self.default_sleep

    def default_sleep(self, seconds):
        import time
        time.sleep(seconds)

    def display(self):
        self.lcd.clear()
        for line in range(self.page_size):
            item_index = self.page_start + line
            if item_index < len(self.menu_items):
                prefix = "> " if item_index == self.selected else "  "
                self.lcd.move_to(0, line)
                self.lcd.putstr(prefix + self.menu_items[item_index][:14])

    def update(self):
        self.selected += self.direction
        if self.selected >= len(self.menu_items) - 1:
            self.selected = len(self.menu_items) - 1
            self.direction = -1
        elif self.selected <= 0:
            self.selected = 0
            self.direction = 1
        if self.selected < self.page_start:
            self.page_start = self.selected
        elif self.selected >= self.page_start + self.page_size:
            self.page_start = self.selected - self.page_size + 1

    def run(self):
        while True:
            self.display()
            self.sleep_fn(self.delay)
            self.update()

# Usage example (replace with your actual LCD and menu items)
# from machine import SoftI2C, Pin
# import utime
# from hal.hal_lcd_i2c import I2cLcd
# i2c = SoftI2C(sda=Pin(21), scl=Pin(20))
# I2C_ADDR = i2c.scan()[0]
# lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)
# menu_items = ["hello 1", "hello 2", "Test 3", "hello test4", "haha 5"]
# navigator = MenuNavigator(lcd, menu_items)
# navigator.run()