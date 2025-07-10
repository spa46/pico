from machine import Timer

class SensorTimer:
    def __init__(self, sensor, interval_ms=2000):
        self.sensor = sensor
        self.interval_ms = interval_ms
        self.timer = None

    def _callback(self, t):
        try:
            self.sensor.measure()
        except Exception as e:
            print("Sensor measurement error:", e)

    def start(self):
        if self.timer is None:
            self.timer = Timer(-1)
            self.timer.init(period=self.interval_ms, mode=Timer.PERIODIC, callback=self._callback)

    def stop(self):
        if self.timer:
            self.timer.deinit()
            self.timer = None

