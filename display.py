from hal import HAL  # Import HAL to interact with sensors/actuators

def update_lcd():
    # Read sensor values using HAL class methods
    ph = HAL.read_ph()
    ec = HAL.read_ec()
    temp, humidity = HAL.read_temp_humidity()  # Assuming you also refactor `read_temp_humidity` in HAL
    water_status = HAL.read_water_level()
    co2 = HAL.read_co2()

    # Update LCD with the latest values
    # lcd.clear()
    # lcd.move_to(0, 0)
    # lcd.putstr(f"pH:{ph} EC:{ec}")
    # lcd.move_to(0, 1)
    # lcd.putstr(f"T:{temp}C H:{humidity}%")
