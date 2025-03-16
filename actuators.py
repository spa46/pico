import utime
from machine import Pin, PWM
from config import *

# 액추에이터 초기화
water_pump = Pin(WATER_PUMP_PIN, Pin.OUT)
air_pump = Pin(AIR_PUMP_PIN, Pin.OUT)
solenoid_valve = Pin(SOLENOID_VALVE_PIN, Pin.OUT)
led_grow_lights = Pin(LED_GROW_LIGHTS_PIN, Pin.OUT)
cooling_fan = Pin(COOLING_FAN_PIN, Pin.OUT)
buzzer = PWM(Pin(BUZZER_PIN))

def control_water_pump(status):
    water_pump.value(1 if status == "LOW" else 0)

def control_nutrients(ph_value):
    if ph_value < 5.5:
        solenoid_valve.value(1)  # 염기 추가
    elif ph_value > 7.5:
        solenoid_valve.value(0)  # 중지

def control_lighting(ec_value):
    led_grow_lights.value(1 if ec_value < 1.0 else 0)

def control_fan(temp):
    cooling_fan.value(1 if temp > 30 else 0)

def alert_buzzer(co2_level):
    if co2_level and co2_level < 400:
        buzzer.duty_u16(30000)
        utime.sleep(1)
        buzzer.duty_u16(0)
