from machine import Pin
from machine import SoftI2C

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
dht22 = Pin(3)
# water_level = Pin(4, Pin.IN)
# sys_led = Pin('LED', Pin.OUT) # Pin 25: System LED

# water_pump = Pin(10, Pin.OUT)
# solenoid_valve = Pin(12, Pin.OUT)


#UART
# co2 = 
# TX:gp16, RX: gp17

# I2C LCD (optional, if using I2C)
i2c = SoftI2C(sda=Pin(21), scl=Pin(20), freq=400000)


# temp
mq135 = Pin(28)