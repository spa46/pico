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
svalve = Pin(11, Pin.OUT)
led_light = Pin(12, Pin.OUT)
fan = Pin(13, Pin.OUT)

# GPIO

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
pin_2 = Pin(2)
pin_3 = Pin(3)
pin_6 = Pin(6)
pin_7 = Pin(7)

pin_20 = Pin(20)
pin_21 = Pin(21)

pin_28 = Pin(28)

# temp_hum = SoftI2C(sda=Pin(), scl=Pin(), freq=400000) #  SHT31-F

# ADC
ph = Pin(26)
ec = Pin(27)


gpio2 = pin_2 # DS18B20
gpio3 = pin_3 # DHT22
i2c0 = SoftI2C(sda=pin_7, scl=pin_6, freq=400000) # SHT31-F: Digital Temperature and Humidity Sensor [SEN0334]
i2c1 = SoftI2C(sda=pin_21, scl=pin_20, freq=400000) # D44780 character LCD connected via PCF8574 on I2C
adc2 = pin_28 # MQ135
