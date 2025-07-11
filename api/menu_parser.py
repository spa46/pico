def parse_menu_enter(lcd, item):
    label = item["label"] if isinstance(item, dict) and "label" in item else str(item)
    if label == "Temp & Humidity":
        lcd.clear()
        lcd.move_to(0, 0)
        lcd.putstr("Temp: ")
        lcd.move_to(0, 1)
        lcd.putstr("Hum:")
        return True
    # Add more menu label handling as needed
    return False

