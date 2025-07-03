from machine import Pin
from machine import SoftI2C

# wpump = 
# svalve = Pin(11, Pin.OUT)
# led_light = Pin(12, Pin.OUT)
# fan = Pin(13, Pin.OUT)

# GPIO
tds = Pin(5, Pin.IN) # SEN0244:  ADC?

pin_2 = Pin(2)
pin_3 = Pin(3)
pin_4 = Pin(4, Pin.IN)
# pin_5 = Pin(5, Pin.IN)
pin_6 = Pin(6)
pin_7 = Pin(7)

pin_10 = Pin(10, Pin.OUT)
pin_11 = Pin(11, Pin.OUT)
pin_12 = Pin(12, Pin.OUT)
pin_13 = Pin(13, Pin.OUT)

pin_16 = Pin(16, Pin.IN, Pin.PULL_UP)
pin_17 = Pin(17, Pin.IN, Pin.PULL_UP)
pin_18 = Pin(18, Pin.IN, Pin.PULL_UP)

pin_20 = Pin(20)
pin_21 = Pin(21)

pin_26 = Pin(26)
pin_27 = Pin(27)
pin_28 = Pin(28)


# GPIO
gpio2 = pin_2 # DS18B20
gpio3 = pin_3 # DHT22
gpio4 = pin_4 # ToDo: SEN0204: incontact water level sensor Sensor-XKC-Y25-T12V
# gpio5 = pin_5 # ToDo: SEN0244: 

# RELAY
relay0 = pin_10 # Water Pump
relay1 = pin_11 # Solenoid Valve
relay2 = pin_12 # LED Light
relay3 = pin_13 # FAN

# Rotary Encoder
gpio16 = pin_16  # s1
gpio17 = pin_17  # s2
gpio18 = pin_18  # key

# I2C LCD (optional, if using I2C)
i2c0 = SoftI2C(sda=pin_7, scl=pin_6, freq=400000) # ToDo: SHT31-F: Digital Temperature and Humidity Sensor [SEN0334]
i2c1 = SoftI2C(sda=pin_21, scl=pin_20, freq=400000) # D44780 character LCD connected via PCF8574 on I2C

# ADC
adc0 = pin_26 # PH
adc1 = pin_27 # EC
adc2 = pin_28 # MQ135
