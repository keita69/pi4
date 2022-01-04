class Sensor():
    def __init__(self, now, humidity, temperature, pressure, co2):
        self.now = now
        self.humidity = humidity
        self.temperature = temperature
        self.max_range_temperature = 28
        self.min_range_temperature = 20
        self.max_range_humidity = 70
        self.min_range_humidity = 40
        self.pressure = pressure
        self.co2 = co2
        self.max_range_co2 = 1000
