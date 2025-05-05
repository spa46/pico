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

wpump = Pin(10, Pin.OUT)
svalve = Pin(12, Pin.OUT)
led_light = Pin(13, Pin.OUT)
fan = Pin(14, Pin.OUT)

# GPIO
wtemp = Pin(2) # DS18B20
dht22 = Pin(3) # dht22
wlevel = Pin(4, Pin.IN) # SEN0204: Sensor-XKC-Y25-T12V
tds = Pin(5, Pin.IN) # SEN0244: 

# sys_led = Pin('LED', Pin.OUT) # Pin 25: System LED

# water_pump = Pin(10, Pin.OUT)
# solenoid_valve = Pin(12, Pin.OUT)


#UART
# co2 = 
# TX:gp16, RX: gp17

# I2C LCD (optional, if using I2C)
# water_level = Pin(4, Pin.IN)
wlevel = SoftI2C(sda=Pin(7), scl=Pin(6), freq=400000)
i2c = SoftI2C(sda=Pin(21), scl=Pin(20), freq=400000)
# temp_hum = SoftI2C(sda=Pin(), scl=Pin(), freq=400000) # Digital Temperature and Humidity Sensor SHT31-F

# ADC
ph = Pin(26)
ec = Pin(27)
mq135 = Pin(28)
