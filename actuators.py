from hal import HAL

hal_instance = HAL()

def control_water_pump(water_status):
    hal_instance.control_water_pump(water_status == "LOW")

def control_nutrients(ph_value):
    hal_instance.control_solenoid_valve(ph_value < 5.5)

def control_lighting(ec_value):
    hal_instance.control_led_grow_lights(ec_value < 500)

def control_fan(temp):
    hal_instance.control_cooling_fan(temp > 30)