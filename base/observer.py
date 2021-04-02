from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from weather_data.weather_data import WeatherData
from weather_data.data import Data


@dataclass
class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, data):
        pass
