import utime
import dht
import machine
from config import *

# Initialize Sensors
ph_sensor = ADC(PH_SENSOR_PIN)
ec_sensor = ADC(EC_SENSOR_PIN)
dht22 = dht.DHT22(Pin(DHT_PIN))
water_level = Pin(WATER_LEVEL_PIN, Pin.IN)

# CO2 Sensor (MH-Z19B) via UART
co2_uart = machine.UART(1, baudrate=CO2_BAUDRATE, tx=Pin(CO2_UART_TX), rx=Pin(CO2_UART_RX))

def read_ph():
    raw_value = ph_sensor.read_u16()
    voltage = raw_value * 3.3 / 65535
    ph_value = 7 + ((voltage - 2.5) / 0.18)  # Adjust based on calibration
    return round(ph_value, 2)

def read_ec():
    raw_value = ec_sensor.read_u16()
    voltage = raw_value * 3.3 / 65535
    ec_value = voltage * 1000  # Example conversion, adjust as needed
    return round(ec_value, 2)

def read_temp_humidity():
    dht22.measure()
    return dht22.temperature(), dht22.humidity()

def read_water_level():
    return "LOW" if water_level.value() == 0 else "HIGH"

def read_co2():
    co2_uart.write(b'\xFF\x01\x86\x00\x00\x00\x00\x00\x79')  # MH-Z19B request
    utime.sleep(0.1)
    data = co2_uart.read(9)
    if data and len(data) == 9:
        co2_value = data[2] * 256 + data[3]
        return co2_value
    return 0
