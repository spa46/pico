from machine import Pin

# Button definitions
# BUTTON_UP = Pin(2, Pin.IN, Pin.PULL_UP)
# BUTTON_DOWN = Pin(3, Pin.IN, Pin.PULL_UP)
# BUTTON_LEFT = Pin(4, Pin.IN, Pin.PULL_UP)
# BUTTON_RIGHT = Pin(5, Pin.IN, Pin.PULL_UP)

# # LCD pins (if you're bit-banging or using GPIO directly)
# LCD_RS = Pin(6, Pin.OUT)
# LCD_E = Pin(7, Pin.OUT)
# LCD_D4 = Pin(8, Pin.OUT)
# LCD_D5 = Pin(9, Pin.OUT)
# LCD_D6 = Pin(10, Pin.OUT)
# LCD_D7 = Pin(11, Pin.OUT)

# GPIO
dht22 = Pin(3, Pin.IN)
water_level = Pin(4, Pin.IN)
sys_led = Pin('LED', Pin.OUT) # Pin 25: System LED

# I2C LCD (optional, if using I2C)
from machine import I2C
i2c = I2C(0, scl=Pin(27), sda=Pin(26), freq=400_000)
