import random

class HAL:
    # Actuator setup
    water_pump = -1
    solenoid_valve = -1
    led_grow_lights = False
    cooling_fan = False

    # Sensor values (simulated)
    ph_sensor = 7.0  # Simulate a neutral pH
    ec_sensor = 1000  # Simulate a normal EC value
    water_level = True  # Simulate sufficient water level (True for enough water)
    co2_uart = "400 ppm"  # Simulate a CO2 reading

    @staticmethod
    def control_water_pump(state):
        if state:
            HAL.water_pump= 1  # Turn ON the water pump
        else:
            HAL.water_pump= 0# Turn OFF the water pump

    @staticmethod
    def control_solenoid_valve(state):
        if state:
            HAL.solenoid_valve = 1  # Turn ON the solenoid valve
        else:
            HAL.solenoid_valve = 0  # Turn OFF the solenoid valve

    @staticmethod
    def control_led_grow_lights(state):
        if state:
            HAL.led_grow_lights = 1  # Turn ON the LED grow lights
        else:
            HAL.led_grow_lights = 0  # Turn OFF the LED grow lights

    @staticmethod
    def control_cooling_fan(state):
        if state:
            HAL.cooling_fan = 1  # Turn ON the cooling fan
        else:
            HAL.cooling_fan = 0  # Turn OFF the cooling fan

    @staticmethod
    def read_ph():
        return round(random.uniform(5.5, 7.5), 2)

    @staticmethod
    def read_ec():
        return round(random.uniform(400, 600), 2)

    @staticmethod
    def read_temp_humidity():
        # Mock temperature and humidity for the emulator
        temp = random.uniform(18, 30)  # Mock temperature range
        humidity = random.uniform(40, 60)  # Mock humidity range
        return temp, humidity

    @staticmethod
    def read_water_level():
        return random.choice(["LOW", "HIGH"])

    @staticmethod
    def read_co2():
        return random.randint(300, 500)
