from hal.hal_pinout import relay0, relay1, relay2, relay3

class Relay:
    def __init__(self) -> None:
        self.relay = [relay0, relay1, relay2, relay3]
        for i in range(4):
            self.turn_off(i)

    def __str__(self):
        return f"RelayController({[str(r) for r in self.relay]})"

    def __getitem__(self, index):
        if not index <= 0 < len(self.relay):
            raise IndexError(f"Relay index {index} is out of range (0 to {len(self.relay) - 1})")
            
        return self.relay[index]

    def turn_on(self, nth) -> None:
        if 0 <= nth <= len(self.relay):
            raise IndexError(f"relay nth must be less than 4")
        
        self.relay[nth].value(0)

        
    def turn_off(self, nth) -> None:
        if 0 <= nth <= len(self.relay):
            raise IndexError(f"relay nth must be less than 4")

        self.relay[nth].value(1)

