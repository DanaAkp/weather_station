from base.subject import Subject
from random import randint
from weather_data.data import Data


class WeatherData(Subject):
    def __init__(self):
        self.list_observer = []
        self.data = Data()
        self.measurements_changed()

    def register_observer(self, obs):
        self.list_observer.append(obs)

    def remove_observer(self, obs):
        self.list_observer.remove(obs)

    def notify_observer(self):
        for i in self.list_observer:
            i.update(self.data)

    def get_temperature(self):
        return randint(-20, 20)

    def get_humidity(self):
        return randint(1, 100)

    def get_pressure(self):
        return randint(750, 770)

    def measurements_changed(self):
        self.data.pressure = self.get_pressure()
        self.data.temperature = self.get_temperature()
        self.data.humidity = self.get_humidity()

        self.data.oxygen = self.get_oxygen()
        self.data.precipitation=self.get_precipitation()
        self.data.is_fog=self.get_fog()

        self.notify_observer()

    def get_oxygen(self):
        return randint(1, 100)

    def get_precipitation(self):
        return randint(1, 100)

    def get_fog(self):
        return bool(randint(0, 1))



