def average_reading(sensor_func, samples=5, delay=0.5):
    readings = []
    for _ in range(samples):
        readings.append(sensor_func())
        utime.sleep(delay)
    return round(sum(readings) / len(readings), 2)
