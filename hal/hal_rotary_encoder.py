# examples/example_rotary_encoder.py
import utime
from hal.hal_pinout import gpio16, gpio17, gpio18

class RotaryEncoder:
    def __init__(self):
        self.pin_s1 = gpio16    # s1
        self.pin_s2 = gpio17    # s2
        self.pin_key = gpio18   # key

        self.last_state = (self.pin_s1.value() << 1) | self.pin_s2.value()
        self.position = 0
        self.last_button_time = 0
        self.button_pressed = False

        self.pin_s1.irq(trigger=self.pin_s1.IRQ_RISING | self.pin_s1.IRQ_FALLING, handler=self.rotary_handler)
        self.pin_s2.irq(trigger=self.pin_s2.IRQ_RISING | self.pin_s2.IRQ_FALLING, handler=self.rotary_handler)
        self.pin_key.irq(trigger=self.pin_key.IRQ_RISING | self.pin_key.IRQ_FALLING, handler=self.button_handler)

    def rotary_handler(self, pin):
        state = (self.pin_s1.value() << 1) | self.pin_s2.value()
        if state != self.last_state:
            if ((self.last_state == 0b00 and state == 0b01) or
                (self.last_state == 0b01 and state == 0b11) or
                (self.last_state == 0b11 and state == 0b10) or
                (self.last_state == 0b10 and state == 0b00)):
                print("Right")
                self.position += 1
            elif ((self.last_state == 0b00 and state == 0b10) or
                  (self.last_state == 0b10 and state == 0b11) or
                  (self.last_state == 0b11 and state == 0b01) or
                  (self.last_state == 0b01 and state == 0b00)):
                print("Left")
                self.position -= 1
            self.last_state = state

    def button_handler(self, pin):
        if not self.pin_key.value():  # Button pressed
            self.last_button_time = utime.ticks_ms()
            self.button_pressed = True
        else:  # Button released
            if self.button_pressed:
                duration = utime.ticks_diff(utime.ticks_ms(), self.last_button_time)
                if duration > 700:
                    print("Long Click")
                else:
                    print("Short Click")
                self.button_pressed = False

encoder = RotaryEncoder(16, 17, 18)
