import utime
from sensors import read_ph, read_ec, read_temp_humidity, read_water_level, read_co2
from actuators import control_water_pump, control_nutrients, control_lighting, control_fan
from display import update_lcd

while True:
    ph = read_ph()
    ec = read_ec()
    temp, humidity = read_temp_humidity()
    water_status = read_water_level()
    co2 = read_co2()

    # Control Actuators
    control_water_pump(water_status)
    control_nutrients(ph)
    control_lighting(ec)
    control_fan(temp)

    # Update LCD Display
    update_lcd(ph, ec, temp, humidity, co2, water_status)

    utime.sleep(5)
