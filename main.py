import machine
import utime
import dht
from machine import Pin, ADC, PWM, I2C
from ssd1306 import SSD1306_I2C  # OLED Display

# Analog Sensors
ph_sensor = ADC(26)  # pH Sensor on ADC0
ec_sensor = ADC(27)  # EC Sensor on ADC1

# Digital Sensors
dht22 = dht.DHT22(Pin(3))  # DHT22 on GP3
water_level = Pin(4, Pin.IN)  # Water level sensor on GP4

# I2C (BH1750, OLED)
i2c = I2C(0, scl=Pin(21), sda=Pin(20), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

# CO2 Sensor (MH-Z19B) UART
co2_uart = machine.UART(1, baudrate=9600, tx=Pin(8), rx=Pin(9))

# Relays for actuators
water_pump = Pin(10, Pin.OUT)
air_pump = Pin(11, Pin.OUT)
solenoid_valve = Pin(12, Pin.OUT)
led_grow_lights = Pin(13, Pin.OUT)
cooling_fan = Pin(14, Pin.OUT)

# Buzzer for alerts
buzzer = PWM(Pin(15))


def read_ph():
    raw_value = ph_sensor.read_u16()
    voltage = raw_value * 3.3 / 65535
    ph_value = 7 + ((voltage - 2.5) / 0.18)  # Example calibration
    return round(ph_value, 2)

def read_ec():
    raw_value = ec_sensor.read_u16()
    voltage = raw_value * 3.3 / 65535
    ec_value = voltage * 100  # Example conversion factor
    return round(ec_value, 2)

def read_temp_humidity():
    dht22.measure()
    return dht22.temperature(), dht22.humidity()

def read_water_level():
    return "HIGH" if water_level.value() else "LOW"

def read_co2():
    co2_uart.write(b'\xFF\x01\x86\x00\x00\x00\x00\x00\x79')  # Request CO2 value
    utime.sleep(0.1)
    if co2_uart.any():
        response = co2_uart.read(9)
        if response and len(response) == 9:
            co2_value = response[2] * 256 + response[3]
            return co2_value
    return None


def update_oled():
    oled.fill(0)
    oled.text(f"pH: {read_ph()}", 0, 0)
    oled.text(f"EC: {read_ec()}", 0, 10)
    temp, hum = read_temp_humidity()
    oled.text(f"T: {temp}C H: {hum}%", 0, 20)
    oled.text(f"Water: {read_water_level()}", 0, 30)
    oled.text(f"CO2: {read_co2()} ppm", 0, 40)
    oled.show()


def control_system():
    ph = read_ph()
    ec = read_ec()
    water_status = read_water_level()
    
    # Adjust water pump based on water level
    water_pump.value(1 if water_status == "LOW" else 0)

    # Adjust solenoid valve based on pH
    if ph < 5.5:
        solenoid_valve.value(1)  # Add base
    elif ph > 7.5:
        solenoid_valve.value(0)  # Stop

    # Turn on grow lights if EC is too low (suggesting nutrient deficiency)
    led_grow_lights.value(1 if ec < 1.0 else 0)

    # Turn on cooling fan if temperature exceeds 30°C
    temp, _ = read_temp_humidity()
    cooling_fan.value(1 if temp > 30 else 0)
    
    # Buzzer alert if CO2 is too low (<400ppm)
    if read_co2() < 400:
        buzzer.duty_u16(30000)  # Sound buzzer
        utime.sleep(1)
        buzzer.duty_u16(0)  # Stop buzzer


while True:
    update_oled()
    control_system()
    utime.sleep(5)  # Wait for 5 seconds before the next reading
