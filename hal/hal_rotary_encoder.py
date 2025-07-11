import utime
from hal.hal_pinout import gpio16, gpio17, gpio18

class RotaryEncoder:
    def __init__(self, sensitivity=4):
        self.pin_s1 = gpio16    # s1
        self.pin_s2 = gpio17    # s2
        self.pin_key = gpio18   # key

        self.on_event = None  # Unified callback: (event_type, value)


        self.last_state = (self.pin_s1.value() << 1) | self.pin_s2.value()
        self.position = 0
        self.last_button_time = 0
        self.button_pressed = False

        self.sensitivity = max(1, sensitivity)
        self.state_counter = 0
        self.last_direction = 0

        self.pin_s1.irq(trigger=self.pin_s1.IRQ_RISING | self.pin_s1.IRQ_FALLING, handler=self.rotary_handler)
        self.pin_s2.irq(trigger=self.pin_s2.IRQ_RISING | self.pin_s2.IRQ_FALLING, handler=self.rotary_handler)
        self.pin_key.irq(trigger=self.pin_key.IRQ_RISING | self.pin_key.IRQ_FALLING, handler=self.button_handler)

    def rotary_handler(self, pin):
        state = (self.pin_s1.value() << 1) | self.pin_s2.value()
        if state == self.last_state:
            return

        direction = 0
        if ((self.last_state == 0b00 and state == 0b01) or
            (self.last_state == 0b01 and state == 0b11) or
            (self.last_state == 0b11 and state == 0b10) or
            (self.last_state == 0b10 and state == 0b00)):
            direction = 1  # Right (CW)
        elif ((self.last_state == 0b00 and state == 0b10) or
              (self.last_state == 0b10 and state == 0b11) or
              (self.last_state == 0b11 and state == 0b01) or
              (self.last_state == 0b01 and state == 0b00)):
            direction = -1  # Left (CCW)

        self.last_state = state

        if direction == 0:
            self.state_counter = 0
            self.last_direction = 0
            return

        if direction != self.last_direction:
            self.state_counter = 0
            self.last_direction = direction

        self.state_counter += 1
        if self.state_counter >= self.sensitivity:
            self.state_counter = 0
            self.position += direction
            if self.on_event:
                self.on_event('rotate', direction)

    def button_handler(self, pin):
        if not self.pin_key.value():
            self.last_button_time = utime.ticks_ms()
            self.button_pressed = True
        else:
            if self.button_pressed:
                duration = utime.ticks_diff(utime.ticks_ms(), self.last_button_time)
                if duration > 700:
                    if self.on_event:
                        self.on_event('long_press', 2)
                else:
                    if self.on_event:
                        self.on_event('short_press', 1)
                self.button_pressed = False