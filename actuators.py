from machine import Pin
from config import *

# Initialize Actuators
water_pump = Pin(WATER_PUMP_PIN, Pin.OUT)
solenoid_valve = Pin(SOLENOID_VALVE_PIN, Pin.OUT)
led_grow_lights = Pin(LED_GROW_LIGHTS_PIN, Pin.OUT)
cooling_fan = Pin(COOLING_FAN_PIN, Pin.OUT)

def control_water_pump(water_status):
    if water_status == "LOW":
        water_pump.value(1)  # Turn ON if water is low
    else:
        water_pump.value(0)  # Turn OFF when water is sufficient

def control_nutrients(ph_value):
    if ph_value < 5.5:
        solenoid_valve.value(1)  # Add alkaline solution
    else:
        solenoid_valve.value(0)

def control_lighting(ec_value):
    if ec_value < 500:
        led_grow_lights.value(1)  # Turn ON if nutrients are low
    else:
        led_grow_lights.value(0)

def control_fan(temp):
    if temp > 30:
        cooling_fan.value(1)  # Turn ON if too hot
    else:
        cooling_fan.value(0)
