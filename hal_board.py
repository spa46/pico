from machine import Pin, ADC, UART, I2C
from config import *

class HAL:
    # Actuator setup
    water_pump = Pin(WATER_PUMP_PIN, Pin.OUT)
    solenoid_valve = Pin(SOLENOID_VALVE_PIN, Pin.OUT)
    led_grow_lights = Pin(LED_GROW_LIGHTS_PIN, Pin.OUT)
    cooling_fan = Pin(COOLING_FAN_PIN, Pin.OUT)

    # Sensor setup
    ph_sensor = ADC(PH_SENSOR_PIN)
    ec_sensor = ADC(EC_SENSOR_PIN)
    water_level = Pin(WATER_LEVEL_PIN, Pin.IN)
    co2_uart = UART(1, baudrate=CO2_BAUDRATE, tx=Pin(CO2_UART_TX), rx=Pin(CO2_UART_RX))

    @staticmethod
    def control_water_pump(state):
        HAL.water_pump.value(1 if state else 0)

    @staticmethod
    def control_solenoid_valve(state):
        HAL.solenoid_valve.value(1 if state else 0)

    @staticmethod
    def control_led_grow_lights(state):
        HAL.led_grow_lights.value(1 if state else 0)

    @staticmethod
    def control_cooling_fan(state):
        HAL.cooling_fan.value(1 if state else 0)

    @staticmethod
    def read_ph():
        raw_value = HAL.ph_sensor.read_u16()
        voltage = raw_value * 3.3 / 65535
        return round(7 + ((voltage - 2.5) / 0.18), 2)

    @staticmethod
    def read_ec():
        raw_value = HAL.ec_sensor.read_u16()
        voltage = raw_value * 3.3 / 65535
        return round(voltage * 1000, 2)

    @staticmethod
    def read_temp_humidity():
        # Implement the logic to read temperature and humidity
        pass  # Replace with actual code

    @staticmethod
    def read_water_level():
        return "LOW" if HAL.water_level.value() == 0 else "HIGH"

    @staticmethod
    def read_co2():
        HAL.co2_uart.write(b'\xFF\x01\x86\x00\x00\x00\x00\x00\x79')
        utime.sleep(0.1)
        data = HAL.co2_uart.read(9)
        return data[2] * 256 + data[3] if data and len(data) == 9 else 0