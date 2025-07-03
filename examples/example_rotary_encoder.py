# examples/example_rotary_encoder_new.py
import machine
import utime

# Pin assignments (change as needed)
PIN_A = 16
PIN_B = 17
PIN_SW = 18

# Rotary encoder state
last_state = 0
position = 0
last_button_time = 0
button_pressed = False

# Setup pins
pin_a = machine.Pin(PIN_A, machine.Pin.IN, machine.Pin.PULL_UP)
pin_b = machine.Pin(PIN_B, machine.Pin.IN, machine.Pin.PULL_UP)
pin_sw = machine.Pin(PIN_SW, machine.Pin.IN, machine.Pin.PULL_UP)

def rotary_handler(pin):
    global last_state, position
    state = (pin_a.value() << 1) | pin_b.value()
    if state != last_state:
        if ((last_state == 0b00 and state == 0b01) or
            (last_state == 0b01 and state == 0b11) or
            (last_state == 0b11 and state == 0b10) or
            (last_state == 0b10 and state == 0b00)):
            print("Right")
            position += 1
        elif ((last_state == 0b00 and state == 0b10) or
              (last_state == 0b10 and state == 0b11) or
              (last_state == 0b11 and state == 0b01) or
              (last_state == 0b01 and state == 0b00)):
            print("Left")
            position -= 1
        last_state = state

def button_handler(pin):
    global last_button_time, button_pressed
    if not pin_sw.value():  # Button pressed
        last_button_time = utime.ticks_ms()
        button_pressed = True
    else:  # Button released
        if button_pressed:
            duration = utime.ticks_diff(utime.ticks_ms(), last_button_time)
            if duration > 700:
                print("Long Click")
            else:
                print("Short Click")
            button_pressed = False

# Initialize last_state
last_state = (pin_a.value() << 1) | pin_b.value()

# Attach interrupts
pin_a.irq(trigger=machine.Pin.IRQ_RISING | machine.Pin.IRQ_FALLING, handler=rotary_handler)
pin_b.irq(trigger=machine.Pin.IRQ_RISING | machine.Pin.IRQ_FALLING, handler=rotary_handler)
pin_sw.irq(trigger=machine.Pin.IRQ_RISING | machine.Pin.IRQ_FALLING, handler=button_handler)

# Main loop (keep the script running)
while True:
    utime.sleep(1)