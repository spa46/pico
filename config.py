from machine import Pin, ADC, I2C, UART

# Analog Sensors
PH_SENSOR_PIN = 26  # Industrial pH Sensor
EC_SENSOR_PIN = 27  # EC Sensor

# Digital Sensors
DHT_PIN = 3  # DHT22 (Temp & Humidity)
WATER_LEVEL_PIN = 4  # Water Level Sensor

# CO2 Sensor (MH-Z19B via UART)
CO2_UART_TX = 16
CO2_UART_RX = 17
CO2_BAUDRATE = 9600

# I2C for LCD Display
I2C_SDA = 20
I2C_SCL = 21

# Actuators (Relays & MOSFET)
WATER_PUMP_PIN = 10
SOLENOID_VALVE_PIN = 12
LED_GROW_LIGHTS_PIN = 13
COOLING_FAN_PIN = 14
