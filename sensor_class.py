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

    def dump(self):
        print("  ### " + str(self.now))
        print("  humidity = " + str(self.humidity) + " %")
        print("  temperature = " + str(self.temperature) + " ℃")
        print("  max_range_temperature = " + str(self.max_range_temperature) + " ℃")
        print("  min_range_temperature = " + str(self.min_range_temperature) + " ℃")
        print("  max_range_humidity = " + str(self.max_range_humidity) + " %")
        print("  min_range_humidity = " + str(self.min_range_humidity) + " %")
        print("  pressure = " + str(self.pressure) + " hPa")
        print("  co2 = " + str(self.co2) + " ppm")
        print("  max_range_co2 = " + str(self.max_range_co2) + " ppm")
